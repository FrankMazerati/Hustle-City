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

## 3. Benchmark inputs and calculation method

For an illustrative planning scenario, this document uses:
- **Interstitial eCPM:** $12.30 per 1,000 paid impressions.
- **Banner eCPM:** $0.60 per 1,000 paid impressions.
- **Banner refresh assumption:** one new paid banner impression per 60 seconds while the banner is visible and the app is active.
- **Interstitial delivery assumption:** all four scheduled opportunities per active hour become paid impressions.

These are historical/illustrative market inputs, not Hustle City forecasts or guaranteed rates. eCPM varies by geography, platform, audience, ad network/mediation, fill, viewability, season, and policy compliance. The $0.60 banner figure is a historical US Android benchmark cited in industry reporting; actual banner eCPM can be materially lower or higher. The 60-second refresh is a modeling assumption, not an approved implementation setting.

Google AdMob says its optimized banner refresh is recommended and permits custom refresh settings between 30 and 150 seconds. Google also notes that refresh occurs only while the banner is visible. The final setting must follow the chosen provider's current rules and measured UX/performance.

Formulas:
- Interstitial revenue = (paid interstitial impressions ÷ 1,000) × realized interstitial eCPM.
- Banner revenue = (paid banner impressions ÷ 1,000) × realized banner eCPM.
- Combined scheduled + banner revenue = interstitial revenue + banner revenue.
- Total advertising revenue = combined scheduled + banner revenue + separately measured rewarded ads + any approved contextual formats.

At the assumptions above:
- Interstitial: 4 × $12.30 ÷ 1,000 = **$0.0492 per active player-hour**.
- Banner: 60 × $0.60 ÷ 1,000 = **$0.0360 per active player-hour**.
- Combined: $0.0492 + $0.0360 = **$0.0852 per active player-hour**.

A paid impression must be recorded as billable by the ad network. An opportunity, request, loaded ad, or closeable ad is not automatically a paid impression. If only a fraction of scheduled opportunities or banner refreshes becomes paid impressions, multiply the relevant revenue by its actual paid-impression realization rate. These are gross amounts before platform fees, taxes, invalid-traffic adjustments, operating costs, and other deductions.

## 4. Combined per-player yield for one continuous session

Assumes the player remains active, the bottom banner remains visible, it refreshes once per minute, and all scheduled interstitial opportunities become paid impressions.

| Active session | Interstitial ads | Banner impressions (assumed) | Interstitial revenue | Banner revenue | Combined gross revenue |
|---:|---:|---:|---:|---:|---:|
| 1 hour | 4 | 60 | $0.0492 | $0.0360 | **$0.0852** |
| 2 hours | 8 | 120 | $0.0984 | $0.0720 | **$0.1704** |
| 3 hours | 12 | 180 | $0.1476 | $0.1080 | **$0.2556** |
| 4 hours | 16 | 240 | $0.1968 | $0.1440 | **$0.3408** |

## 5. Combined monthly yield if the player plays every day

Assumes 30 active days per month with the same daily play duration, 60-second banner refresh, $0.60 banner eCPM, four paid interstitial impressions per active hour, and $12.30 interstitial eCPM.

| Average active play per day | Interstitial revenue/month | Banner revenue/month | Combined gross ads/player/month |
|---:|---:|---:|---:|
| 1 hour/day | $1.476 | $1.080 | **$2.556** |
| 2 hours/day | $2.952 | $2.160 | **$5.112** |
| 3 hours/day | $4.428 | $3.240 | **$7.668** |
| 4 hours/day | $5.904 | $4.320 | **$10.224** |

This table is an illustrative upper-case calculation under the stated assumptions, not a forecast. If paid delivery is 75% for both formats, multiply each combined amount by 0.75. For example, the 3-hour/day case becomes about **$5.75 gross per player per month**, before deductions. Banner and interstitial delivery rates should ultimately be measured separately.

## 6. What this means for the $10,000/month target

Under the 100%-paid-delivery assumptions in section 5, approximate active players required to generate $10,000/month in combined banner + interstitial gross ad revenue:

| Average active hours per player per day | Combined gross per player/month | Approx. active players for $10,000 gross/month |
|---:|---:|---:|
| 1 hour/day | $2.556 | 3,913 |
| 2 hours/day | $5.112 | 1,956 |
| 3 hours/day | $7.668 | 1,304 |
| 4 hours/day | $10.224 | 978 |

