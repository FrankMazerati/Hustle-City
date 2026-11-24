# Hustle City — In-App Store, Hustle Club Memberships, Rewards, Advertising and Revenue

**Status:** Creator-defined product direction plus implementation specification. Candidate prices and ad ideas are recorded exactly; benefit quantities, package contents, ad-network settings and forecasts remain unapproved until measured and configured.

## 1. Store identity and purchase paths

The player-facing storefront is the **Hustle City In-App Store** (the store for Play Store / in-app purchases). Inside it, players can:
- Become a **Hustle Club Member** through a monthly subscription tier.
- Buy one-time individual packages without subscribing.
- Buy currency bundles and individually listed game goods.
- Review purchases, membership status, receipts, grants and support options.

Do not confuse the Hustle City In-App Store with a physical in-world retail shop. The in-world bar, clubs, dealerships and clothing stores remain gameplay locations; the In-App Store is the platform commerce interface.

## 2. Hustle Club monthly membership ladder

Creator-proposed monthly USD price points:

| Membership level (working labels) | Candidate price / month | Benefit contents |
|---|---:|---|
| Hustle Club $9.99 | $9.99 | To be defined |
| Hustle Club $19.99 | $19.99 | To be defined |
| Hustle Club $29 | $29.00 | To be defined |
| Hustle Club $39 | $39.00 | To be defined |
| Hustle Club $49 | $49.00 | To be defined |
| Hustle Club $59 | $59.00 | To be defined |

The six price points are recorded as the creator's proposed ladder, not a finalized launch catalogue. Tier names, quantities, entitlements, regional pricing, taxes and exact benefits need creator approval and Play billing configuration. The client retrieves localized price strings from Google Play; do not hardcode US prices as universal prices.

### Benefit matrix to author and approve
Each tier must specify exact quantities and cadence, rather than vague claims of “more value.” Candidate benefit columns:
- Hustle Money grant.
- Diamonds grant (travel currency).
- Wings grant (flyer currency).
- Hustle City Poker Chips grant.
- Card pack or card benefit, with full odds/guarantee disclosure.
- Member cosmetics: profile badge/frame, clothing, jewelry or exclusive styles.
- Convenience and customization entitlements.
- Member social recognition or member-only optional events, if approved.

No tier benefits or amounts are yet canon. Do not assume membership includes every currency. No membership should be required for core travel, basic social participation or ordinary progression. Membership is not a substitute for separately owned permanent items.

## 3. One-time individual packages

All listed categories must be represented in the catalogue and can be offered individually or grouped into creator-approved packages:

| Store category | Purchase examples | Currency / entitlement |
|---|---|---|
| Hustle Money | Cash bundles | Hustle Money |
| Diamonds | Travel-currency bundles | Diamonds |
| Wings | Flyer-resource bundles | Wings |
| Poker Chips | Table-chip bundles | Hustle City Poker Chips |
| Cards | Card packs; a specific last-missing-card offer if approved | Card inventory |
| Vehicles | Cars, cosmetics and eligible upgrades | Permanent ownership / upgrade |
| Fashion | Clothing, shoes, outfits and accessories | Cosmetic inventory |
| Jewelry | Jewelry and accessories | Cosmetic inventory |
| Property | Apartment items and eligible building upgrades | Property inventory / upgrade |
| Businesses and venues | Business, club and venue upgrades | Business state |
| Flyers and events | Flyer templates, visual styles or distribution boosts | Cosmetic entitlement / Wings where approved |

**Currency terminology:** Diamonds are for premium travel. Wings are for flyers. Hustle Money is ordinary in-game cash. Hustle City Poker Chips are virtual poker/table chips. The creator also said “poker money”; whether this is simply another name for Poker Chips or a distinct fifth balance is unresolved. Until confirmed, treat “poker money” as a display/search synonym for Poker Chips, not a separate currency or conversion path.

Building/property upgrades bought with **actual money** must be represented as real-money in-app products only when explicitly sold through platform billing. Ordinary in-world upgrades paid with Hustle Money remain a separate gameplay transaction. Store listings must state which one is being purchased.

For every SKU define product ID, title, itemized contents, purchase type, localized platform price, eligibility, repeat limit, prerequisites, permanence/expiry, grant behavior, refund/revoke policy, regional availability, disclosures and approval state. No invented prices, currency quantities, card odds or upgrade costs.

## 4. Daily login rewards and return loop

Provide a daily reward claim system:
- One claim per eligible player per defined reset period.
- Display the reward before claim and show the next reset time in the player's local timezone.
- Reward schedule is server-authoritative and versioned.
- Candidate reward types: Hustle Money, Poker Chips, Wings, Diamonds only if explicitly balanced, card packs, cosmetics or temporary boosts.
- Exact amounts, sequence length, streak behavior, missed-day handling and eligibility are unresolved.
- Do not punish players with harsh streak loss or imply a purchase is required to claim a daily reward.
- Record claim idempotently so reconnects, retries or multiple devices cannot duplicate rewards.

