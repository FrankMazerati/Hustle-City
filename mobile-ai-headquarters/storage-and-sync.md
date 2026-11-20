# Phone Storage, GitHub Synchronization, and USB Asset Storage

## Storage roles

### Galaxy A17 internal storage
Keep:
- agent prompts, personas, and configuration;
- lightweight Trinity/relay client files;
- project specifications and integration contracts;
- active task metadata and small working copies;
- status snapshots and recent reports.

Do not assume the phone can run multiple large local models. The selected design uses remote AI inference.

### GitHub
Treat the repository as the canonical source for text/code configuration and version history. Synchronize by commits and branches, not by silently copying over newer work. Never commit secrets.

### USB-attached 1 TB storage
Use for:
- large 3D assets and source art;
- exports, renders, and packaged builds;
- archival snapshots and backup copies;
- large datasets that do not belong in Git history.

Use a clear folder structure such as:
`HUSTLE_CITY_ASSETS/`, `HUSTLE_CITY_EXPORTS/`, `HUSTLE_CITY_ARCHIVES/`, and `HUSTLE_CITY_BACKUPS/`.

### Tablet
Use as the review/display workstation for repository changes, pull requests, QA results, previews, and project status.

## USB connection checks

Before relying on the drive:
1. Connect using a compatible USB-C OTG adapter/cable.
2. Confirm Android Files or Samsung My Files detects the drive.
3. Confirm the filesystem is readable and writable.
4. Copy a small test file to the drive and read it back.
5. Check available capacity and safe-eject behavior.
6. If the drive needs more power than the phone supplies, use a powered USB hub.
7. Do not reformat a drive until its contents are backed up and the user explicitly approves.

## Backup policy

- Keep at least two copies of irreplaceable work when practical.
- Do not treat one removable drive as the only copy.
- Maintain dated snapshots and a short restore note.
- Test restoration periodically.
- Keep source code/configuration in GitHub and large binaries in managed asset storage with documented references.

## Synchronization rules

- Pull/fetch before editing.
- Use a feature branch for each task or coherent batch.
- Commit small, descriptive changes.
- Resolve conflicts deliberately; never blindly overwrite.
- Keep main protected and require human approval to merge.
- Do not put API keys, tokens, passwords, or private signing material in phone project folders that are synced to Git.
