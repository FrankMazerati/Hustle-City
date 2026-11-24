# Hustle City — Flyers and Wings Economy

## 1. Purpose and currency distinction
**Wings** are a dedicated in-game resource for the flyer system. They are separate from:
- **Diamonds:** premium travel currency.
- **Hustle Money:** ordinary in-game cash.
- **Hustle City Poker Chips:** virtual chips for poker and approved chip-based activities.

Wings must not be treated as a travel currency, poker currency, or general-purpose substitute for Diamonds or Hustle Money. No automatic conversion between currencies is allowed.

## 2. Flyer system scope
Flyers are promotional objects players can create, customize, distribute and use to publicize supported activities in Hustle City. Candidate use cases include:
- Player-hosted parties at eligible owned/managed venues.
- Club nights and venue promotions.
- Crew meetups and cruising gatherings.
- City events and community activities.
- Business promotions and special offers.

These are intended system use cases; exact flyer types, distribution limits and paid promotion features require creator approval.

## 3. Wings spending model
The established rule is that Wings are specifically for flyers. The precise actions that consume Wings remain to be approved. Potential spend points include creating a flyer, printing/publishing it in the game world, boosting its reach, distributing batches, or refreshing a campaign. Do not charge Wings for ordinary social posts or event invitations unless explicitly approved.

Every Wings action must display the action, Wings cost, expected in-game result, audience/reach limits and duration before confirmation. A flyer action should not promise a guaranteed attendance count or business revenue.

## 4. Flyer creation flow
1. Player opens Flyer Studio or an approved flyer creation surface.
2. Selects an eligible event, venue, business or gathering (or a permitted custom announcement).
3. Chooses an approved template and edits permitted text, imagery, date/time, location and host attribution.
4. Preview validates content, event status, venue permissions, time zone and moderation rules.
5. UI displays any Wings cost and campaign effect.
6. Player confirms; server atomically debits Wings and creates a flyer/campaign record.
7. Flyer becomes available in its approved distribution surfaces.
8. Owner can review status, engagement and expiry; edits/republication follow configured rules.

The name "Flyer Studio" is a working label, not approved canon.

## 5. Distribution and placement
Possible distribution surfaces include in-world flyer boards, eligible venue entrances/interiors, business counters, event listings, city feeds and approved social sharing. Placement must be data-driven and respect district/venue permissions. External sharing uses the social sharing system and does not imply that Wings buy off-platform advertising.

## 6. Data contract
Flyer definition: flyer_id, creator_id, campaign_id, template_id, linked_event_id (nullable), linked_venue_id (nullable), linked_business_id (nullable), headline, body, media_asset_id, location/placement IDs, start_at, end_at, visibility, moderation_state, wings_spent, created_at, version.
Campaign record: campaign_id, owner_id, target_surface, placement_ids, start/end, budget_wings, actual_wings_spent, impression/engagement counters where privacy-compliant, status and audit data.
Wings wallet entries use the shared economy ledger and an explicit flyer reason code. Do not create a separate, unsynchronized Wings balance.

## 7. Acquisition and monetization
Wings acquisition methods are unresolved. Potential paths for creator approval include gameplay rewards, event/crew achievements, business activity, seasonal rewards or store packages. Do not assume Wings are sold directly for real money or included in a particular package. If Wings are offered through Google Play, use the verified purchase/entitlement flow and disclose exactly what they can do.

## 8. Abuse prevention and safety
Moderate flyer text and media; prevent spam, impersonation, scams, harassment, misleading promotions and unauthorized use of venue/business identity. Rate-limit creation and distribution, enforce expiry, provide report/takedown tools and preserve audit history. Only owners/managers with appropriate permissions may advertise a private venue or business as its official host.

## 9. Unresolved creator decisions
1. Which flyer actions consume Wings: creation, publishing, boosting, physical in-world placement, distribution, or some combination?
2. How are Wings earned, granted or purchased?
3. Are flyers free to design but paid to distribute, or do all stages cost Wings?
4. Which surfaces and districts support flyer placement?
5. Do flyers link to events, businesses, venues, crews, or general player profiles?
6. Can a player edit, cancel, reuse or extend an active flyer?
7. What campaign durations, audience limits and Wings costs apply?
8. Are any flyer actions available without Wings?

## 10. QA acceptance
- Wings balance is separate from all three other currencies.
- No Diamond fare or Poker Chip action can debit Wings.
- Failed flyer creation does not consume Wings.
- Retry does not duplicate flyers or debit twice.
- Unauthorized users cannot publish for a venue/business.
- Expired or canceled events cannot be promoted as active.
- Flyer moderation, reporting, expiry and privacy controls work.
- Flyer metrics do not expose private player identities or exact locations.
