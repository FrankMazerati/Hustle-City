"""Import staged FBX/OBJ/glTF assets into the current Unreal project.

Run inside the Unreal Editor with Python Editor Script Plugin enabled.
Place source files under Content/_Staging/<PackName>/ before running.
This script imports only interchange files; it does NOT migrate .uasset sample projects.
"""
import os
import unreal

STAGING_ROOT = os.path.join(unreal.Paths.project_content_dir(), "_Staging")
DESTINATION_ROOT = "/Game/Imported"

SUPPORTED = {".fbx", ".obj", ".gltf", ".glb"}

def main():
    if not os.path.isdir(STAGING_ROOT):
        unreal.log_warning("Hustle City importer: staging folder does not exist: " + STAGING_ROOT)
        return

    tasks = []
    for root, dirs, files in os.walk(STAGING_ROOT):
        dirs.sort()
        for filename in sorted(files):
            ext = os.path.splitext(filename)[1].lower()
            if ext not in SUPPORTED:
                continue

            source = os.path.join(root, filename)
            relative = os.path.relpath(root, STAGING_ROOT).replace("\\", "/")
            destination = DESTINATION_ROOT
            if relative != ".":
                destination = destination + "/" + relative

            task = unreal.AssetImportTask()
            task.filename = source
            task.destination_path = destination
            task.automated = True
            task.replace_existing = False
            task.save = True
            tasks.append(task)

    if not tasks:
        unreal.log_warning("Hustle City importer: no FBX/OBJ/glTF/glb files found in _Staging.")
        return

    unreal.log("Hustle City importer: importing {} staged files.".format(len(tasks)))
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)

    imported = sum(len(task.imported_object_paths) for task in tasks)
    unreal.log("Hustle City importer: {} assets imported from {} source files.".format(imported, len(tasks)))
    unreal.log_warning("Review imported meshes, materials, collisions, LODs, scale, and texture settings before production use.")

if __name__ == "__main__":
    main()
