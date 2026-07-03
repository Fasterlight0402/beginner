extends Node


# 为了避免脚本过多，一般只在根节点创造脚本
# 在一个脚本内，控制若干个节点的分工合作
# 例子：
# 上节课 中小球接触玩家2 的拍子时，发出响声
# 本质：在Area2D的节点内，命令声音节点工作
# 前提：在rea2D的节点内，获取声音节点对象
# 操作：声音节点对象调用播放音乐的函数

func _ready() -> void:
# 在这里获取节点
# 自定义一个变量保存
	var a=get_node("AudioStreamPlayer")
# .play() 声音节点自带的函数，播放  .前面的节点内声音
	a.play()

# 还有一个简写方法
	var b=$AudioStreamPlayer
	b.play()
	

# 与get_node()相关的函数展示与用法
# ① get_child() 直接获取子节点
#	()内的参数需要填写为整数，为子节点在父节点下的序号数
	get_child(2)

#② get_parent()   获取当前节点的父节点 与 get_node('..') 作用相同
	get_parent()
	get_node('..')

# ③ / 获取多级子节点，多级父节点
	get_node('AudioStreamPlayer/AudioStreamPlayer')
# 获取了声音节点的子节点

# ④ get_children   获取所有直接子节点,子节点的子节点并不能被获取
	self.get_children()
# self. 全部都可以被省略

# get_node() 的优缺点
# 	优点：
# 		可以直接获取对象，方便简捷

# 	缺点：
# 		必须知道子节点的名称 | 如果对象，函数不存在，会error，对分块测试不友好

# 所以，在同一个场景内部，一般使用 get_node()来协调各个节点
# 在场景与场景之间，使用 信号 





func _process(delta: float) -> void:
	pass
