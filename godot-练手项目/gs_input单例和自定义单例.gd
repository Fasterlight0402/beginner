extends Sprite2D



# 单例
#	单例是一个可以在任何一个脚本中对其进行直接访问的对象，分为内置单例和自定义单例。
#	每个单例都是独一无二的对象
#	
#	内置单例不是节点，主要成员是各类server，开发者可以直接使用它们控制游戏程序的图形与音效等内容
#	此外还包括了一些其他对象，它们设计的范围包括网络、时间、电脑系统、输入等
#
#	自定义单例必须是节点类型的对象，是开发者自定义的全局对象

# input()单例
# ①input
# input 是一个重要对象，它可以对玩家的按键情况进行反馈
# input 的 Action 手动设置
# input 的 常用函数介绍
#
# ②轮询
# 在_process() 或 _physic_process 中通过 input 单例对按键情况进行判断
# 从而影响游戏内情况的变化。这种反复检测输入情况的编码方式被称为轮询
# if+轮询+修改内置变量==游戏在玩家的控制下发生实质性的改变


# get_action_strength()
# 返回你按下某个按键的力度，一般在 0-1 之间，如果使用键盘，固定为0和1


# 自定义单例
# ①自定义单例步骤
#	在项目设置中选择Autoload
#	选择脚本路径
#	点击添加
#
#②自定义单例特征及用途
#	可以在任何一个脚本中对它们进行直接访问
#	用于记录全局变量

func _ready() -> void:
	print(cus_01.a)
	cus_01.b()
	print(Input.get_action_strength('向左走'))
	


# 画面每刷新一次，_process()函数就会被调用一次

func _process(_delta: float) -> void:
	if Input.get_action_strength('向左走'):
		self.position.x-=1
	else :
		self.position.x+=1
	
	
