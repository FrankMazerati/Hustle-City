extends CharacterBody3D
const WALK_SPEED := 5.2
const RUN_SPEED := 8.0
const SENSITIVITY := 0.0025
var camera_pivot: Node3D
var pitch := -0.12

func _enter_tree() -> void:
	_add_action("move_forward",[KEY_W,KEY_UP])
	_add_action("move_back",[KEY_S,KEY_DOWN])
	_add_action("move_left",[KEY_A,KEY_LEFT])
	_add_action("move_right",[KEY_D,KEY_RIGHT])

func _add_action(action: String, keys: Array) -> void:
	if not InputMap.has_action(action):
		InputMap.add_action(action)
	for code in keys:
		var event := InputEventKey.new()
		event.physical_keycode = code
		if not InputMap.action_has_event(action,event):
			InputMap.action_add_event(action,event)

func _ready() -> void:
	var visual := MeshInstance3D.new()
	var capsule := CapsuleMesh.new()
	capsule.radius = 0.38
	capsule.height = 1.8
	visual.mesh = capsule
	var material := StandardMaterial3D.new()
	material.albedo_color = Color(0.12,0.62,0.92)
	visual.material_override = material
	visual.position.y = 0.9
	add_child(visual)
	var collision := CollisionShape3D.new()
	var shape := CapsuleShape3D.new()
	shape.radius = 0.38
	shape.height = 1.8
	collision.shape = shape
	collision.position.y = 0.9
	add_child(collision)
	camera_pivot = Node3D.new()
	camera_pivot.position.y = 1.55
	add_child(camera_pivot)
	var camera := Camera3D.new()
	camera.position = Vector3(0,1.0,5.5)
	camera.rotation.x = -0.12
	camera.current = true
	camera_pivot.add_child(camera)
	Input.mouse_mode = Input.MOUSE_MODE_CAPTURED

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventMouseMotion and Input.mouse_mode == Input.MOUSE_MODE_CAPTURED:
		rotate_y(-event.relative.x*SENSITIVITY)
		pitch = clampf(pitch-event.relative.y*SENSITIVITY,-0.9,0.45)
		camera_pivot.rotation.x = pitch
	if event is InputEventScreenDrag:
		rotate_y(-event.relative.x*SENSITIVITY*1.6)
		pitch = clampf(pitch-event.relative.y*SENSITIVITY*1.6,-0.9,0.45)
		camera_pivot.rotation.x = pitch
	if event is InputEventKey and event.pressed and event.keycode == KEY_ESCAPE:
		Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
	if event is InputEventMouseButton and event.pressed and Input.mouse_mode == Input.MOUSE_MODE_VISIBLE:
		Input.mouse_mode = Input.MOUSE_MODE_CAPTURED

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity.y -= 20.0*delta
	else:
		velocity.y = 0.0
	var input_dir := Vector2(Input.get_action_strength("move_right")-Input.get_action_strength("move_left"),Input.get_action_strength("move_back")-Input.get_action_strength("move_forward")).normalized()
	var direction := (transform.basis*Vector3(input_dir.x,0,input_dir.y)).normalized()
	var speed := RUN_SPEED if Input.is_key_pressed(KEY_SHIFT) else WALK_SPEED
	if direction:
		velocity.x = direction.x*speed
		velocity.z = direction.z*speed
	else:
		velocity.x = move_toward(velocity.x,0,speed*5.0*delta)
		velocity.z = move_toward(velocity.z,0,speed*5.0*delta)
	move_and_slide()
