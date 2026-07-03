extends Area2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
	
func _physics_process(delta: float) -> void:
	for i in get_overlapping_areas():
		if i.is_in_group('Ball'):
			i.vec.x=1
	var y1 = Input.get_action_raw_strength("player1 上")
	var y2 = Input.get_action_raw_strength("player1 下")
	var y3=position.y-y1*5+y2*5
	if y3>16 and y3<630:
		position.y=position.y-y1*5+y2*5
