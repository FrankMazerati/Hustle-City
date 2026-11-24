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

## 5. In-game friends and card-trading social layer
- Friend discovery, friend requests, accept/decline/removal, block/report and privacy settings are first-class in-game systems.
- Players can open another eligible player's public trading profile, subject to inventory visibility settings, and see only the card details that player has chosen to share.
- The in-game Card Finder matches missing cards against tradeable duplicates and supports wish lists, reciprocal matches, trade requests and notifications.
- The trade conversation, counteroffers, approvals, receipts and history remain inside Hustle City. No external app or group is required to find or complete a trade.
- Friend status is not consent to reveal private inventory, messages or location. Blocks and privacy settings override discovery.
- Refer to [Cards, Packs and Trading](CARDS_PACKS_AND_TRADING.md) for the authoritative card-exchange protocol.

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


## 7.1 Universal gameplay shareability requirement
**Creator-approved direction:** social sharing and player acquisition are designed into the entire gameplay experience, not limited to City Keys or a few major milestones. Any meaningful player action or accomplishment should be eligible to produce personalized, shareable content. Examples include character creation, first car, apartment/property acquisition, clothing and outfit showcases, card discoveries and collection completion, poker/activity milestones, yachts, businesses, clubs, venues, City Keys and profile progression. This catalogue is extensible; every new gameplay feature must consider shareability.

For every new or materially changed feature, its design/acceptance checklist must answer:
- Which authoritative gameplay events can produce shareable moments?
- What artifact is generated (image, profile card, clip/animation or share link)?
- Which player-controlled privacy choices apply?
- Which supported destinations and fallback share-sheet paths are available?
- Is a share reward configured, or explicitly not applicable? What prevents duplicate claims?
- Can the artifact/link attribute a genuinely new player to the inviter?
- What QA covers content correctness, privacy, accessibility, platform behavior, abuse and analytics?

A share artifact is a promotional representation, not proof of ownership by itself. Generate it from confirmed server state. Never expose unreleased content, hidden card details, private properties, private messages, account identifiers or exact player location.

## 7.2 Universal social-growth architecture
Use reusable services with stable IDs and auditable state:
1. **Gameplay Event Publisher:** emits approved meaningful events from authoritative gameplay services, not client claims.
2. **Share Eligibility and Template Service:** selects a versioned template, permitted player details and destination-safe format.
3. **Share Artifact Generator:** creates personalized branded images and, where supported, short animations/video or profile showcases.
4. **Share Orchestrator:** offers Share, Save, Copy Link and available OS share-sheet targets. Follow current platform APIs and policies; do not promise unsupported direct publishing.
5. **Share Proof and Verification Service:** records and evaluates proof submissions.
6. **Reward Eligibility and Ledger Service:** grants configured rewards idempotently with audit records.
7. **Referral Attribution and Qualification Service:** attributes new-player registrations and qualifying milestones.
8. **Analytics and Abuse Detection:** measures the funnel while respecting privacy and retention controls.

Do not build a separate one-off sharing/reward mechanism for every feature.

## 8. Share records, proof submission and verification
The creator approved a proof-based sharing-reward direction: after sharing an eligible artifact, a player may return to Hustle City and submit a screenshot/photo as evidence. A screenshot is evidence to review, not cryptographic or conclusive proof that a post was published or remains public.

Minimum records:
- **ShareEvent:** share_event_id, player_id, source_gameplay_event_id, artifact_id, template_version, created_at, eligible_destinations, status.
- **ShareArtifact:** artifact_id, owner_player_id, artifact_type, content_version, safe_payload_reference, generated_at, expiration/retention metadata.
- **ShareProofSubmission:** proof_id, share_event_id, player_id, claimed_platform, uploaded_media_reference, submitted_at, review_status and decision metadata.
- **ShareVerificationDecision:** decision_id, proof_id, verification_method, confidence/outcome, policy_version, decided_at and audit metadata.
- **ShareRewardClaim:** claim_id, player_id, share_event_id, reward_config_id, status, ledger_transaction_id and created_at.
- **ReferralAttribution:** referral_id, inviter_player_id, opaque_token_id, referred_account_id, attribution_timestamp, qualifying_milestone and campaign_version.

### 8.1 Player flow
1. An authoritative gameplay event makes a share opportunity available.
2. Hustle City generates a unique share event and personalized artifact.
3. Player chooses to share, save, copy or dismiss. Sharing is optional.
4. If the reward policy requires proof, the player returns and uploads a screenshot or other permitted evidence.
5. The service validates file type/size, associates proof with the correct player and share event, and checks duplicates/fraud signals.
6. Automated review may approve, reject or route ambiguous cases to manual review. Show pending, approved, rejected and appeal/retry states clearly.
7. Only an approved decision can trigger the configured reward. The server writes one idempotent ledger transaction.
8. Referral rewards are evaluated separately when a referred new player completes the configured qualifying milestone.

