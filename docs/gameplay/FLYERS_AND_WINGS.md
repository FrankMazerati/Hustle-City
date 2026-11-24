# Hustle City — Flyer Promotion System

## 1. Purpose and currency distinction
The flyer system lets players create, customize and distribute promotional material. **Wings are not the flyer currency; creator-confirmed, Wings are reserved for flying and air-travel services.** The four currencies are Hustle Money (ordinary in-game purchases), Diamonds (boats and cars), Wings (flying) and Poker Chips (poker play). Flyer creation and promotion costs remain unresolved; do not debit Wings for flyers.

## 2. Flyer system scope
Flyers are promotional objects players can create, customize, distribute and use to publicize supported activities in Hustle City. Candidate use cases include:
- Player-hosted parties at eligible owned/managed venues.
- Club nights and venue promotions.
- Crew meetups and cruising gatherings.
- City events and community activities.
- Business promotions and special offers.

These are intended system use cases; exact flyer types, distribution limits and paid promotion features require creator approval.

## 3. Flyer cost model
The currency or entitlement used for flyer creation, publishing, distribution and boosting is unresolved. Do not charge Wings for flyer actions. The creator may later decide that flyer design is free and that distribution or boosting uses Hustle Money or a separately approved mechanism. Until then, show no assumed cost and do not debit any wallet.

Every paid flyer action must display its cost, expected in-game result, audience/reach limits and duration before confirmation. A flyer action should not promise a guaranteed attendance count or business revenue.

## 4. Flyer creation flow
1. Player opens Flyer Studio or an approved flyer creation surface.
2. Selects an eligible event, venue, business or gathering (or a permitted custom announcement).
3. Chooses an approved template and edits permitted text, imagery, date/time, location and host attribution.
4. Preview validates content, event status, venue permissions, time zone and moderation rules.
5. UI displays any approved cost and campaign effect; no Wings debit is permitted.
6. Player confirms; server atomically debits Wings and creates a flyer/campaign record.
7. Flyer becomes available in its approved distribution surfaces.
8. Owner can review status, engagement and expiry; edits/republication follow configured rules.

The name "Flyer Studio" is a working label, not approved canon.

## 5. Distribution and placement
Possible distribution surfaces include in-world flyer boards, eligible venue entrances/interiors, business counters, event listings, city feeds and approved social sharing. Placement must be data-driven and respect district/venue permissions. External sharing uses the social sharing system and does not imply that Wings buy off-platform advertising.

## 6. Data contract
Flyer definition: flyer_id, creator_id, campaign_id, template_id, linked_event_id (nullable), linked_venue_id (nullable), linked_business_id (nullable), headline, body, media_asset_id, location/placement IDs, start_at, end_at, visibility, moderation_state, currency_spent, created_at, version.
Campaign record: campaign_id, owner_id, target_surface, placement_ids, start/end, budget_amount, actual_amount_spent, impression/engagement counters where privacy-compliant, status and audit data.
Any approved flyer charge uses the shared economy ledger with an explicit flyer reason code. Do not debit Wings.

## 7. Acquisition and monetization
Flyer promotion pricing and any related earn/purchase method are unresolved. Do not list Wings as a flyer package; Wings are reserved for flying. If a flyer-related product is later offered through Google Play, use verified purchase/entitlement flow and disclose exactly what it provides.

## 8. Abuse prevention and safety
Moderate flyer text and media; prevent spam, impersonation, scams, harassment, misleading promotions and unauthorized use of venue/business identity. Rate-limit creation and distribution, enforce expiry, provide report/takedown tools and preserve audit history. Only owners/managers with appropriate permissions may advertise a private venue or business as its official host.

## 9. Unresolved creator decisions
1. Which flyer actions, if any, have a cost, and which currency or entitlement applies?
2. Are flyers free to design but paid to distribute, or do all stages cost Hustle Money?
3. Which surfaces and districts support flyer placement?
4. Do flyers link to events, businesses, venues, crews, or general player profiles?
5. Can a player edit, cancel, reuse or extend an active flyer?
6. What campaign durations and audience limits apply?
7. Are any flyer actions always free?

## 10. QA acceptance
- Wings balance is reserved for flying and remains separate from the other three currencies.
- No flyer action can debit Wings; Wings are reserved for flying.
- Failed flyer creation does not consume Wings.
- Retry does not duplicate flyers or debit twice.
- Unauthorized users cannot publish for a venue/business.
- Expired or canceled events cannot be promoted as active.
- Flyer moderation, reporting, expiry and privacy controls work.
- Flyer metrics do not expose private player identities or exact locations.
