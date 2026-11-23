# Hustle City — Opening Cinematic & Bella Rose Guided Introduction

**Status:** Production brief derived from creator-approved direction. This is the first visual vertical-slice target. It is not a claim that the scene, assets or cinematics have been built.

## Non-negotiable player-control rule

The player has **no character control during the entire opening cinematic, station sequence, Hustle Towers visit, or Bella Rose guided tour**. Movement and camera changes are authored/cinematic or guided. Player control is released only after the introduction/tour is complete and Bella has wrapped up. Do not hand control back after the train disembarkation or midway through the tour.

## Opening sequence

1. Rain outside a passenger train; begin on a cinematic view through a rain-streaked train window.
2. Exterior overhead/aerial shot of the train moving along wet tracks toward Hustle City.
3. Reveal the skyline and establish the city's atmosphere and arrival.
4. Train brakes and stops at the station; passengers disembark, still under cinematic control.
5. Follow the new arrivals through the station into the concierge hall.
6. They bump into Bella Rose; establish her personality and introduce her naturally.
7. Bella guides the group to Hustle Towers.
8. Show the Towers exterior and courtyard, then the interior lobby.
9. Visit Bella Rose's room and let her establish her home base and personal style.
10. The player books their own room at Hustle Towers.
11. Meet Bella downstairs again.
12. Bella begins the selected guided tour. Hustle Towers is mandatory first stop.

## Tour modes

### Short tour
- Covers Hustle Towers and its complete facilities/amenities introduction.
- Bella explains the home base, rooms, services, shared spaces and relevant amenities.
- Only after she completes the short tour and closes the introduction does player control unlock.

### Full tour
- Hustle Towers is always the first mandatory destination.
- Bella then offers the remaining destinations one at a time.
- The player may see all destinations, choose selected stops, or end the tour when ready.
- The tour remains cinematic/guided and narrated throughout; the player does not directly control character movement until it ends.
- Destinations already toured are remembered so returning players can skip or take a short tour.
- On later launches, the player's home/start location is Hustle Towers even if they previously logged out elsewhere.
- When the introduction ends, the last toured location is the initial gameplay location for that first session.

## Guided-tour destinations

1. Hustle Towers — mandatory home base and amenities.
2. Hustle Club.
3. The Shuffle Club — the casino is inside The Shuffle Club; do not model it as a separate destination.
4. Velvet Lounge.
5. American Swagger Clothing Company.
6. Hustle City Marina and Yacht Club.
7. Mazerati Boyz Automotive Group — working name; final rename pending creator approval.
8. Get Wild Beach.
9. We Fly High International Airport — name subject to the current project naming decision.

## Bella Rose voice and role

Bella is more than a tutorial narrator: she is the player's personal guide to Hustle City. Her delivery is confident, sassy, funny, high-energy, stylish and street-smart, with a warm, conversational, girly-hood swagger. She introduces the city's culture, opportunities, businesses, rules, lifestyle, food, drinks, nightlife, hustle areas, money-making, transportation, entertainment, shopping, relationships and neighborhoods.

Use the creator's sample line as voice/tone reference, not mandatory final dialogue:

> “Girl, let me tell you something. This city right here? Baby, it is LIVE. I moved out here about 20 years ago, and I ain't left since. You got everything you need out here. Food, drinks, shopping, money-making opportunities… honey, you better come with a plan!”

Bella's narration should be tied to what the camera is showing. Avoid long static exposition while the visuals fail to demonstrate the subject being discussed.

## First visual milestone / asset needs

- passenger train exterior, train interior and rain-streaked window;
- wet rails, rail corridor, train motion and arrival platform;
- city skyline and approach vistas;
- station exterior and grand concierge hall;
- Bella Rose character, rig, facial performance, walk cycle and gestures;
- Hustle Towers exterior, courtyard, lobby, bedroom and room-booking interaction;
- cinematic camera rigs, Sequencer shots, transitions and audio ambience;
- guided pathing, dialogue state, tour selection, save/revisit flags and control-lock/unlock state.

## Required specialist handoffs

- SCRIBE: scene beats, Bella dialogue, continuity and tour narrative.
- LENS: shot list, camera choreography, framing, timing and transitions.
- P04-ARCHITECTURE / P05-INTERIORS: station, Towers, courtyard, lobby and room spatial design.
- P06-TRANSIT: train, tracks, platform, arrival and passenger movement.
- P08-CHARACTERS / P09-NPC-NAV: Bella's visual/animation requirements and guided movement.
- P10-GAMEPLAY / P11-ONBOARDING: booking, tour state, control gating, skip/revisit and start-location rules.
- P12-UNREAL-INTEGRATION: Sequencer/Blueprint implementation plan, asset import and test map.
- QA-1/2/3: independently review assigned production-specialist outputs. SCRIBE and LENS outputs require separate independent review; neither approves their own work.

## Acceptance criteria

- The entire sequence plays without player movement control until the tour is finished.
- The train arrival, station walk, Bella meeting and Hustle Towers visit are visibly shown, not skipped by summary text.
- Bella's narration corresponds to the location/action on screen.
- Short tour ends after the complete Towers introduction; full tour offers optional destinations after Towers.
- Shuffle Club contains the casino as an internal venue.
- Tour progress and visited destinations persist correctly.
- First-session tour ending location is respected; later launches start at Hustle Towers.
- All assets have source/license/version metadata and pass scale, collision, material and performance review.
- No asset is marked imported until it is actually present and verified in the Unreal project.