### 8.2 Verification levels and honest claims
- **Level 1 — Proof received:** screenshot uploaded and basic file/account/event checks passed. This is not confirmation that a post is authentic or public.
- **Level 2 — Evidence reviewed:** screenshot is consistent with the expected artifact/platform and passes configured checks. This supports an evidence-based reward decision but does not guarantee the post remains live.
- **Level 3 — Referral qualified:** a genuinely new account is attributed to the inviter and completes the configured qualifying milestone. This is separate from proof of a social post.

Where an authorized platform integration is available and permitted, it may provide stronger confirmation. Platform APIs and policies vary. Do not scrape, bypass access controls, collect social passwords or claim capabilities an integration does not provide. Screenshot-only review must be described as evidence review, not definitive platform verification.

## 9. Share rewards and referral rewards
Sharing rewards and referral rewards are distinct:
- **Share reward:** configured incentive for an eligible share event after its required verification path passes.
- **Referral reward:** configured incentive for bringing a genuinely new player who completes a defined qualifying milestone.

All reward amounts, currency types, caps, campaign durations, qualifying milestones and launch incentives remain **TBD / creator approval required**. Do not invent values or assume every share event must pay a reward.

Controls:
- One share event can produce at most one successful share reward claim under its configured policy.
- Retries, duplicate requests and reconnects are idempotent.
- A proof file/artifact cannot be reused for multiple unrelated share events.
- Re-sharing the same event does not create repeat rewards unless a future campaign explicitly configures a separate bounded incentive.
- Referral rewards are issued only after server-verified qualifying milestones, not merely a link click or install attempt.
- Grants and reversals are recorded in the authoritative ledger with campaign/rule version.
- Disclose terms clearly. Never require public posting or referrals for core progression.

## 10. Fraud prevention, moderation and privacy
Detect and rate-limit:
- Reused screenshots, perceptually similar images and duplicate proof hashes.
- Proofs submitted by the wrong account or associated with another player's share event.
- Edited, fabricated, cropped or inconsistent evidence; route ambiguous cases to human review.
- Multiple claims for one share event, replayed requests and concurrent reward attempts.
- Self-referrals, duplicate accounts, device/account farms, collusion, bot activity and referral rings.
- Artificial engagement, spam and attempts to expose personal information.
- Deleted/private posts where a policy requires visibility, recognizing screenshot evidence cannot prove continuing visibility.

Use proportionate, privacy-preserving risk signals; no single device fingerprint is conclusive. Provide reason codes, appeal/review paths and support audit trails. Define upload type/size limits, malware scanning, restricted media access, retention/deletion periods and role-based staff access. Do not retain screenshots indefinitely by default.

Players control which profile details appear in generated content. Default to safe content. Never include email, phone, legal name, account IDs, private messages, hidden inventory or precise real-world location.

## 11. Referral attribution
Referral links use non-guessable opaque attribution tokens and resolve to install/open flows without exposing private account data. The service must define qualifying event (verified account, onboarding completion or meaningful play), attribution window, one-account/one-referrer rules, fraud detection, reward caps, reversals, campaign version and disclosure. Exact milestones and payouts remain unresolved. Do not reward link clicks alone.

## 12. Analytics and growth measurement
Measure:
- Eligible gameplay events and artifact generation.
- Share sheet opened, destination selected where observable, artifact saved/copied and share flow completed where the platform reports it.
- Proof submission, review latency, approval/rejection rates and appeals.
- Reward cost, duplicate claims, fraud flags and reversals.
- Referral clicks, attributed registrations, onboarding completion, qualifying milestones, retention and cost per qualified player.
- Conversion by artifact type/template and gameplay feature.

Do not infer a successful public post merely because the OS share sheet opened or the player returned to the game. Distinguish observed events from player-reported actions and platform-confirmed signals.

## 13. Expanded QA and acceptance
- Any meaningful gameplay event configured as shareable generates the correct personalized artifact from confirmed server state.
- A new feature cannot be marked social-sharing complete until its shareability checklist is reviewed.
- Player can decline sharing and continue gameplay without penalty.
- Artifact preview/output obey profile visibility and privacy settings.
- Share targets fall back gracefully to OS share sheet, save and copy-link options.
- Share IDs are unique, opaque and bound to the correct player, source event and artifact.
- Proof upload rejects unsupported files and handles interruption safely.
- Reused/altered/wrong-account proof is flagged; ambiguous proof can be reviewed without false certainty.
- One event cannot issue duplicate rewards under retries, reconnects or concurrent submissions.
- Pending/rejected/approved states and appeal paths are clear.
- Referral attribution survives install/open flows where supported and cannot be overwritten by arbitrary client claims.
- Self-referrals, duplicate accounts, referral rings and repeated reward attempts are tested.
- Deleted/private posts are not represented as continuously verified based on an old screenshot.
- No social password collection, unauthorized scraping or platform-policy bypass.
- Private messages, hidden inventory, private profile data and exact real-world location never leak into artifacts or feeds.
- Reward ledger, proof decisions, referral qualification and moderation actions are auditable.

## 14. Not ready for production until approved
Exact share-reward amounts, reward currencies, claim limits, referral milestones, attribution window, campaigns, proof-retention period, manual-review staffing/SLA, platform integrations and supported platform-specific verification methods remain unresolved. These require creator approval, platform-policy review, privacy/security review and implementation testing.