Daily rewards are a retention mechanic, not an unbounded currency faucet. Monitor earned/spent balances, inflation and impact on paid purchases.

## 5. The Bar: social hub, recovery and ad-supported dwell time

The in-world **bar** is a real social destination and recovery location, not merely a blocking timer:
- Players can enter when energy is low and/or when they have run out of Poker Chips.
- The bar has a DJ area, social seating, player presence, chat/emotes and licensed music playback once the necessary music rights are secured.
- Players may socialize while waiting for recovery. Do not force an ad view to enter, sit, socialize or receive baseline recovery.
- Poker Chip recovery and energy recovery are separate meters with separate server rules. The creator suggested a wait of roughly 30 minutes for poker money/chips to restore; this is a tentative balancing idea, not a final timer.
- Show the remaining recovery time and any recovery cap/next grant clearly.
- Optional rewarded ads may offer a clearly disclosed, capped bonus (for example, a limited acceleration or extra small reward) after the player chooses to watch. Reward amounts and daily caps remain unresolved.
- A player who does not watch ads still receives the standard recovery benefit.

Music: DJ playback uses real-world music only after licenses/rights for the relevant compositions, recordings, territories, platforms and usage have been obtained. Until then, use original, commissioned or properly licensed tracks. The music system needs track metadata, territory/rights windows, reporting and takedown controls.

## 6. Advertising formats and player-respect rules

The creator wants bottom-of-screen ads that recur, optional ads at the bar, and interstitial ads. These are distinct formats:

1. **Banner/display ads:** persistent placement at the bottom of eligible screens. The creator suggested a 10–15 second recurrence/refresh concept. Do not force-refresh or rotate banners on a timer unless the selected ad network explicitly permits that refresh interval and placement. Implement refresh according to the provider's current policy and actual ad response; treat 10–15 seconds as a creator idea to validate, not a committed technical setting. Keep the banner outside gameplay controls and safe areas.
2. **Rewarded video ads:** player voluntarily taps to watch, sees the exact reward before starting, can decline without penalty, and receives the reward only after a verified completion callback. The bar is a natural optional location for these offers.
3. **Interstitial ads:** full-screen ads only at natural transitions (e.g. after leaving a completed activity or between sessions), never during poker hands, driving, conversation, purchase checkout, active social moments, or recovery interaction. Use conservative frequency caps, cooldowns, session caps and a remote kill switch.

Never stack an interstitial immediately after a rewarded ad or show one simply because the player entered the bar. No ad should block the basic bar recovery loop. Respect age, consent, privacy, regional restrictions, ad-network policies and store requirements. Do not reward clicks, impressions or accidental taps; reward only valid completed rewarded-ad events.

### Ad configuration fields
Store placement_id, format, screen/context, enabled flag, network, refresh policy, frequency cap, cooldown, session cap, daily cap, consent requirement, eligible age/region, reward definition (rewarded only), experiment/version and remote kill switch. All caps are server/config controlled and auditable.

## 7. Subscription lifecycle and entitlement integrity

Subscription states: not_subscribed, pending, active, grace_period, billing_retry, auto_renew_off, paused (if supported), expired and revoked.
1. Player compares tiers, benefits, localized price, billing interval, renewal and cancellation terms.
2. Google Play checkout is invoked for the selected subscription.
3. Backend verifies purchase token with Google Play and binds it to the correct game account.
4. Benefits are granted only after server verification.
5. Each billing period has one idempotent grant record.
6. Canceling auto-renew does not remove paid access before paid-through expiry unless platform state requires it.
7. Refunds, chargebacks, revocations, retries and out-of-order notifications are reconciled server-side.
8. Subscription expiry removes active subscription entitlements, not permanent goods separately purchased.

Consumable recurring benefits need explicit expiration/rollover policy. Do not grant from client callbacks alone. Never expose purchase tokens in client logs.

## 8. Revenue model and forecasting

Revenue must be modeled as separate lines, not one guessed “per player” figure:

- Gross subscription billings.
- Gross one-time in-app purchase billings.
- Gross ad revenue by banner, rewarded and interstitial format.
- Refunds, chargebacks, taxes, platform fees and ad-network deductions.
- Net receipts after deductions.
- Operating expenses (hosting, backend/database, moderation/support, music licensing, development, marketing, tools and other costs).
- Net operating contribution = net receipts − operating expenses. This is not automatically accounting profit or owner take-home.

### Player-count scenarios
Provide editable scenarios for 1,000 / 5,000 / 10,000 / 25,000 / 50,000 monthly active users, and daily active users separately. Do not assume all registered players are active or paying.

Required input variables:
- DAU, MAU, sessions per DAU, average session minutes.
- Banner eligible impressions per session and fill rate / realized eCPM.
- Rewarded-ad opt-in rate, completed views per opted-in user, fill rate / realized eCPM.
- Interstitial impressions per DAU and realized eCPM, after caps.
- Membership conversion rate by tier, monthly churn, renewals and refunds.
- One-time buyer conversion, average order value, purchase frequency and refunds.
- Platform fee, taxes, ad-network share and regional mix.
- Monthly operating expenses.

