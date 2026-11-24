# Hustle City — Advertising Revenue Model

**Status:** Planning model; not a revenue forecast or guarantee  
**Owner:** Creator  
**Planning target:** $10,000+ monthly gross revenue  
**Launch target:** May 2027 (target, not guarantee)  
**Scope:** Per-active-player advertising yield, session duration, and monthly scale

## 1. Creator-approved direction

- A persistent bottom banner remains visible for every player, including paid members. Membership does not remove the banner.
- The banner is a separate revenue stream from interstitial and rewarded advertising.
- The proposed scheduled-ad cadence is at 15, 30, 45, and 60 minutes of active play: up to four scheduled interstitial opportunities per active hour.
- A scheduled ad must wait for a safe transition. Never interrupt a poker hand, card trade, conversation, key interaction, or other critical activity.
- The creator is considering two ad presentation experiences: a short 10–15-second ad followed by a close option, or a 30-second ad with a close option. Exact close timing and available formats depend on the selected ad network and the creative served.
- Rewarded ads remain a separate, voluntary format with a clearly disclosed in-game reward. They are not counted in the scheduled-interstitial calculations below.
- Contextual bar, card-trading, and casino placements remain under design. They must not stack on top of the scheduled-ad cap or turn every interaction into an ad.

## 2. Session schedule

The scheduled opportunity count is four per completed active hour. A partial hour earns only the opportunities whose time points are reached.

| Active session duration | Scheduled opportunities |
|---:|---:|
| 15 minutes | 1 |
| 30 minutes | 2 |
| 45 minutes | 3 |
| 60 minutes | 4 |
| 90 minutes | 6 |
| 2 hours | 8 |
| 3 hours | 12 |
| 4 hours | 16 |
| 5 hours | 20 |

These are opportunities, not guaranteed paid impressions. If an ad is unavailable, the player is busy, or a safe transition does not occur, skip that opportunity; do not queue missed ads or show them back-to-back. Count active foreground play, not idle/background time.

## 3. Benchmark input and calculation method

A 2025 Appodeal report chart gives approximate US Android averages of **$12.30 interstitial eCPM** and **$0.60 banner eCPM**. These are historical market benchmarks, not a promise of Hustle City's rates. Actual results vary by country, device/platform, audience, ad network/mediation, fill, viewability, season, and policy compliance.

Formula:

- Interstitial revenue = (paid interstitial impressions ÷ 1,000) × realized interstitial eCPM.
- Banner revenue = (paid banner impressions ÷ 1,000) × realized banner eCPM.
- Total ad revenue = interstitial + banner + separately measured rewarded ads + any approved contextual formats.

For the simple session table below, use four **served and monetized** interstitial impressions per active hour and the illustrative $12.30 US Android eCPM:

**Illustrative gross interstitial yield = 4 × $12.30 ÷ 1,000 = $0.0492 per active player-hour.**

This is a gross illustration before platform fees, taxes, invalid-traffic adjustments, operating costs, and any other deductions. If only a fraction of scheduled opportunities become paid impressions, multiply the result by that realized served-impression fraction. For example, at 75% realization, multiply by 0.75. Do not treat an ad opportunity, a loaded ad, or a closeable ad as a paid impression unless the network records a billable impression.

## 4. Per-player session yield — interstitials only

| Active play in one session | Opportunities | Illustrative gross yield at 100% paid delivery |
|---:|---:|---:|
| 1 hour | 4 | $0.0492 |
| 2 hours | 8 | $0.0984 |
| 3 hours | 12 | $0.1476 |
| 4 hours | 16 | $0.1968 |
| 5 hours | 20 | $0.2460 |

### Monthly illustration by average daily active play

Assumes 30 active days per month, the same active hours each day, four paid interstitial impressions per hour, and the illustrative $12.30 eCPM. This is not a forecast.

| Average active play per day | Paid interstitial impressions/month | Gross interstitial revenue/player/month |
|---:|---:|---:|
| 1 hour/day | 120 | $1.476 |
| 2 hours/day | 240 | $2.952 |
| 3 hours/day | 360 | $4.428 |
| 4 hours/day | 480 | $5.904 |
| 5 hours/day | 600 | $7.380 |

At a 75% paid-delivery realization rate, multiply each monthly amount by 0.75. Example: 3 hours/day becomes approximately $3.32 gross interstitial revenue per active player per 30-day month.

## 5. What this means for the $10,000/month target

At the illustrative $12.30 eCPM, four paid interstitial impressions per active hour produce about $0.0492 per active player-hour. Interstitials alone would therefore require roughly **203,252 active player-hours per month** to generate $10,000 gross before deductions.