These are arithmetic scenarios, not audience forecasts. They assume every listed player is active every day for 30 days and every assumed ad impression is paid. At 75% paid delivery for both formats, the player counts would be approximately one-third higher. Real requirements may also be higher if realized eCPM, banner visibility, fill, retention, or daily active participation is lower. Recalculate using actual network reporting after launch.

## 7. Persistent banner implementation and measurement

The bottom banner is always part of the experience, including for paid members. It is not removed by membership.

Google AdMob's automatic banner refresh settings allow a custom interval of 30–150 seconds, while recommending its optimized rate. Refresh is only expected while the banner is visible. Therefore:
- The 60-second interval in this model is a scenario input, not a locked technical requirement.
- Test the provider-optimized rate against a 60-second custom rate if permitted and available.
- Do not generate refresh requests while the game is backgrounded or the banner is not visible.
- Keep the banner in a fixed, non-interactive gameplay-safe area; it must not cover controls or create accidental clicks.
- Track requests, served impressions, viewable impressions, fill rate, realized eCPM, visible time, refresh events, and banner revenue per DAU/MAU.

## 8. Short versus 30-second interstitial test

Test the creator's two candidate experiences as separate ad placements/creative experiences, subject to provider capabilities and policy:
- Variant A: 10–15 seconds before a close option is available, if the served format supports it.
- Variant B: 30 seconds with a close option, if the served format supports it.

Measure realized eCPM, paid impressions per eligible opportunity, completion/close behavior, session length, next-day and 7-day retention, complaints, accidental clicks, and revenue per active user. A longer ad does **not** automatically pay more: pricing is based on the ad auction and billable event, not simply the number of seconds the player watches. Do not force a 30-second watch where the network's format or policy requires a different experience.

## 9. Revenue streams to model separately

1. Persistent bottom banner (all players, including members).
2. Scheduled interstitial opportunities (up to four per active hour, safely deferred or skipped).
3. Voluntary rewarded ads (separate opt-in; record starts, completions, rewards, and revenue).
4. Approved contextual placements (bar, card trading, casino) only after separate frequency and UX review; must not silently add extra full-screen interruptions.
5. Membership revenue (separate from ad revenue; membership does not remove the banner).
6. Optional purchases (separate from ad revenue).

Do not add revenue streams together until each has a measured or explicitly labeled assumed input. Report gross ad revenue, net proceeds after store/platform/network fees, and operating profit separately.

## 10. Measurement and dashboard requirements

For every session and player cohort, measure:
- Active foreground minutes and session duration buckets (15, 30, 45, 60, 90, 120, 180+ minutes).
- Scheduled opportunities reached, deferred, skipped, requested, loaded, shown, billable impressions, and failed requests.
- Realized eCPM and revenue by format, country, platform, placement, and network.
- Banner impressions and viewability separately from interstitials.
- Rewarded-ad opt-in, start, completion, reward grant, and revenue.
- Revenue per DAU, revenue per MAU, ARPDAU, retention, session frequency, and ad-related complaints.
- Membership conversion and purchase revenue separately.

Use privacy-conscious analytics and applicable consent, child-safety, advertising, store, and regional requirements. Never optimize revenue by creating accidental clicks, deceptive close controls, or interruptions during core play.

## 11. Policy and implementation checks

Google AdMob guidance says interstitials belong at natural transition points, warns against surprising or excessive interruptions, and provides frequency caps. The proposed 15-minute cadence is a product hypothesis to test, not a guarantee of provider approval. Confirm current network rules and exact game implementation before launch.

## 12. Sources

- Appodeal, *The Latest eCPM Report 2025*: https://appodeal.com/wp-content/uploads/2025/03/Appodeal-The-Latest-eCPM-Report-2025.pdf
- Historical US Android banner eCPM reference ($0.60): https://www.blog.udonis.co/mobile-marketing/mobile-apps/ecpms
- Google AdMob, *Use automatic refresh for your banner ads*: https://support.google.com/admob/answer/3245199
- Google AdMob, *Interstitial ad guidance*: https://support.google.com/admob/answer/6066980
- Google AdMob, *Disallowed interstitial implementations*: https://support.google.com/admob/answer/6201362
- Google AdMob, *Set frequency caps for apps or ad units*: https://support.google.com/admob/answer/6244508

---
**Open decisions:** exact short/long ad format and close timing; realized eCPM assumptions by country and platform; banner refresh/viewability rules; final frequency cap; contextual placements; rewarded-ad limits. Keep these unresolved until tested and approved.
