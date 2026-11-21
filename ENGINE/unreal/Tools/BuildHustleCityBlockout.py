"""Generate the first greybox district for Hustle City.

Run inside Unreal Editor with the Python Editor Script Plugin enabled:
Tools > Execute Python Script > select this file.

Creates /Game/Maps/HC_Prototype. This is a greybox foundation, not a
finished district. EditorLevelLibrary is retained for broad UE5 compatibility;
some UE5 releases mark it deprecated but still expose it to Python.
"""
import unreal

LEVEL_PATH = "/Game/Maps/HC_Prototype"
CUBE_PATH = "/Engine/BasicShapes/Cube.Cube"


def require_asset(path):
    asset = unreal.load_object(None, path)
    if asset is None:
        raise RuntimeError("Required Unreal asset could not be loaded: " + path)
    return asset


def spawn_cube(label, location, scale, cube_mesh):
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.StaticMeshActor,
        unreal.Vector(*location),
        unreal.Rotator(0.0, 0.0, 0.0)
    )
    if actor is None:
        raise RuntimeError("Could not spawn actor: " + label)

    actor.set_actor_label(label)
    mesh_component = actor.get_editor_property("static_mesh_component")
    mesh_component.set_static_mesh(cube_mesh)
    actor.set_actor_scale3d(unreal.Vector(*scale))
    return actor


def spawn_actor(actor_class, label, location, rotation):
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        actor_class, unreal.Vector(*location), unreal.Rotator(*rotation)
    )
    if actor is None:
        raise RuntimeError("Could not spawn actor: " + label)
    actor.set_actor_label(label)
    return actor


def build():
    cube_mesh = require_asset(CUBE_PATH)

    if not unreal.EditorLevelLibrary.new_level(LEVEL_PATH):
        raise RuntimeError("Could not create level: " + LEVEL_PATH)

    # One kilometre square greybox ground surface.
    spawn_cube("HC_Ground_Plane", (0, 0, -100), (500, 500, 1), cube_mesh)

    # Four north-south and four east-west road strips.
    for x in (-180, -60, 60, 180):
        spawn_cube("HC_Road_NS_{:03d}".format(x),
                   (x, 0, 1), (8, 500, 0.08), cube_mesh)
    for y in (-180, -60, 60, 180):
        spawn_cube("HC_Road_EW_{:03d}".format(y),
                   (0, y, 1.2), (500, 8, 0.08), cube_mesh)

    # Initial building masses. Heights are intentionally varied for skyline
    # rhythm; these are placeholders for authored architecture later.
    heights = (18, 32, 24, 45, 28, 55, 20, 38, 26, 48, 22, 34)
    positions = [
        (-120, -120), (-60, -120), (60, -120), (120, -120),
        (-120, -60), (120, -60), (-120, 60), (120, 60),
        (-120, 120), (-60, 120), (60, 120), (120, 120),
    ]
    for index, ((x, y), height) in enumerate(zip(positions, heights), start=1):
        spawn_cube(
            "HC_Greybox_Building_{:02d}".format(index),
            (x, y, height / 2.0 + 2),
            (32, 32, height / 2.0),
            cube_mesh
        )

    spawn_actor(
        unreal.PlayerStart,
        "HC_PlayerStart",
        (-35, -35, 120),
        (0, 45, 0)
    )

    sun = spawn_actor(
        unreal.DirectionalLight,
        "HC_Sun_KeyLight",
        (0, 0, 300),
        (-45, -35, 0)
    )

    # Intensity belongs to the light component, not the actor.
    light_component = sun.get_editor_property("directional_light_component")
    light_component.set_editor_property("intensity", 8.0)

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Unreal Editor could not save the generated level")

    unreal.log("Hustle City greybox created: " + LEVEL_PATH)


build()
