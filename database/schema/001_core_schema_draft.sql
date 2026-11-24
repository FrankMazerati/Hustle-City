-- Hustle City core schema draft.
-- Review only: do not apply until the correct Supabase project is confirmed
-- and the creator approves the schema. Generate the real migration with the
-- Supabase CLI so migration history is tracked correctly.
--
-- RLS is enabled on every application table. No broad client policies are
-- created here; access remains deny-by-default pending policy design.

create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  username text unique,
  display_name text,
  avatar_asset_id text,
  bio text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.cities (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique,
  name text not null,
  theme_key text,
  description text,
  is_available boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists public.player_characters (
  id uuid primary key default gen_random_uuid(),
  player_id uuid not null references public.profiles(id) on delete cascade,
  city_id uuid references public.cities(id) on delete set null,
  character_name text,
  appearance jsonb not null default '{}'::jsonb,
  is_active boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists player_characters_player_idx on public.player_characters(player_id);

create table if not exists public.player_city_unlocks (
  player_id uuid not null references public.profiles(id) on delete cascade,
  city_id uuid not null references public.cities(id) on delete cascade,
  unlocked_at timestamptz not null default now(),
  unlock_source text,
  primary key (player_id, city_id)
);

create table if not exists public.player_home_cities (
  player_id uuid primary key references public.profiles(id) on delete cascade,
  city_id uuid not null references public.cities(id) on delete restrict,
  selected_at timestamptz not null default now()
);

create table if not exists public.districts (
  id uuid primary key default gen_random_uuid(),
  city_id uuid not null references public.cities(id) on delete cascade,
  slug text not null,
  name text not null,
  district_order integer,
  map_metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  unique (city_id, slug),
  unique (city_id, district_order)
);

create table if not exists public.neighborhoods (
  id uuid primary key default gen_random_uuid(),
  city_id uuid not null references public.cities(id) on delete cascade,
  district_id uuid references public.districts(id) on delete set null,
  slug text not null,
  name text not null,
  master_grid_x integer check (master_grid_x between 1 and 7),
  master_grid_y integer check (master_grid_y between 1 and 7),
  boundary_metadata jsonb not null default '{}'::jsonb,
  expansion_status text not null default 'planned'
    check (expansion_status in ('planned','available','claimed','active','full','archived')),
  created_at timestamptz not null default now(),
  unique (city_id, slug)
);

-- Ownership and residency are deliberately different tables.
create table if not exists public.neighborhood_ownership (
  id uuid primary key default gen_random_uuid(),
  neighborhood_id uuid not null unique references public.neighborhoods(id) on delete cascade,
  owner_player_id uuid not null references public.profiles(id) on delete restrict,
  founder_player_id uuid not null references public.profiles(id) on delete restrict,
  claimed_at timestamptz not null default now(),
  ownership_status text not null default 'active'
    check (ownership_status in ('active','transferred','relinquished','suspended'))
);
create index if not exists neighborhood_ownership_owner_idx on public.neighborhood_ownership(owner_player_id);

create table if not exists public.neighborhood_residencies (
  id uuid primary key default gen_random_uuid(),
  neighborhood_id uuid not null references public.neighborhoods(id) on delete cascade,
  player_id uuid not null references public.profiles(id) on delete cascade,
  residency_status text not null default 'resident'
    check (residency_status in ('resident','visitor','former_resident')),
  started_at timestamptz not null default now(),
  ended_at timestamptz,
  unique (neighborhood_id, player_id),
  check (ended_at is null or ended_at >= started_at)
);

create table if not exists public.city_blocks (
  id uuid primary key default gen_random_uuid(),
  neighborhood_id uuid not null references public.neighborhoods(id) on delete cascade,
  grid_x integer not null check (grid_x between 1 and 5),
  grid_y integer not null check (grid_y between 1 and 5),
  block_name text,
  world_metadata jsonb not null default '{}'::jsonb,
  activation_status text not null default 'planned'
    check (activation_status in ('planned','ambient','interactive','under_construction','archived')),
  unique (neighborhood_id, grid_x, grid_y)
);

create table if not exists public.crews (
  id uuid primary key default gen_random_uuid(),
  city_id uuid references public.cities(id) on delete set null,
  name text not null,
  slug text not null unique,
  description text,
  founded_by_player_id uuid references public.profiles(id) on delete set null,
  headquarters_neighborhood_id uuid references public.neighborhoods(id) on delete set null,
  crew_status text not null default 'active'
    check (crew_status in ('active','inactive','disbanded')),
  created_at timestamptz not null default now()
);

create table if not exists public.crew_memberships (
  id uuid primary key default gen_random_uuid(),
  crew_id uuid not null references public.crews(id) on delete cascade,
  player_id uuid not null references public.profiles(id) on delete cascade,
  membership_status text not null default 'active'
    check (membership_status in ('invited','active','paused','left','removed')),
  joined_at timestamptz,
  ended_at timestamptz,
  unique (crew_id, player_id),
  check (ended_at is null or joined_at is null or ended_at >= joined_at)
);

create table if not exists public.crew_leadership (
  id uuid primary key default gen_random_uuid(),
  crew_id uuid not null references public.crews(id) on delete cascade,
  player_id uuid not null references public.profiles(id) on delete restrict,
  leadership_role text not null,
  appointed_at timestamptz not null default now(),
  ended_at timestamptz,
  check (ended_at is null or ended_at >= appointed_at)
);
create index if not exists crew_leadership_active_idx on public.crew_leadership(crew_id, player_id) where ended_at is null;

create table if not exists public.properties (
  id uuid primary key default gen_random_uuid(),
  city_id uuid not null references public.cities(id) on delete cascade,
  neighborhood_id uuid references public.neighborhoods(id) on delete set null,
  city_block_id uuid references public.city_blocks(id) on delete set null,
  name text not null,
  property_type text not null,
  property_status text not null default 'available'
    check (property_status in ('planned','available','owned','leased','inactive')),
  world_asset_key text,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists public.property_ownership (
  id uuid primary key default gen_random_uuid(),
  property_id uuid not null references public.properties(id) on delete cascade,
  player_id uuid not null references public.profiles(id) on delete restrict,
  ownership_share numeric(5,2) not null default 100 check (ownership_share > 0 and ownership_share <= 100),
  acquired_at timestamptz not null default now(),
  released_at timestamptz,
  check (released_at is null or released_at >= acquired_at)
);

create table if not exists public.businesses (
  id uuid primary key default gen_random_uuid(),
  city_id uuid not null references public.cities(id) on delete cascade,
  property_id uuid references public.properties(id) on delete set null,
  name text not null,
  business_type text not null,
  business_status text not null default 'planned'
    check (business_status in ('planned','open','closed','suspended')),
  operating_data jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists public.business_ownership (
  id uuid primary key default gen_random_uuid(),
  business_id uuid not null references public.businesses(id) on delete cascade,
  player_id uuid not null references public.profiles(id) on delete restrict,
  ownership_share numeric(5,2) not null default 100 check (ownership_share > 0 and ownership_share <= 100),
  acquired_at timestamptz not null default now(),
  released_at timestamptz,
  check (released_at is null or released_at >= acquired_at)
);

-- Four distinct currencies: Hustle Money, Diamonds, Poker Chips and Wings. The ledger, not a client-supplied balance, is authoritative.
create table if not exists public.wallet_accounts (
  id uuid primary key default gen_random_uuid(),
  player_id uuid references public.profiles(id) on delete cascade,
  crew_id uuid references public.crews(id) on delete cascade,
  currency_code text not null check (currency_code in ('HUSTLE_MONEY','DIAMONDS','POKER_CHIPS','WINGS')),
  created_at timestamptz not null default now(),
  check ((player_id is not null and crew_id is null) or (player_id is null and crew_id is not null))
);
create unique index if not exists wallet_accounts_player_currency_uq on public.wallet_accounts(player_id, currency_code) where player_id is not null;
create unique index if not exists wallet_accounts_crew_currency_uq on public.wallet_accounts(crew_id, currency_code) where crew_id is not null;

create table if not exists public.wallet_transactions (
  id uuid primary key default gen_random_uuid(),
  idempotency_key text not null unique,
  transaction_type text not null,
  transaction_status text not null default 'posted'
    check (transaction_status in ('pending','posted','reversed','rejected')),
  source_reference text,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists public.wallet_entries (
  id uuid primary key default gen_random_uuid(),
  transaction_id uuid not null references public.wallet_transactions(id) on delete restrict,
  wallet_account_id uuid not null references public.wallet_accounts(id) on delete restrict,
  amount_delta bigint not null check (amount_delta <> 0),
  created_at timestamptz not null default now()
);
create index if not exists wallet_entries_account_created_idx on public.wallet_entries(wallet_account_id, created_at desc);

create table if not exists public.inventory_items (
  id uuid primary key default gen_random_uuid(),
  item_key text not null unique,
  display_name text not null,
  item_category text not null,
  item_metadata jsonb not null default '{}'::jsonb,
  is_tradeable boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists public.player_inventory (
  id uuid primary key default gen_random_uuid(),
  player_id uuid not null references public.profiles(id) on delete cascade,
  item_id uuid not null references public.inventory_items(id) on delete restrict,
  quantity integer not null default 1 check (quantity > 0),
  acquired_at timestamptz not null default now(),
  unique (player_id, item_id)
);

create table if not exists public.collectible_cards (
  id uuid primary key default gen_random_uuid(),
  card_key text not null unique,
  collection_name text,
  display_name text not null,
  rarity text,
  card_metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists public.player_cards (
  id uuid primary key default gen_random_uuid(),
  player_id uuid not null references public.profiles(id) on delete cascade,
  card_id uuid not null references public.collectible_cards(id) on delete restrict,
  quantity integer not null default 1 check (quantity > 0),
  acquired_at timestamptz not null default now(),
  unique (player_id, card_id)
);

create table if not exists public.card_packs (
  id uuid primary key default gen_random_uuid(),
  pack_key text not null unique,
  display_name text not null,
  collection_name text,
  pack_metadata jsonb not null default '{}'::jsonb,
  is_available boolean not null default false
);

create table if not exists public.venues (
  id uuid primary key default gen_random_uuid(),
  city_id uuid not null references public.cities(id) on delete cascade,
  neighborhood_id uuid references public.neighborhoods(id) on delete set null,
  property_id uuid references public.properties(id) on delete set null,
  venue_key text not null unique,
  name text not null,
  venue_type text not null,
  venue_status text not null default 'planned'
    check (venue_status in ('planned','open','closed','maintenance')),
  capacity integer check (capacity is null or capacity >= 0),
  venue_metadata jsonb not null default '{}'::jsonb
);

-- The location's five collectible pack slots are represented as slots 1 through 5.
create table if not exists public.card_pack_placements (
  id uuid primary key default gen_random_uuid(),
  venue_id uuid not null references public.venues(id) on delete cascade,
  card_pack_id uuid not null references public.card_packs(id) on delete restrict,
  pack_slot smallint not null check (pack_slot between 1 and 5),
  is_active boolean not null default true,
  unique (venue_id, pack_slot),
  unique (venue_id, card_pack_id)
);

create table if not exists public.venue_presence (
  id uuid primary key default gen_random_uuid(),
  venue_id uuid not null references public.venues(id) on delete cascade,
  player_id uuid not null references public.profiles(id) on delete cascade,
  entered_at timestamptz not null default now(),
  exited_at timestamptz,
  presence_state text not null default 'present' check (presence_state in ('present','away','exited')),
  check (exited_at is null or exited_at >= entered_at)
);
create index if not exists venue_presence_active_idx on public.venue_presence(venue_id, player_id) where exited_at is null;

create table if not exists public.venue_tables (
  id uuid primary key default gen_random_uuid(),
  venue_id uuid not null references public.venues(id) on delete cascade,
  table_key text not null,
  activity_type text not null,
  seat_capacity smallint not null check (seat_capacity > 0),
  table_status text not null default 'available' check (table_status in ('available','in_use','disabled')),
  unique (venue_id, table_key)
);

create table if not exists public.table_seats (
  id uuid primary key default gen_random_uuid(),
  venue_table_id uuid not null references public.venue_tables(id) on delete cascade,
  seat_number smallint not null check (seat_number > 0),
  player_id uuid references public.profiles(id) on delete set null,
  seat_status text not null default 'available' check (seat_status in ('available','reserved','occupied','blocked')),
  occupied_at timestamptz,
  unique (venue_table_id, seat_number)
);

create table if not exists public.social_conversations (
  id uuid primary key default gen_random_uuid(),
  conversation_type text not null check (conversation_type in ('private','group','crew','nearby','table')),
  created_by_player_id uuid references public.profiles(id) on delete set null,
  created_at timestamptz not null default now()
);

create table if not exists public.conversation_participants (
  conversation_id uuid not null references public.social_conversations(id) on delete cascade,
  player_id uuid not null references public.profiles(id) on delete cascade,
  joined_at timestamptz not null default now(),
  left_at timestamptz,
  primary key (conversation_id, player_id)
);

create table if not exists public.messages (
  id uuid primary key default gen_random_uuid(),
  conversation_id uuid not null references public.social_conversations(id) on delete cascade,
  sender_player_id uuid not null references public.profiles(id) on delete restrict,
  message_body text not null,
  created_at timestamptz not null default now(),
  edited_at timestamptz,
  deleted_at timestamptz
);
create index if not exists messages_conversation_created_idx on public.messages(conversation_id, created_at desc);

create table if not exists public.contact_exchange_requests (
  id uuid primary key default gen_random_uuid(),
  requester_player_id uuid not null references public.profiles(id) on delete cascade,
  recipient_player_id uuid not null references public.profiles(id) on delete cascade,
  request_status text not null default 'pending' check (request_status in ('pending','accepted','declined','cancelled')),
  created_at timestamptz not null default now(),
  responded_at timestamptz,
  check (requester_player_id <> recipient_player_id)
);

create table if not exists public.city_events (
  id uuid primary key default gen_random_uuid(),
  city_id uuid not null references public.cities(id) on delete cascade,
  venue_id uuid references public.venues(id) on delete set null,
  event_key text not null unique,
  name text not null,
  event_type text not null,
  event_status text not null default 'scheduled' check (event_status in ('draft','scheduled','live','completed','cancelled')),
  starts_at timestamptz,
  ends_at timestamptz,
  event_metadata jsonb not null default '{}'::jsonb,
  check (ends_at is null or starts_at is null or ends_at >= starts_at)
);

create table if not exists public.event_participants (
  event_id uuid not null references public.city_events(id) on delete cascade,
  player_id uuid not null references public.profiles(id) on delete cascade,
  participation_status text not null default 'joined' check (participation_status in ('interested','joined','watching','left')),
  joined_at timestamptz not null default now(),
  primary key (event_id, player_id)
);

create table if not exists public.vehicles (
  id uuid primary key default gen_random_uuid(),
  city_id uuid not null references public.cities(id) on delete cascade,
  vehicle_key text not null unique,
  display_name text not null,
  vehicle_type text not null,
  capacity smallint check (capacity is null or capacity >= 0),
  vehicle_metadata jsonb not null default '{}'::jsonb
);

create table if not exists public.vehicle_ownership (
  id uuid primary key default gen_random_uuid(),
  vehicle_id uuid not null references public.vehicles(id) on delete cascade,
  player_id uuid not null references public.profiles(id) on delete restrict,
  acquired_at timestamptz not null default now(),
  released_at timestamptz
);

create table if not exists public.travel_trips (
  id uuid primary key default gen_random_uuid(),
  city_id uuid not null references public.cities(id) on delete cascade,
  requested_by_player_id uuid not null references public.profiles(id) on delete restrict,
  vehicle_id uuid references public.vehicles(id) on delete set null,
  origin_key text not null,
  destination_key text not null,
  travel_mode text not null,
  trip_status text not null default 'requested'
    check (trip_status in ('requested','validated','boarding','in_progress','arrived','cancelled','recovered')),
  requested_at timestamptz not null default now(),
  completed_at timestamptz,
  trip_metadata jsonb not null default '{}'::jsonb,
  check (origin_key <> destination_key)
);

-- RLS is on for all public application tables. Table-specific policies are
-- intentionally deferred until the trusted server boundary is designed.
alter table public.profiles enable row level security;
alter table public.cities enable row level security;
alter table public.player_characters enable row level security;
alter table public.player_city_unlocks enable row level security;
alter table public.player_home_cities enable row level security;
alter table public.districts enable row level security;
alter table public.neighborhoods enable row level security;
alter table public.neighborhood_ownership enable row level security;
alter table public.neighborhood_residencies enable row level security;
alter table public.city_blocks enable row level security;
alter table public.crews enable row level security;
alter table public.crew_memberships enable row level security;
alter table public.crew_leadership enable row level security;
alter table public.properties enable row level security;
alter table public.property_ownership enable row level security;
alter table public.businesses enable row level security;
alter table public.business_ownership enable row level security;
alter table public.wallet_accounts enable row level security;
alter table public.wallet_transactions enable row level security;
alter table public.wallet_entries enable row level security;
alter table public.inventory_items enable row level security;
alter table public.player_inventory enable row level security;
alter table public.collectible_cards enable row level security;
alter table public.player_cards enable row level security;
alter table public.card_packs enable row level security;
alter table public.venues enable row level security;
alter table public.card_pack_placements enable row level security;
alter table public.venue_presence enable row level security;
alter table public.venue_tables enable row level security;
alter table public.table_seats enable row level security;
alter table public.social_conversations enable row level security;
alter table public.conversation_participants enable row level security;
alter table public.messages enable row level security;
alter table public.contact_exchange_requests enable row level security;
alter table public.city_events enable row level security;
alter table public.event_participants enable row level security;
alter table public.vehicles enable row level security;
alter table public.vehicle_ownership enable row level security;
alter table public.travel_trips enable row level security;
