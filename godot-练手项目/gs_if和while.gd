extends Node


# Called when the node enters the scene tree for the first time.
func _enter_tree() -> void:
	var a=0.1
	var b=0.2
	var c='114514'
	
# 判断方法和py相同，if语句的格式也相同
	if a+b==0.3:
		print('hello')
# 小数的精度有问题，在二进制中 0.1并不是单纯的0.1
# 所以并不会打印 hello

# 非空字符串默认为true，字符串和bool不太能相互转化
	if c:
		print('godot')


# is_equal_approx(x,y) 是个返回bool值 的函数
# 两个浮点数是否近似相等的意思
	if is_equal_approx(a+b,0.3):
		print('world')

# if 后面跟 elif else 用法和py完全相同

# while 循环方法和 py完全相同，注意避免死循环，也可以用break打断循环
	var x =1
	while x<20:
		if x>=10:
			break
		print(x)
		x+=1



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
