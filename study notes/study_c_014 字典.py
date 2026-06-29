# 字典这个数据结构活跃在所有python程序的背后，即便你的源代码并没有直接用到它。
# 字典是python中唯一实现映射关系的内置类型

# 字典映射速度更快 dict

q={'迪迦','大古'}  # 这个是set 集合 ，不是字典dict
w={'吕布':'奉先'}  # 这个是字典，中间有个冒号  左边叫做键 右边叫做值
# 字典中通过 键 来获得 值

print(w['吕布'])

w['关羽']='云长'   # 可以通过创造 键 值 的方式，给字典加东西
print(w)

# 字典方法 ①
# 创建字典   dict()
#   1.直接使用大括号创建

#   2.dict()
e=dict(张飞='翼德',诸葛亮='孔明')    # 这种方法，键上面不能加''尽管它是个字符串

#   3.使用列表，列表中的每个元素都是元组包裹起来的键值对
r=dict([('赵云','子龙'),('周瑜','公瑾')])   # dict(zip(x,y)))

#   4.可以使用混合方法
t=dict({'吕布':'奉先'},曹操='孟德')

#   5.使用zip()函数
y=dict(zip(['悟空','八戒'],['大师兄','二师弟']))


# 字典方法 ②
#   增  fromkeys(iterable[values])
u=dict.fromkeys('abc',123)
print(u)
u['a']=10  # 这样可以方便地改 字典中 a 对应的值，当然得是十进制数字

print(u)   # 所以字典中的键 是不能重复的 ，重复就会把新的值覆盖旧的值

u['d']=124 # 这样就把d=124 这个键值对 加入到了字典中
print(u)


#   删 pop()
#       pop('key') 如果key不存在，程序异常
#           pop('key','没找到') 如果key不存在，则会返回'没找到'
print(u.pop('a'),'\t',u)  # u.pop('a')会返回a对应的值，之后u里就没有a对应的键值对了

#       popitem()  # python3.7 之后的版本是固定删除最后一个键值对  3.7之前是随机删除一个

print(u.popitem(),'\t',u)

#       del  整个删除字典，字典本身就不存在了
del q

#       clear() 清空字典，字典变为 空字典，字典依然存在
u.clear()
print(u)


#   改
#   update([other])  可以同时传入多个 键值对
lo=dict.fromkeys('abc')   # 不加key的情况下，默认都是 None
lo['a']=11                #  把字典中的a：None  改为 a：11

print(lo)
lo.update({'b':22,'c':33})  # 用{} 的形式，里面必须加''
print(lo)

lo.update(d=44,e=55)        # 用括号的形式，里面需要用等号，不能加''
print(lo)


#   查
#   直接输入[键]就会返回值，若[键]不存在，就会报错
#   get(key[,default])
print(lo.get('h','找不到'))  # 字典里没有h，就返回'找不到'

#   setdefault(key[,default]) 查找字典中的 key 键，如果在就返回对应的value，如果不在就添加 键值对

print(lo.setdefault('a',999))  # 因为字典中本来就有a：11，所以输入999无效

print(lo.setdefault('i',999),lo)  # 字典中没有 key i 所以 添加了新的 键值对 i：999

#   .items()    .keys()   .values()
#   获取字典的视图对象


#   拷贝
#   .copy() 浅拷贝

#   其他功能
#   len()  求字典中 键值对 的数量
#   in      not in      求出某个keys是否存在 dict 中
#   list()  这样会得到字典中所有 键keys 组成的列表
#   list(dict.values())  可以得到 dict 中所有 values 组成的 list

#   .iter()    将字典转化为迭代器，只能使用一次

#   reversed()  排序

print(tuple(reversed(lo.values())))
# reversed 把字典转为迭代器，所以要用 str，tuple，list 转为迭代对象再打印


#   字典的嵌套
loo={'张三':{'被判':15,'罚款':20},'李四':{'被判':10,'罚款':10}}  # 字典嵌套字典

print(f'{list(loo.keys())[0]}')
print(loo['张三']['罚款'])

#   字典也可以嵌套列表

#   字典推导式
looo={'F':70,'G':80,'H':90}
print(looo)
oool={v:k for k,v in looo.items()}   # 将 键值对 反过来了
print(oool)

oool2={v:k for k,v in looo.items() if v>=80}  # 字典嵌套中也可以加上if 筛选
print(oool2)

uni={x:ord(x) for x in 'abcd'}  # 把abcd 的unicode 转入到字典 uni 中
print(uni)

uni2={x:y for x in[1,2,3]for y in [1,2,3]}  # 后生成的键值对会覆盖掉前面的键值对
print(uni2)
#   先是 1：1 还然后 1:2 这样就把 1：1 给覆盖掉了，以此类推 最后只有1：3   2：3  3：3