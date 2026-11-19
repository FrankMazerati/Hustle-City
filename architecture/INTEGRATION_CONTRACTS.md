# Cross-System Integration Contracts

## Coordinate and scale
Before production asset approval, define world units, origin, forward axis, grid/block dimensions and vertical conventions. Every spatial asset declares origin, scale, collision bounds, navigation footprint and attachment anchors. No agent may invent incompatible axes, units or naming.

## Character
Declare rig/skeleton version, height range, collision capsule, movement modes, interaction reach, animation states, clothing slots and safe-recovery hooks.

## Buildings
Declare exterior footprint, floors, interior scenes, navigation links, collision geometry, doors, accessibility, interaction anchors, lighting sockets, streaming bounds and interactive/decorative status.

## Vehicles
Declare dimensions, collision volumes, driver/passenger seats, entry/exit anchors, door states, capacity, automated route interface, safe stop/brake states and camera sockets.

## Transit
Represent journeys as request → validate destination → reserve capacity → approach → board → depart → travel → arrive → disembark → complete. Failures enter a safe recovery state.

## Interactions
Each object declares stable ID, interaction type, range, preconditions, authoritative owner, feedback, cancellation, failure recovery and accessibility fallback.

## NPC truth
NPCs report events, venue status, transit and directions only from authoritative live-state queries. If unavailable, say they do not know rather than invent information.

## Economy and networking
Hustle Money, Diamonds and Poker Chips are separate balances. Transactions are server-authoritative, auditable and idempotent. Client code cannot authorize balances, inventory, ownership or competitive outcomes.

## Asset metadata
Every asset declares ID, owner, version, intended use, license/provenance, dimensions, dependencies, target budgets and validation state. Concept art is not a production asset by default.
