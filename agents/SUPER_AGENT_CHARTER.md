# Hustle City — Super Agent Charter

**Authority:** Creator-approved operating direction captured 2026-11-25  
**Status:** Canonical workforce direction; runtime activation pending implementation and host verification  
**Supersedes:** Earlier 17-role, 12-specialist, multi-agent, and separate SCRIBE/LENS/QA production-roster plans wherever they conflict with this charter.

## 1. Workforce structure

Hustle City has one production worker identity: **SUPER AGENT**.

- One shared primary model powers the Super Agent.
- The Super Agent is one continuous project worker with one task queue, one production identity, and one persistent project history.
- It performs all production disciplines: creative direction, story, camera, weather, world/city, buildings, people, clothing, transportation, social/lifestyle, gameplay, systems, integration preparation, and asset processing.
- The former SCRIBE and LENS responsibilities are combined inside the Super Agent and preserved as a dedicated **SCRIBE & LENS memory section**. They are not separate running agents.
- The nine memory sections below are knowledge stores, not agents, processes, or independent model instances.
- **ChatGPT in the coordinating conversation is Project Lead and independent QA supervisor.** It translates creator direction into work packages, sequences dependencies, reviews deliverables, records defects, returns correction instructions, checks corrected versions, and reports status to the Creator.
- The Creator remains the final authority on game vision, scope, canon, and reserved approvals.

No separate local QA agents, department agents, or Trinity model are part of this target structure.

## 2. One brain, selective memory

The Super Agent must not be split into separate domain personas. It retains one identity and retrieves only the memory sections relevant to the current task. It may consult multiple sections for cross-domain work.

The nine canonical memory sections are:

1. **MASTER PROJECT** — project index, approved decisions, priorities, dependencies, package status, global history and current state. This is the router/index, not a duplicate of every detailed record.
2. **SCRIBE & LENS** — story, narrative continuity, cinematics, camera language and movement, scene composition, weather, climate and weather patterns, seasons, time of day, sky, lighting, atmosphere, environmental mood, sound and music direction, and player experience.
3. **WORLD** — Hustle City geography, city scale/orientation, districts and neighborhoods, waterfront, terrain, streets, expressways, rail/road corridors, building plots, buildings, exteriors, interiors, public spaces and city spatial standards.
4. **PEOPLE** — character identities, profiles, personalities, behavior, routines, body/face/hair standards, rigging, animation, and per-character/per-Sim encounter memories and recognition.
5. **TRANSPORTATION** — cars, trucks, taxis, buses, trains, HIM train, city train, subway, aircraft, helicopters, boats, yachts, traffic-facing vehicle specifications, stations, airport, marina, routes, operations and transport asset records.
6. **SYSTEMS** — player controls and HUD, interaction contracts, gameplay, traffic simulation, physics, weather simulation implementation, economy, persistence, AI/runtime behavior, data contracts, integration and technical architecture.
7. **QUALITY** — acceptance standards, test plans, inspection evidence, defects, severity, corrections, regression results, verification and release/approval records.
8. **ASSET LIBRARY** — original downloads, original photographs, reference videos, source provenance/licensing, reconstructed models, meshes, textures, materials, rigs and animation assets. Preserve source originals.
9. **SOCIAL & LIFESTYLE** — clothing and fashion collections, outfits, wardrobe and changing clothes; relationships, friendships, dating, family and rivalries; communications, conversations, calls and messages; parties, birthdays, concerts and other events; invitations, notifications, reminders, social calendars and everyday life activities.

### Ownership boundaries

- SCRIBE & LENS defines the intended weather, climate, seasonal pattern, timing, mood and cinematic use. SYSTEMS implements simulation and state changes; WORLD supplies city/environment geometry and materials that respond.
- PEOPLE owns character identity, personality, behavior, animation and an individual Sim's remembered encounters. SOCIAL & LIFESTYLE owns what people wear, their social ties, communications, events, notifications and everyday activities. Cross-link both when needed.
- WORLD owns the physical city layout and building records. TRANSPORTATION owns transport assets, routes and operations. SYSTEMS owns the mechanics and data behavior that make them function.
- QUALITY records independent review and evidence; it does not silently rewrite production artifacts.
- AI project memory is not the same as in-game Sim memory. Sim memories are game data; the PEOPLE memory section documents their design and implementation.