Illustrative scale examples:

| Average active hours per player per day | Approx. monthly active players needed for $10,000 gross interstitial revenue |
|---:|---:|
| 1 hour/day | 6,776 |
| 2 hours/day | 3,388 |
| 3 hours/day | 2,259 |
| 4 hours/day | 1,694 |
| 5 hours/day | 1,356 |

These are arithmetic scenarios, not audience forecasts. They assume every scheduled opportunity becomes a paid impression at the benchmark eCPM, all listed players are active every day for 30 days, and no deductions. Real requirements will be higher if delivery, fill, retention, or realized eCPM is lower. The model must be recalculated with actual ad-network reporting after launch.

## 6. Persistent banner — separate calculation

The bottom banner is always part of the experience, including for paid members. Do not assume one impression per minute or any refresh rate until the selected provider, platform rules, and placement implementation are confirmed.

Track:
- Banner requests, served impressions, viewable impressions, fill rate, and realized eCPM.
- Actual visible time and refresh events while the app is foregrounded.
- Banner revenue per daily active user and per monthly active user.

Formula: monthly banner revenue per player = (that player's paid banner impressions in the month ÷ 1,000) × realized banner eCPM.

The $0.60 US Android banner eCPM in the cited 2025 report is only an illustrative benchmark. The banner is not removed by membership.

## 7. Short versus 30-second ad test

Test the creator's two candidate experiences as separate ad placements/creative experiences, subject to provider capabilities and policy:

- Variant A: 10–15 seconds before a close option is available, if the served format supports it.
- Variant B: 30 seconds with a close option, if the served format supports it.

Measure realized eCPM, paid impressions per eligible opportunity, completion/close behavior, session length, next-day and 7-day retention, complaints, accidental clicks, and revenue per active user. A longer ad does **not** automatically pay more: pricing is based on the ad auction and billable event, not simply the number of seconds the player watches. Do not force a 30-second watch where the network's format or policy requires a different experience.

## 8. Revenue streams to model separately

1. Persistent bottom banner (all players, including members).
2. Scheduled interstitial opportunities (up to four per active hour, safely deferred or skipped).
3. Voluntary rewarded ads (separate opt-in; record starts, completions, rewards, and revenue).
4. Approved contextual placements (bar, card trading, casino) only after separate frequency and UX review; must not silently add extra full-screen interruptions.
5. Membership revenue (separate from ad revenue; membership does not remove the banner).
6. Optional purchases (separate from ad revenue).

Do not add revenue streams together until each has a measured or explicitly labeled assumed input. Report gross ad revenue, net proceeds after store/platform/network fees, and operating profit separately.

## 9. Measurement and dashboard requirements

For every session and player cohort, measure:
- Active foreground minutes and session duration buckets (15, 30, 45, 60, 90, 120, 180+ minutes).
- Scheduled opportunities reached, deferred, skipped, requested, loaded, shown, billable impressions, and failed requests.
- Realized eCPM and revenue by format, country, platform, placement, and network.
- Banner impressions and viewability separately from interstitials.
- Rewarded-ad opt-in, start, completion, reward grant, and revenue.
- Revenue per DAU, revenue per MAU, ARPDAU, retention, session frequency, and ad-related complaints.
- Membership conversion and purchase revenue separately.

Use privacy-conscious analytics and applicable consent, child-safety, advertising, store, and regional requirements. Never optimize revenue by creating accidental clicks, deceptive close controls, or interruptions during core play.

## 10. Policy and implementation checks

Google AdMob guidance says interstitials belong at natural transition points, warns against surprising or excessive interruptions, and notes that close timing can vary by format and demand source. Google also provides frequency caps. The proposed 15-minute cadence is a product hypothesis to test, not a guarantee of provider approval. Confirm current network rules and the exact game implementation before launch.

## 11. Sources

- Appodeal, *The Latest eCPM Report 2025* (US Android chart; approximate banner $0.60, interstitial $12.30): https://appodeal.com/wp-content/uploads/2025/03/Appodeal-The-Latest-eCPM-Report-2025.pdf
- Google AdMob, *Interstitial ad guidance*: https://support.google.com/admob/answer/6066980
- Google AdMob, *Disallowed interstitial implementations*: https://support.google.com/admob/answer/6201362
- Google AdMob, *Set frequency caps for apps or ad units*: https://support.google.com/admob/answer/6244508

---
**Open decisions:** exact short/long ad format and close timing; realized eCPM assumptions by country and platform; banner refresh/viewability rules; final frequency cap; contextual placements; rewarded-ad limits. Keep these unresolved until tested and approved.
