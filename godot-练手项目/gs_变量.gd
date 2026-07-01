extends Node

var a=1  
# 定义一个变量，变量名规则和python相同，就是多个 var




# gs中的变量类型,和py中的一样
# 整形 int
# 浮点 float
# 字符串 str
# 布尔 bool

var z:int=1
var x:float=3.9
var c:String='hello'
var v:bool=true
# 没有类型限定，就可以相互转换
# gs中是在变量名字后面加 :类型，来确定什么类型的数
# 只要数字为0 bool就是false 其他为true

# 值变量：A=B,之后修改B并不会改变A
# 引用变量：A=B,之后修改B会随之影响A

# 二维向量
# 二维向量的x属性和y属性，都是浮点类型
var b=Vector2(1,1)

# 定义函数  函数名 ()： 
# py中是def 这里是 func 其他一样
# self. 是为变量指明对象
# gs中的所有变量都要放在函数中
func _enter_tree():
	self.a+=1
	print(self.a)
	z=x
# 这里会把浮点数取高斯函数给到整数
	c=str(x)
	c+=c
# 字符串加法就是后面重复
	print(z,'\t',c)
# 特殊位置符的用法和py相同
	v=!z
# ! 就是反转，专属于bool的运算符
	print(v)

	b.x=20
	b.y=0
# 二维向量的修改方式
	print(b)

# 变量除了定义的过程外，必须在函数内进行数值的修改
# 内置代码中的许多变量在修改后，会对游戏的实际内容产生影响
# 可以用自定义的变量来定义逻辑上的游戏数据
# 而后通过判断逻辑上数据情况，调整内置代码中的变量，对游戏的画面、音效等产生实际的影响