## 3. Memory retrieval and write-back

Every task begins with a Master Project lookup, then retrieves only the relevant department records and linked records. The Super Agent maintains a compact active working summary and does not load the entire project archive into every prompt.

Every durable record must include, as applicable:
- Stable record ID and title
- Memory section and subcategory
- Status: approved, proposed, unresolved, in progress, implemented, tested, accepted, or superseded
- Version and last-updated date
- Source/provenance and creator decision reference
- Requirements/specification and acceptance criteria
- Related record IDs across memory sections
- Asset/file locations and identifiers
- Dependencies, risks, and open questions
- Build/package history and QA evidence

After each package, write back changes to the relevant memory section and update the Master Project index/status. Never overwrite or discard original asset sources. Keep a backup of project memory; an external drive must not be the only copy.

Initial storage may use organized Markdown/JSON plus a lightweight SQLite full-text index. Embeddings/vector search are optional later, not a prerequisite. External storage reduces active prompt/context loading but does not reduce the RAM needed to load model weights.

## 4. Authority, safeguards and honesty

- Creator-approved requirements are mandatory unless the Creator changes them.
- Mark assumptions and unresolved details; never turn proposals into approved canon.
- Do not invent test results, file changes, builds, integrations, model availability or live worker status.
- Use one active local model inference at a time on the constrained shared host unless a verified capacity test supports another limit.
- Hosted inference remains off unless exact free quota and data terms are verified. Paid fallback is prohibited without explicit Creator authorization.
- No agent/runtime process may merge to `main`, spend money, enable paid services, or change protected project direction without explicit authorization.
- A written charter or model assignment does not mean a live worker is running.

## 5. First production priority

The first work is creative intelligence and city foundation, not construction of the entire surrounding world.

1. Read and reconcile approved SCRIBE & LENS creative direction, including the opening train-arrival cinematic, atmosphere, weather and camera requirements.
2. Create the Hustle City master plan and authoritative spatial registry.
3. Establish major expressways, streets and permanent street names.
4. Establish rail/transit corridors and station reservations, including the HIM train, city train and subway; preserve unresolved expansions of acronyms instead of guessing.
5. Establish the marina/waterfront and its access.
6. Complete neighborhood/district layout and building plots.
7. Begin detailed building and venue packages against the approved city geometry.

The opening cinematic's train station, train route, camera staging and weather requirements must be reserved in the city plan early. Detailed outer-world construction is deferred; build Hustle City itself first.

## 6. Runtime status

This charter is the canonical target design. The existing IntelliSync runtime was built around earlier multi-agent stations and does not yet prove support for this single-worker plus external ChatGPT QA cycle. Keep the scheduler disabled until a dedicated configuration, handoff/QA workflow, tests, and target-host model inference have been verified.


## 7. Continuous production and correction ownership

The default is to let the Super Agent continue productive work while ChatGPT reviews earlier submitted packages. ChatGPT does not interrupt the worker for every small defect.

- ChatGPT may make a small, isolated, unambiguous, low-risk correction directly when the necessary repository/file access exists and the change does not require the Super Agent's specialist tools or environment. Every such edit must be logged and verified.
- Moderate, technical, multi-file, asset, or domain-specific corrections are assigned to the Super Agent in a prioritized correction queue. The agent can finish its current safe package before taking them.
- The Creator may inspect deliverables and give small direction changes. ChatGPT records and routes them; do not make the Creator repeat known requirements.
- Stop starting new packages and request a Creator + ChatGPT + Super Agent group review when core architecture/direction is wrong, a critical dependency is broken, the same major defect recurs, a safety/security/data-loss issue appears, or multiple related high-severity issues accumulate (guideline: three or more related moderate/high issues in one package).
- Keep production, correction and minor-fix queues distinct. Do not modify an immutable package version during active QA. Submit versioned corrections.
- ChatGPT must not silently perform substantial production work, invent verification, or claim an untested change is fixed. The Super Agent remains responsible for specialist implementation.
