extends Node3D
const PLAYER_SCRIPT = preload("res://scripts/player.gd")

func _ready() -> void:
	_build_environment()
	_build_block()
	_build_player()
	_build_hud()

func _mat(color: Color) -> StandardMaterial3D:
	var m := StandardMaterial3D.new()
	m.albedo_color = color
	m.roughness = 0.82
	return m

func _box(label: String, size: Vector3, pos: Vector3, color: Color) -> void:
	var mesh := BoxMesh.new()
	mesh.size = size
	var instance := MeshInstance3D.new()
	instance.name = label
	instance.mesh = mesh
	instance.position = pos
	instance.material_override = _mat(color)
	add_child(instance)
	var body := StaticBody3D.new()
	var collision := CollisionShape3D.new()
	var shape := BoxShape3D.new()
	shape.size = size
	collision.shape = shape
	body.add_child(collision)
	instance.add_child(body)

func _build_environment() -> void:
	var world := WorldEnvironment.new()
	var env := Environment.new()
	env.background_mode = Environment.BG_COLOR
	env.background_color = Color(0.055, 0.075, 0.16)
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.ambient_light_color = Color(0.55, 0.62, 0.9)
	env.ambient_light_energy = 0.7
	world.environment = env
	add_child(world)
	var sun := DirectionalLight3D.new()
	sun.rotation_degrees = Vector3(-48, -32, 0)
	sun.shadow_enabled = true
	add_child(sun)

func _build_block() -> void:
	_box("Street", Vector3(100,0.2,100), Vector3(0,-0.2,0), Color(0.12,0.14,0.19))
	_box("CrossStreet", Vector3(100,0.22,12), Vector3(0,-0.08,0), Color(0.19,0.2,0.24))
	_box("MainAvenue", Vector3(12,0.24,100), Vector3(0,-0.06,0), Color(0.19,0.2,0.24))
	for i in range(-4,5):
		_box("LaneDash_%d" % i, Vector3(0.25,0.03,3.2), Vector3(0,0.08,i*8.0), Color(0.92,0.83,0.56))
	var positions := [Vector3(-23,7,-22),Vector3(23,10,-23),Vector3(-24,9,24),Vector3(24,6,24)]
	var heights := [14.0,20.0,18.0,12.0]
	var colors := [Color(0.18,0.24,0.38),Color(0.25,0.22,0.38),Color(0.2,0.3,0.39),Color(0.36,0.23,0.36)]
	for i in range(positions.size()):
		var h: float = heights[i]
		_box("ChicagoInspiredBuilding_%d" % i, Vector3(18,h,18), positions[i]+Vector3(0,h/2.0,0), colors[i])
		for floor_index in range(int(h/3.0)):
			_box("WindowBand_%d_%d" % [i,floor_index], Vector3(18.08,0.16,18.08), positions[i]+Vector3(0,floor_index*3.0-h/2.0+1.5,0), Color(0.18,0.55,0.82))
	_box("Plaza", Vector3(10,0.16,10), Vector3(9,0.02,9), Color(0.32,0.35,0.43))
	_box("WelcomeSign", Vector3(0.35,4.5,8), Vector3(13,2.4,14), Color(0.12,0.55,0.88))
	_box("ShowroomVehicleBody", Vector3(2.2,0.75,4.4), Vector3(-8,0.7,7), Color(0.82,0.16,0.48))
	_box("ShowroomVehicleRoof", Vector3(1.8,0.65,2.0), Vector3(-8,1.35,7), Color(0.08,0.12,0.2))
	_box("ParkGreen", Vector3(12,0.18,9), Vector3(-12,0.03,-10), Color(0.12,0.32,0.25))

func _build_player() -> void:
	var player := CharacterBody3D.new()
	player.name = "Player"
	player.set_script(PLAYER_SCRIPT)
	player.position = Vector3(0,1.1,18)
	add_child(player)

func _build_hud() -> void:
	var layer := CanvasLayer.new()
	add_child(layer)
	var title := Label.new()
	title.text = "HUSTLE CITY  |  CHICAGO-INSPIRED DISTRICT"
	title.position = Vector2(24,18)
	title.add_theme_font_size_override("font_size",22)
	title.add_theme_color_override("font_color",Color(0.65,0.86,1))
	layer.add_child(title)
	var help := Label.new()
	help.text = "WASD / ARROWS: MOVE     MOUSE: LOOK     SHIFT: RUN     ESC: RELEASE MOUSE"
	help.position = Vector2(24,54)
	help.add_theme_font_size_override("font_size",14)
	help.add_theme_color_override("font_color",Color(0.93,0.91,1))
	layer.add_child(help)
	var footer := Label.new()
	footer.text = "FIRST PLAYABLE BLOCK  •  DEVELOPMENT PREVIEW"
	footer.anchor_top = 1.0
	footer.anchor_bottom = 1.0
	footer.position = Vector2(24,-42)
	footer.add_theme_color_override("font_color",Color(1,0.55,0.78))
	layer.add_child(footer)
