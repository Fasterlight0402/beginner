extends Sprite2D


# Array 数组，类似python的元组
# 可以在array[]中加入想要存入数组中的值的类型，类型不对会报错
# 可用 数组名[序号] 来访问数组中的某个元素的值
# 数组可以通过函数来增加或者去除内部数据，可以通过size()来获取数组内元素的总数

# 添加 .append(值)  把 值 添加到数组的最后

# 删除 .erase(值)  把 值 从数组中删除,默认删除序号更小的 值
#	remove_at()  可以按照序号数把 元素 删除

# .size() 相当于 .len(), 返回 数组 的长度

# 数组是引用变量 数组A=数组B时，AB都同时引用同一个数组，修改数组B会影响数组A
var a:Array=[1,1.1,'hello',true]

func _ready() -> void:
	var b:Array[int]=[1,1,4,5,1,4]
	var d=a
	print(a[2],'\t',b[0])
	d.append(0)
	d.erase('hello')
	d.remove_at(2)
	print(a,'\t',d)
	for i in b:
		print(i)
		i+=1
	
# for 循环中 修改 i的值，对于遍历的数组来说没有影响，只会改变i自己的值
