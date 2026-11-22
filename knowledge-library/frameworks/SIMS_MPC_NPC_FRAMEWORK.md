# Hustle City Sims / MPC / NPC Simulation Framework

**Status:** Initial framework. The intended meaning and technical scope of “MPC” must be confirmed with the creator. This document uses NPC to mean non-player character. “Sims-style” describes a living-life simulation design reference, not a requirement to copy another game's proprietary systems.

## Purpose
Make Hustle City feel populated by people who live, work, travel, socialize, maintain routines and react to the changing city. NPCs should have purposeful behavior, not exist only as static scenery.

## Simulation layers
- **Identity and role:** resident, commuter, visitor, employee, business owner, transit worker, construction worker, emergency responder, vendor and others.
- **Daily schedule:** home, work, errands, recreation, social activities, travel and rest.
- **Needs and goals:** context-appropriate priorities and short-/long-term goals.
- **Relationships:** family, friends, coworkers, crews, neighbors, rivals and acquaintances.
- **Social behavior:** greetings, conversations, group activities, conflict, cooperation and relationship changes.
- **Economy and work:** jobs, shifts, wages, purchases, business operations and services where supported.
- **Mobility:** walking, driving, public transit, cycling and destination selection.
- **World awareness:** weather, time, crowding, construction, closures, events and district conditions.
- **Memory and continuity:** selected interactions and meaningful events persist according to game rules.

## Population by place
Rail stations: passengers, operators, attendants, security, cleaners, vendors and maintenance. Construction sites: laborers, engineers, supervisors, inspectors and deliveries. Residential blocks: residents, visitors, deliveries and families. Commercial areas: customers, employees, owners, service workers and nightlife crowds. Civic/recreation areas: visitors, staff and scheduled activities.

## Believable routines and scalable simulation
NPCs should vary by role, personality, relationships, location, time, weather and events. Simulation detail can scale:
- High detail near the player and for story-critical characters.
- Reduced simulation for nearby crowds.
- Abstract schedules, population counts or event-driven updates for distant areas.
Use reproducible behavior where useful for debugging and QA. Avoid identical schedules and obvious repeated loops.

## Player interaction
Define which NPCs can be greeted, spoken to, hired, served, followed, befriended, challenged or otherwise interacted with. Depth depends on character importance, role, context and scope. Dialogue and social behavior must coordinate with narrative, character and gameplay frameworks.

## Technical and data design
Eventually specify identity, archetypes, schedules, jobs, locations, relationships, needs/goals, state transitions, memory, spawn/despawn rules, navigation, crowd density, persistence, replication and server authority. Do not create database tables or networking rules solely from this draft; reconcile with the data model and multiplayer architecture first.

## Performance and QA
Define budgets for active, nearby and distant populations. Test schedule continuity, pathfinding, crowd congestion, station boarding, construction interactions, time changes, save/load and multiplayer consistency.

## Open decisions
Confirm “MPC”; decide simulation depth, persistent NPC scope, relationship and memory rules, routines, and multiplayer authority.
