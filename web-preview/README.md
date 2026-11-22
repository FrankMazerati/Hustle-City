# Hustle City — Browser Preview

This is the lightweight mobile browser companion for early creator reviews. It uses Babylon.js from its public CDN and vanilla HTML/CSS/JavaScript; there is no paid API, backend, or account requirement.

## Scenes
- **HIM:** intercity passenger terminal and train.
- **HCTA:** local rail system examples.
- **Fashion / Swagger District:** a separate central district placeholder; its final identity awaits creator direction.
- **Diamond District:** location of Hustle Towers, the 100-floor vertical landmark.

## Run locally
Open `index.html` through a local static HTTP server. From the repository root, for example:

```bash
python3 -m http.server 8080 --directory web-preview
```

Then open `http://127.0.0.1:8080` in a browser on the same device. On Android, use the UserLAnd terminal and open the device-local address in Chrome if the local networking setup permits it.

## GitHub Pages
The files are static and can be published through GitHub Pages after the project owner enables/configures Pages for the repository. This branch is not automatically a live website. Do not claim a public preview URL until deployment has succeeded and the URL has been checked.

## Controls
- Tap HIM, HCTA, Fashion / Swagger, or Diamond District to switch scenes.
- Drag to orbit; pinch or wheel to zoom.
- Tap Reset view to restore the camera.

## Fidelity and status
This is an early interactive geometry blockout. It proves the browser viewing path and provides spatial review controls; it is not final art, a route map, or a playable game. Babylon.js must load from its CDN, so the browser needs an internet connection.

## Canonical design references
- `../world/TRANSPORTATION_NETWORK_SPEC.md`
- `../world/FASHION_HUB_AND_HUSTLE_TOWERS_SPEC.md`
- `../world/MASTER_GEOGRAPHY_BLUEPRINT.md`
