extends Label

var c:String='Hello World'
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	self.text=c
# 这里修改label的text，就是显示内容


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
