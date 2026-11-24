# Hustle City — Gameplay State and Acceptance Criteria

## 1. Shared identifiers
All systems must use stable IDs for player, account, currency, transaction, card definition, card instance, collection, pack, building, ownership, property, business, vehicle, catalogue item, event, venue, travel booking, referral and social post. Avoid display-name joins and duplicate sources of truth.

## 2. Authority boundaries
Server-authoritative: balances, ledger, paid entitlements, card ownership, pack outcomes, trades, collection completion, building unlock/claim, property/business ownership, upgrade effects, travel charges, referral qualification, event capacity and moderation state. Clients request actions and display confirmed state.

## 3. Cross-system invariants
- Four currencies (Hustle Money, Diamonds, Wings and Poker Chips) remain separate and never merge or silently convert.
- Basic transportation never requires Diamonds.
- Poker Chips are non-redeemable virtual chips under the baseline.
- Each eligible building (except the beach), boat/yacht and car/dealership collection uses the standard five-card ranked ladder; completing all five unlocks only its configured ownership claim. Ten-card prestige collections require separate creator approval.
- Building ownership is distinct from neighborhood ownership, crew leadership and residency.
- Card trade is atomic and cannot duplicate or destroy cards.
- Platform purchase grants only after server receipt validation.
- Social privacy applies consistently to feeds, map, convoys and notifications.
- Private messages never leak into public feeds.
- Event hosting requires venue rights and respects capacity.
- Every paid/earned grant has an auditable transaction or entitlement record.
- All retries are idempotent.
- No player death; safety/recovery rules remain in force.

## 4. End-to-end acceptance scenarios
1. New player joins, creates profile, sees four separate wallet balances and understands their uses.
2. Player takes a basic ride using free/Hustle Money service without Diamonds.
3. Player selects premium travel, sees Diamond fare and confirms before debit.
4. Player opens a card pack; server records one debit and one unique result despite retry.
5. Player obtains four of five building cards; UI shows 4/5 and does not unlock building.
6. Player obtains the fifth required card; exact configured building unlocks; claim flow checks availability and eligibility.
7. Player claims the building; ownership appears in map/profile/dashboard after reconnect.
8. Owner upgrades the venue; wallet and upgrade state update atomically.
9. Owner schedules a party, invites crew, posts to permitted venue feed and receives RSVPs.
10. Player shares “I just joined Hustle City. Join me over here. Here's my link” externally; attribution is tracked without exposing private data.
11. Qualified referral grants only the approved rewards once.
12. Two players trade cards; concurrent attempts cannot duplicate or lose an instance.
13. Player hides location; feed/map/convoy presence respects the choice.
14. Google Play purchase is pending/canceled/refunded; no unauthorized grant remains.
15. Player buys clothing/accessory and equips it; ownership persists across sessions.
16. Vehicle/apartment/business upgrade validates prerequisites and shows only implemented effects.
17. Event reaches capacity; extra RSVP/entry is rejected gracefully and host sees accurate count.
18. Player disconnects during travel, trade, pack opening or purchase; state reconciles safely on return.

## 5. Card rewards and in-game trading acceptance
- Daily login reward configuration can grant building-specific, selectable or general card packs through the canonical pack service.
- Poker gameplay rewards can grant approved cards/packs through defined participation or achievement milestones without making high-stakes play necessary for essential collection progression.
- Player can add another player as a friend, manage requests and block/report users.
- Player can search for a missing building card and find eligible traders inside Hustle City.
- Card Album, wish lists, inventory visibility and Card Finder obey privacy settings.
- Players can propose multi-card exchanges, counteroffer and approve exact final terms.
- Both parties approve the same trade version before the server atomically transfers all cards.
- Pending offers reserve cards; cancel/decline/expiry releases them; reconnect and retries preserve the authoritative state.
- Trade history, notifications, abuse reporting and moderator audit trail function in-game.
- No external app, website, Discord, Facebook group or spreadsheet is needed to discover, negotiate or complete a card trade.

## 5. Daily rewards and streak acceptance
- One qualifying login can claim at most one daily reward per server-defined reward day.
- Daily reward may grant Hustle Money, Diamonds or Poker Chips; Wings are excluded unless a creator-approved reward configuration explicitly includes them.
- Seven consecutive daily claims trigger one separate weekly bonus in addition to the seventh daily reward.
- A missed-day/streak policy is explicitly configured and displayed; it is never inferred by the client.
- Optional prize wheel has one configured spin entitlement per eligible period; outcome is server-selected before the client animation.
- Wheel odds/prize pool are disclosed; duplicate requests, retries and reconnects cannot produce extra spins or grants.
- All reward grants create auditable ledger entries and update the corresponding separate wallet.
- Reward schedules and wheel pools are versioned and can be rolled back without altering already-earned grants.