Calculation framework:
- Ad impressions = eligible opportunities × fill rate (subject to actual provider reporting).
- Ad gross revenue = (paid impressions ÷ 1,000) × realized eCPM, calculated separately per format and geography.
- Subscription gross billings = active paid subscriptions × localized monthly price.
- One-time gross billings = completed purchases × realized average order value.
- Net receipts = gross billings − refunds/chargebacks − taxes/withholding − platform fees − ad-network deductions, using actual statements and jurisdiction-specific accounting.
- Net operating contribution = net receipts − operating expenses.

Do not invent an eCPM, fill rate, conversion rate, churn rate, payer percentage, platform fee or revenue forecast and present it as fact. Dashboard must show low/base/high scenarios with every assumption visible and editable. Mark projections as estimates; replace assumptions with actual cohort and network data as soon as available. Never promise a guaranteed amount from 1,000 or 5,000 users.

## 9. Professional Owner Dashboard and Creator Studio

The owner needs a secure professional web dashboard, separate from the player-facing game UI, with role-based access.

### Executive overview
- DAU, WAU, MAU, new registrations, active/returning players and churn/lost customers.
- Session count, session length, retention cohorts and funnel conversion.
- Current live players and service health.
- Gross and net revenue by day/week/month and by stream.
- Membership counts by tier, MRR, renewals, cancellations, churn and refunds.
- Individual purchase volume, average order value, top SKUs and repeat buyers.
- Advertising impressions, fill, completion, eCPM and revenue by format, placement, geography and date.
- Expenses, cost categories, net operating contribution and cash/settlement reconciliation.
- Daily/weekly/monthly comparisons and exportable reports.

### Financial operations
- Reconcile Google Play orders, subscription states, refunds, chargebacks and payout statements.
- Reconcile ad-network reports and estimated vs finalized earnings.
- Ledger views for Hustle Money, Diamonds, Wings and Poker Chips separately.
- Track grants, sinks, package sales, adjustments and suspicious balance changes.
- Expense register for hosting, backend, licenses, moderation, support, marketing and other operating costs.
- Separate gross billings, platform proceeds, tax liabilities, payout timing and operating contribution. Do not label gross sales as profit.
- Audit log for every manual adjustment, refund action, promotion and financial export.

### Live game and player operations
- Search player account, inspect entitlements and transaction history under permission controls.
- Monitor concurrent players, crashes, errors, latency and service status.
- Configure daily rewards, recovery timers, bar offers and ad caps.
- Publish notices and approved events.
- Create win-back promotions for lapsed users with eligibility rules, budget limits, holdout tests and abuse controls.
- Configure membership benefits and individual SKU catalogue; preview/test before publish.
- Manage vehicles/car packs, clothing, jewelry, buildings, property and business content.
- Draft, review, approve, schedule and roll back catalogue/content changes.

### Creator Studio, permissions and safety
- Separate content-authoring workflow from financial reporting.
- Roles such as owner, finance, live-ops, content creator, support and read-only analyst.
- Two-person approval for high-risk financial changes, large grants, refunds, price changes and economy adjustments.
- Immutable audit log, MFA, least-privilege permissions, export logging and emergency disable controls.
- Never expose payment credentials, purchase tokens or unnecessary personal data in dashboard views.

## 10. QA and release gates
- Test each subscription tier purchase, renewal, cancellation, grace, refund and revoke.
- Test each one-time SKU, duplicate purchase, pending purchase, delayed receipt and restore.
- Test all four currencies independently; no accidental cross-wallet grant.
- Test daily reward idempotency across devices and reset boundaries.
- Test bar entry, energy recovery, chip recovery, wait display and reconnect behavior.
- Test rewarded-ad decline, completion, invalid callback, duplicate callback and capped reward.
- Test banner placement, safe areas, provider-compliant refresh and no gameplay obstruction.
- Test interstitial caps and all prohibited interruption contexts.
- Test owner dashboard role permissions, financial reconciliation, export, audit and rollback.
- Test low/base/high forecasts against synthetic inputs and label estimates clearly.

## 11. Decisions still open
- Final membership tier names, whether all six prices launch, and exact benefit matrix/quantities.
- Whether “poker money” is an alias for Poker Chips (working assumption) or a separate currency.
- Exact one-time package contents, prices, repeat limits and permanent/consumable classification.
- Daily reward calendar, reset time and reward amounts.
- Energy and Poker Chip recovery rates/caps; the suggested ~30-minute chip recovery is tentative.
- Whether the banner idea means a 10–15 second ad refresh; actual refresh must comply with the selected network's policy.
- Rewarded-ad offers and caps; interstitial frequency caps.
- Launch regions, age/consent policy, ad providers, Play billing configuration.
- Revenue forecast inputs and actual operating cost estimates.
- Dashboard deployment/authentication and finance roles.
