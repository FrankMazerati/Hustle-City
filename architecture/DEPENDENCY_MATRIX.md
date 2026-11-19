# Cross-Agent Dependency Matrix

| Producer | Must coordinate with | Shared contract / reason |
|---|---|---|
| Geography Atlas | World, City, Transit, Roads, Legal/Canon | Coordinates, sources, licensing, geographic fidelity |
| World Design | City, Environment, Transit, Systems | World scale, geography, travel and expansion |
| City Masterplan | Neighborhood, Roads, Architecture, Transit | Grid, boundaries, roads, district and station placement |
| Neighborhood | City, Architecture, Environment, Social, Economy | Ownership layers, identity, activation, entrances |
| Architecture | Character, Interior, Navigation, Interaction, Environment | Scale, doors, collision, navigation and interaction anchors |
| Interior | Venue, NPC, Character, Navigation, Interaction | Circulation, seating, service points, usable objects |
| Environment | World, City, Vehicle, Character, Audio | Weather, lighting, water, visibility and transition effects |
| Roads | Traffic, Transit, Pedestrian Navigation, City | Lanes, intersections, crossings and signals |
| Transit | City, Architecture, Character, Animation, Navigation | Stations, platforms, boarding and passenger flows |
| Character | Architecture, Clothing, Animation, Vehicle, Transit, Navigation | Rig, scale, movement, attachment slots and access |
| NPC | Navigation, Events, Venue, Social, Operations | Goals, live state, schedules and dialogue truth |
| Clothing | Character, Animation, Character Art | Rig compatibility, layering and motion |
| Interaction | Character, Architecture, Vehicle, Venue, UI, QA | Interaction affordances, preconditions and failure recovery |
| Navigation | City, Architecture, Interior, Transit, NPC, QA | Reachability, traversal and blocked path recovery |
| Vehicle Design | Character, Animation, Vehicle Simulation, Transport Ops | Seats, doors, anchors, capacity and camera |
| Vehicle Simulation | Traffic, Roads, Character Safety, QA | Safe movement, stopping, collision avoidance |
| Traffic | Roads, Vehicle Simulation, Transit, Pedestrian Navigation | Signals, occupancy, priority and deadlocks |
| Transport Operations | Transit, Vehicle, Character, UI, Economy, Multiplayer | Destination journeys, capacity, boarding and arrival |
| Venue | Architecture, Interior, NPC, Interaction, Economy, Events | Venue services and activity loops |
| Poker | Venue, Economy, UI, Multiplayer, QA | Table state, rules, chips, turns and synchronization |
| Crew/Social | UI, Multiplayer, Economy, Events, Security | Membership, chat, feeds, permissions and safety |
| Economy | Backend, Multiplayer, Security, UI, Property | Authoritative balances, transactions and audit |
| Events | NPC, Venue, Social, Ops Dashboard, QA | Event lifecycle, live state, participation and monitoring |
| Godot Engineering | Systems Architecture, all implementation agents, Integration, QA | Scene/script implementation and integration |
| Multiplayer | Backend, Social, Events, Security, QA | Authoritative state, replication and reconnect |
| Backend | Economy, Social, Multiplayer, Ops, Security | Schemas, APIs, persistence and transaction integrity |
| Player Shell UI | Character, Social, Economy, Map, Venue, Accessibility | Persistent identity, currencies and contextual controls |
| Creator Studio | Art agents, Backend, Security, Build, QA | Asset metadata, validation, approval and publishing |
| Operations Dashboard | Events, Backend, Multiplayer, Security, UI | Live telemetry, alerts and authorized intervention |
| AI Orchestration | SAM, all agents, runtime, Backend, Security | Task routing, permissions, logs, model and tool lifecycle |

## Mandatory review rule
A deliverable that changes a shared contract must identify every affected row, request targeted review and wait for blocking approvals. Integration Agent checks compatibility; QA Director checks behavior and evidence; SAM coordinates; creator approves product decisions.