## Venue collection and property progression acceptance
- Each configured building/venue collection has exactly five ranked card slots and a stable target/collection mapping.
- Completing a set grants only its configured entitlement; it cannot accidentally grant venue ownership, casino operation, all vehicles at a dealership or all boats at a marina.
- A new Hustle Towers player can be represented as an apartment tenant; completing the correct apartment-specific five-card set unlocks a permanent ownership claim for that apartment.
- Rental state and permanent ownership state remain distinct across reconnects and devices; rent terms and expiry behavior are explicit configuration, not inferred.
- Shuffle Club remains a shared venue and is never granted as player-owned property. Its configured card collection can grant private-room access only. Casino remains an experience inside the Shuffle Club unless separately approved as a distinct collection (not a separate building by default).
- Velvet Lounge collection completion does not grant an unspecified reward; the system blocks publishing an unapproved completion entitlement.
- Marina/yacht-club venue collection and dealership collection are separate from individual boat and car collections.
- Beach has no five-card building ownership collection.

## Creator-approved ownership and production acceptance
- Monster Beats is represented as a production company/facility; a player may own a studio inside it and produce music, but cannot acquire ownership of the Monster Beats building/company through that studio collection.
- A player can establish a film crew and make movies using the Upper Level studio/production facility without automatically owning that facility.
- A car-lot collection grants the configured individual lot, not the entire dealership group or every vehicle.
- A clothing-store collection grants the configured store.
- A yacht collection grants the individual yacht and never the Hustle City Marina and Yacht Club.
- Hustle Club and Velvet Lounge collections can grant their respective venue/business ownership.
- Shuffle Club/casino collection grants private-room access only; no player can claim ownership of the Shuffle Club or casino.
- Hustle Towers apartment collection grants permanent ownership of the specific apartment; rental remains a distinct state.
- All these outcomes are represented by separate entitlement types and cannot accidentally grant the host building or adjacent assets.

## Universal social-sharing and reward acceptance
- Every meaningful gameplay feature includes a documented shareability decision: eligible authoritative events, generated artifact, privacy rules, supported share destinations, reward policy and referral opportunity.
- Share artifacts are generated only from confirmed server state and never reveal private player data or hidden content.
- Share proof is bound to a unique share event and player; screenshot evidence is treated as evidence for review, not definitive proof of a live public post.
- Proof review supports pending, approved, rejected and appeal/retry states; ambiguous evidence can be escalated for human review.
- Only an approved, configured claim can issue a share reward; duplicate submissions, retries and concurrent requests cannot create duplicate grants.
- Referral rewards are separate from share rewards and require a server-verified new-player qualifying milestone.
- Referral attribution, proof decisions, reward grants/reversals and fraud actions are auditable.
- Sharing is optional and never a prerequisite for core gameplay progression.
- Social sharing integrations obey platform policies; no social passwords, unauthorized scraping or unsupported direct-posting claims.
- Share artifacts, feeds and referral flows obey player privacy, block/report and moderation settings.

## 5. QA evidence required
For each feature, retain test ID, build/version, account fixtures, setup, action, expected result, actual result, server log/transaction reference, pass/fail and defect link. QA supervisors must independently verify economy, card/ownership and social privacy boundaries.

## 6. Not ready for production until approved
Exact pack odds/prices, card catalog, building-to-five-card mappings, card consumption policy, currency earn/spend table, Play Store SKUs/prices, Diamond travel fares, upgrade effects/prices, referral payouts, poker variants/stakes/venue layout and event capacity policies.


## Expandable content and progression acceptance
- New approved asset collections can be added through versioned data/configuration and stable IDs without schema redesign or hard-coded collection-count limits.
- A new collection points to one exact asset/privilege entitlement and preserves host-building ownership boundaries.
- New card packs can be released, scheduled, retired or rolled back without deleting owned cards, breaking trades, invalidating completed collections or revoking earned entitlements.
- Player level/XP, stats, reputation, stars/prestige, achievements, business/crew progression and collection milestones are stored as distinct tracks with versioned rules.
- Adding a progression track or new level/reward band does not require resetting existing player progress.
- No level cap, XP curve, stat formula, star scale, pack odds, card quantity or expansion cadence is hard-coded as final before creator approval.
- All new rewards, packs, progression changes and entitlements remain server-authoritative, idempotent and auditable.
