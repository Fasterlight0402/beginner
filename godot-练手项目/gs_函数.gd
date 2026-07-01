extends Node


# 定义函数
#
# 调用函数，和python一样的
func _enter_tree():
	var d=add(1,1)
	print(d)

# 函数逻辑和py的相同，return后就不执行了
# 函数的参数可以自定义接受数据的类型
# 关键词参数，如果不给b的实参，就会默认b=16进行输出

# 可以在函数括号后面跟一个 -> 类型关键词 ，代表能传入的参数类型
func add(a:int,b=10)->int:
	var c=a+b
	print('Hello')
	return c


	

# 内置虚函数的调用
# 常用的虚函数: 
#_init  	节点被创建时
#ready  	当一个节点的全部 子节点 接入 场景树 时调用

#_process  	画面刷新时自动调用
#_physic_process 物理引擎刷新时节点调用
# 这两个虚函数，()里有默认参数，参数值代表距离上次刷新的时间间隔

# 一个函数中定义的变量，无法在另一个函数中直接调用
# 一般情况下，func结束后，内部的变量和值会自动销毁
