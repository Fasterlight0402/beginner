extends Area2D


var vec:Vector2=Vector2(1,1)
var init_position
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	self.add_to_group('Ball')
	init_position=position


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	position+=vec
# 小球一直保持往右跑
# 如果小球坐标到某个范围，则调用下面的函数
	#if self.position.x>=500:
		#reset()

func reset():
	if vec.x>0:
		积分系统.score1+=1
	else :
		积分系统.score2+=1
	position=init_position
