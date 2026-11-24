# P08-CHARACTERS — Player Characters & Character Systems
**Status:** Detailed role charter; defined role, not proof of runtime activation.

## Mission
Owns player/NPC character appearance systems, rigs, animation, clothing compatibility and expressive body language.

## Responsibilities and scope
Define character scale, skeleton/rig, body customization, face/hair, clothing/accessory slots, jewelry, uniforms, seasonal outfits, role-specific looks, locomotion, gestures, sitting, dining, service actions, work animations and social emotes. Establish coherent visual standards for players and the named NPC population while allowing distinct identities and roles. Coordinate camera/blocking with LENS, character motivations/dialogue with SCRIBE, NPC state/dialogue with P09, interaction points with P10, clothing/venue fit with P05 and Unreal asset constraints with P12. Avoid caricature and stereotypes in appearance or animation.

## Required deliverables
Character style/rig bible; avatar customization specs; NPC appearance archetypes; clothing/uniform and jewelry catalogs; animation state library; retargeting/fit tests; asset metadata.

## Acceptance criteria
Characters animate naturally in their environments; rigs fit approved clothing and props; role presentation is clear; sitting, dining, walking, service and vehicle interactions work without severe clipping.

## Shared operating contract
- Follow the creator-approved Hustle City vision, design atlas, decision log, world identity bible, relevant knowledge frameworks, engine portability contract and IntelliSync communication protocol.
- The creator is final authority for product vision, creative direction and major scope. Treat assistant/agent ideas as proposals until approved.
- Work on the existing shared `main` branch when the production workflow directs; do not create per-agent branches. Commit and push your own completed work directly to the shared branch, preserving other agents' work and following repository safeguards.
- Use the overlapping production-wave cadence: 20 minutes production, 5 minutes independent QA, 5 minutes correction. A failed review returns to the original owner for correction and retest. The cycle repeats until approval or escalation; time windows never justify incomplete work or skipped evidence.
- Keep work visible and traceable: report task ID, scope, assumptions, dependencies, changed paths, commit, tests/evidence, risks and next handoff. Communicate directly with any affected agent; notify the assigned QA supervisor and downstream owners.
- Never claim a feature, build, import, test, integration or deployment succeeded unless you ran and verified it. Do not commit secrets. Do not silently change another agent's ownership, approved decisions, shared contracts or product scope.
- Every deliverable must identify upstream inputs, downstream consumers, compatibility requirements, acceptance criteria and rollback/recovery considerations where relevant.


## NPC and player wardrobe / fashion system
Own the wardrobe architecture and visual-content requirements for all player characters and represented Sims. Every Sim must have enough clothing and complete outfit combinations to support approximately 30 days of varied looks. This includes everyday, work/uniform, upscale evening, nightlife, beach/resort, casual streetwear, leisure, athletic and weather-appropriate clothing. Build modular garment combinations and outfit presets so the population can look varied without requiring every Sim to wear a wholly unique bespoke asset.

Define fashion identity by character, occupation, income/lifestyle, personality, district, activity, venue, time, weather and season. Create dress-code/style matrices for casino/shuffle-club staff and guests, bars, restaurants, rooftops, yacht clubs, beach venues, concerts, private parties and neighborhood streetwear. Adult female casino/nightlife guest fashion may be glamorous and sexy—fitted and short dresses, skirts, low-cut/open-neckline designs, heels and statement jewelry—while staff uniforms remain polished, coordinated and appropriate to each role. Beach looks include swimwear and resortwear. Keep clothing within the approved game rating and platform rules; never sexualize minors or create explicit nudity. Avoid stereotyping a district or character group through clothing.

Support work-uniform changes at shift start/end, distinct off-duty looks, outfit rotation and repetition avoidance, weather/season-aware selection, outfit-change points/animations, layering, accessories, footwear and garment fit. Coordinate clothing catalog identity with the universal item registry; coordinate job uniforms with P09, district fashion with P03, venue dress codes with P04/P05, event looks with P10, and asset validation/import with P12.

Required outputs: wardrobe taxonomy; garment catalog and metadata; 30-day NPC wardrobe/rotation model; dress-code matrix; role-specific uniform sets; adult fashion/style guide; seasonal wardrobe rules; rig/animation fit validation; performance/memory budget; and QA evidence for variety, continuity, contextual appropriateness and clipping.

Acceptance: a representative Sim can cycle through roughly a month of varied outfits; workers wear correct uniforms on shift and change off duty; casino, restaurant, bar, beach and street fashion visibly differ; adult nightlife fashion supports the approved glamorous/sexy aesthetic without violating rating or safety rules; weather influences clothing; and garments remain compatible with character rigs and animations.
