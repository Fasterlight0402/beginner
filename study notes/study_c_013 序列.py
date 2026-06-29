# 序列
# 列表，元组，字符串的共同点：
#   可通过索引获取每一个元素
#   第一个元素序号都是0
#   可通过切片的方法获得范围内的集合
#   有很多共同运算符
#
# python 将列表，元组，字符串统称为序列
# 分为可变序列 不可变序列

# 能够作用于序列的一些运算符和函数
# + 序列进行拼接  * 序列进行重复

"""
"""
'''
[1,2,3]*3==[1,2,3,1,2,3,1,2,3]
[1,1,4]+[5,1,4]==[1,1,4,5,1,4]

'''
s=[1,2,3]
print(id(s))
s*=2
print(id(s))
# python内每一个对象都有三个基本属性：唯一标志，类型，值
#   唯一标志是对象创建时就有的，不可修改，不可重复，相当于对象的身份证
#   id() 就是返回对象的身份代表的整数值

t=(1,2,3)
print(id(t))
t*=2
print(id(t))  # 和之前的id值不一样了

# is  is not 用于检测id值，输出布尔数值
x,y=[1],[1]         # 列表就不是同一个对象
z,w=(1,),(1,)       # 元组是同一个对象
print(x is y,z is w)

# in     not in 判断是否是包含关系，左边是否是右边的子集
print('你'in'你好','你'not in '你好')

# del 用于删除指定的对象
# del x，y    x列表就不再存在了，y元组也不存在了
# del 还可以进行一定步骤删除，而列表切片则会报错

q=[1,1,4,5,1,4]
del q[-1]          # 和q[-1]=[]相同
print(q)

w=[1,1,4,5,1,4]
del w[::2]         # 每隔2个序号数 进行 del
print(w)

e=[1,1,4,5,1,4]   # e.clear() 就会清空列表内所有元素
del e[::]
print(e)

# 和序列相关的一些函数
# 列表，元组，字符串的相互转化函数
# list()  tuple()  str()

r=list('114514')
t=tuple('114514')
u=str([114514])
print(r,'\n',t,'\n',u)

# min    max 对比传入的参数，返回最大值和最小值
i=min('123')
print(min(i))
# min(对象,default='sss') 如果找不到，就会返回default中指定的内容

# len() 求长度 最大值不会超过 2^64-1
# sum() 求和
print(sum(w),sum(w,start=-5))  # start= 就是sum从多少开始求和

# sorted()  可接受任何可迭代的对象作为参数
# .sort() 只能将列表进行排序
# reversed()  返回参数的反向迭代器,可用list() tuple str 再把迭代器变回指定的序列
o=[1,1,4,5,1,4]
print(sorted(o),o)  # 从小到达排序，返回一个全新的列表，原来列表不受影响

print(sorted(o,reverse=True))  # 排序后进行翻转

f=['12','niu','hao','nihao']
print(sorted(f,key=len),'\n',sorted(f))

print(list(reversed(o)))
print(list(reversed(range(0,10)))) # 0-9,的倒过来，再变为列表

# all()  可迭代序列中任意元素是否为真
# any()  可迭代序列中存在元素是否为真
print(all([1,0,1]),any([1,0,1]))

# enumerate()
# 创建一个序列的枚举对象
# 还有start参数，可以指定第一个序号从哪开始
seasons=['spring','summer','autumn','winter']

print(list(enumerate(seasons)))
print(list(enumerate(seasons,1)))

# zip()
# 用于创建一个聚合多个可迭代对象的迭代器
# 它会将 作为参数传入的 每个可迭代对象 的每个元素，依次组成元组
# 即第i个元组包含来自每个参数的第i个元素

num_1=[1,2,3]
num_2=[4,5,6]
num_3=[7,8,9]
num_4=[10,11]
zipped=zip(num_1,num_2,num_3,num_4)  # 按照len最小的序列组合，多余的就舍弃了
print(list(zipped))

import itertools
zipped2=itertools.zip_longest(num_1,num_2,num_3,num_4)  # 导入itertools，这样就不会舍弃多余的
print(list(zipped2))


# map()
# 会根据提供的函数对指定的可迭代对象的每个元素进行运算
# 并返回运算结果的迭代器
# map(计算方法,传入第一个对象 )

mapped=map(ord,'Hello ') # ord 求出字符的unicode编码，
print(list(mapped))

mapped2=map(pow,[1,2,3],[10,3,0])  # pow 指数计算函数 相当于pow(1,10) pow(2,3)
                                   # 每次拿第一个序列的 序号0 和后面的 序列的序号 0进行计算
print(list(mapped2))

mapped3=map(max,[1,2,3],[10,3,0],[2,2])  # 最后一个序列最短，一共只会比较2次max
print(list(mapped3))


# filter()
# 过滤器的意思
# 会根据提供的函数对指定的可迭代对象的每个元素进行运算
# 并将运算结果为真的元素，以迭代器的形式返回

fi=list(filter(str.islower,'Hello'))  # 由于H大写，所以就不会返回了，只有 ello被返回
print(fi)

# 可迭代对象，比如序列，是可以进行重复的适用
# 迭代器只能用一次

num_5,num_6=[1,1,4],[5,1,4]
zipped4=zip(num_5,num_6)    # 这个zipped4 成为了 num_5 num_6 的zip后的迭代器
for i in zipped4:
    print(i,end=' ')        # 这里已经适用过 zipped4 了
print()
print(list(zipped4))        # 所以这里再适用zipped4 就已经为 None了


# iter()
# 可以将 可迭代对象 列表、元组、字符串 转变为 迭代器(一次性的)
num_7=[1,1,4,5,1,4]
g=iter(num_7)
print(type(g),type(num_7))

# next()
# 逐个将迭代器 iterator 中的元素 提取出来，每次取一个，原来的迭代器就会少掉那一个
# 当迭代器中所有元素都被next() 取出时，再取就会出异常

# next(迭代器,'没啦！') 可以在元素全部被提取之后，返回 ,后面的东西，不再出异常
h=iter(num_7)

