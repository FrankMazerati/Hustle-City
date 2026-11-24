# Hustle City — Player Commerce and Customization

## 1. Player-facing store
One discoverable store/catalogue can organize clothing, shoes, accessories, card packs, vehicles or vehicle upgrades, apartment/property upgrades, business upgrades and approved currency packages. Each item must identify whether it is earned, bought with Hustle Money, bought with Diamonds, unlocked by cards, or purchased through platform billing.

## 2. Clothing and accessories
Player flow: browse category → preview on current character → inspect details/fit/compatibility → select color/variant → purchase or claim → add to wardrobe → equip/unequip → save outfit. Support clothing, shoes, jewelry, bags, eyewear, hats, watches and other approved accessories as catalogued assets. Brand names/logos require rights review. Avoid selling an item already owned without clearly labeling duplicates or gift behavior.

## 3. Vehicles
Vehicle catalogue and garage distinguish ownership, access, cosmetics, performance/functional upgrade and travel service entitlement. Because automated destination travel is the preferred core experience, vehicle upgrades must describe actual supported effects (appearance, capacity, comfort, convoy presentation or approved travel tier) and must not imply manual-driving performance if that mechanic is not implemented. Upgrade purchase validates vehicle ownership, compatibility, cost and resulting stat cap.

## 4. Apartments and properties
Show current property, available upgrades, prerequisites, cost, visual preview and functional effect. Potential upgrade categories include furnishing, decor, storage, garage, guest capacity and access options, only where supported by that property. Apartment upgrades do not automatically grant building or neighborhood ownership.

## 5. Businesses
Business upgrade catalogue may include appearance, interior, service offerings, staffing, inventory capacity, operating efficiency and event capabilities. Every upgrade must map to implemented server-side effects and be visible in owner dashboard. No unbalanced passive income promises.

## 6. Purchase contract
For in-game currency purchases, server validates price and balance, locks relevant inventory/ownership row, debits wallet and grants entitlement atomically. For Google Play purchases, use verified receipts as defined in ECONOMY_AND_MONETIZATION.md. Failed grants are recoverable by idempotency key. Display ownership and purchase history.

## 7. QA
Test item compatibility, already-owned items, simultaneous purchase, insufficient balance, currency mismatch, stale catalogue, upgrade prerequisites, vehicle mismatch, property access rights, business manager permissions, receipt pending/refund/revoke and client tampering.
