"""Editor utility: generate the first greybox city blockout for Hustle City.

Run in Unreal Editor with Python Editor Script Plugin enabled:
Tools > Execute Python Script > select this file.
Creates /Game/Maps/HC_Prototype.
"""
import unreal

LEVEL_PATH = "/Game/Maps/HC_Prototype"
CUBE = unreal.load_object(None, "/Engine/BasicShapes/Cube.Cube")


def spawn_cube(label, location, scale):
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.StaticMeshActor, unreal.Vector(*location), unreal.Rotator(0, 0, 0)
    )
    actor.set_actor_label(label)
    actor.get_editor_property("static_mesh_component").set_static_mesh(CUBE)
    actor.set_actor_scale3d(unreal.Vector(*scale))
    return actor


def build():
    unreal.EditorLevelLibrary.new_level(LEVEL_PATH)
    spawn_cube("HC_Ground_Plane", (0, 0, -100), (500, 500, 1))

    for x in (-180, -60, 60, 180):
        spawn_cube("HC_Road_NS", (x, 0, 1), (8, 500, 0.08))
    for y in (-180, -60, 60, 180):
        spawn_cube("HC_Road_EW", (0, y, 1.2), (500, 8, 0.08))

    heights = (18, 32, 24, 45, 28, 55, 20, 38, 26, 48, 22, 34)
    positions = [
        (-120, -120), (-60, -120), (60, -120), (120, -120),
        (-120, -60), (120, -60), (-120, 60), (120, 60),
        (-120, 120), (-60, 120), (60, 120), (120, 120),
    ]
    for index, ((x, y), height) in enumerate(zip(positions, heights), start=1):
        spawn_cube("HC_Greybox_Building_{:02d}".format(index),
                   (x, y, height / 2.0 + 2), (32, 32, height / 2.0))

    unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.PlayerStart, unreal.Vector(-35, -35, 120), unreal.Rotator(0, 45, 0)
    )
    sun = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.DirectionalLight, unreal.Vector(0, 0, 300), unreal.Rotator(-45, -35, 0)
    )
    sun.set_actor_label("HC_Sun_KeyLight")
    sun.set_editor_property("intensity", 8.0)
    unreal.EditorLevelLibrary.save_current_level()
    unreal.log("Hustle City greybox created: " + LEVEL_PATH)


build()
