# Hustle City — Social Network, Sharing and Referrals

## 1. Product intent
The social layer should feel live, location-aware, lively and “hood” in voice without sacrificing privacy or safety. It should make it easy to see what's happening, react, talk, invite friends and bring new players into Hustle City.

## 2. Feed surfaces
- **World News Feed:** broad city activity and official updates.
- **Friends Feed:** activity shared by friends under their privacy settings.
- **Environment News Feed:** live, venue- or location-specific activity with local personality.
- **Crew Feed:** crew announcements, gatherings, achievements and invitations.
- **Business/Venue Feed:** approved posts, events and activity tied to an owned or public venue.
- **Official Admin Feed:** moderation notices, maintenance, announcements and live operations.

Possible feed events already discussed: player purchases, arrivals, poker wins, reactions, public table chat, private chat indicators where appropriate, friend requests and crew invitations. Private messages must never be copied into public feeds.

## 3. Posts and reactions
Player post fields: post_id, author_id, content, optional approved media, visibility, optional venue/event reference, created_at, moderation state and interaction counts. Reactions and comments are permission-controlled. Support reporting, blocking, muting, deletion/edit policy and rate limits. Avoid automatically revealing exact real-time location; use venue presence only when the player opts in or the activity is inherently public and approved.

## 4. Chat and relationships
Support private 1:1 chat, public table chat, nearby chat where enabled, crew chat, group/travel chat and event/venue chat. Friends, friend requests, crew invitations, business invitations and event invitations are distinct invitation types. Include accept/decline, expiry, block/report and notification preferences.

## 5. External social sharing
Provide share actions for supported installed apps and OS share sheet targets, including social networks and messaging. Previously discussed examples include Facebook, Instagram, TikTok, Snapchat, X, WhatsApp, Messenger, text and email; availability depends on platform/app installation and current API policies.

Canonical share-message example:
> I just joined Hustle City. Join me over here. Here's my link: [personal invite link]

The link should resolve to an install/open flow, carry a non-guessable referral attribution token, and avoid exposing private account data. Support copy link, native share sheet and approved deep links. Do not promise direct posting to every social platform where API access is unavailable.

## 6. Referrals
Referral rewards were discussed as potentially including credits, Diamonds, Poker Chips and Hustle Money. Launch bonuses may start larger and scale down as the player base grows. Exact amounts and milestones are unresolved.

Referral service must define qualifying event (for example, install alone vs verified account vs completed onboarding vs meaningful play), attribution window, one-account/one-referrer rules, fraud detection, reward caps, reversals for fraud/refunds, campaign version and transparent disclosure. Avoid self-referrals, device farms, collusion and spam. Reward only after the configured qualifying event.

## 7. Location and privacy controls
Players choose visibility for online status, current venue, travel status, map presence, crew emblem/name display, feed activity and invitation reach. Provide block, mute, report, hide activity and invitation controls. A player who disables presence must not be exposed through map, convoy or feed surfaces. Use approximate venue-level presence where appropriate; never leak precise real-world location.

## 8. Notification system
Notifications include friend requests, accepted invitations, crew activity, event reminders/changes, trade offers, trade completion, card set progress, business/venue notices and moderation/system messages. Each category has independent settings, quiet hours and delivery preferences.

## 9. QA
Test visibility combinations, blocked users, private accounts, event-only posts, external share token attribution, expired/abused referral links, duplicate referral rewards, deleted posts, message privacy, venue feeds and opt-out of map presence.
