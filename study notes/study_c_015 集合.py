# set() 集合中所有元素都是独一无二的，都是无序的

# 创建集合
#  ① {'114','514'}

#   ②集合推导式
k={k for k in "114514"} # 不能重复，以及无序
print(k)

#   ③类型构造器
l=set('114514')
print(l)

#   由于集合的无序性，所以 l[0] 结果是error

#   集合可以用 in    not in  进行判断

# 访问集合的元素
for i in l:
    print(i,end=" ")

# 集合可以很方便地进行去重
j=[1,1,4,5,1,4]

# len(j)==len(set(j))  这样可以方便地判断列表中是否有重复

# 集合的方法
#   不会对集合内容产生改动的方法

#   ①浅拷贝 .copy()
h=set(j).copy()
print(h)

#   以下()中可以多参数的
#   ②判断是否有交集 .isdisjoint()   只要传入可迭代对象即可   .前面  和() 里判断是否有交集

print(h.isdisjoint(set(l)))  # 如果为True 说明两个集合没有相同元素  为False 至少有1个相同的元素 判断是否有交集

#   ③判断是否为子集  .issubset()   .前的 是否 是() 里的子集
print(l.issubset('1234567'))

#   ④判断是否是超集，也就是反过来的子集  .issuperset()   ()里的 是否是 .前的子集
print(l.issuperset('14'))

#   ⑤并集  .union()   将.前的集合 和 () 中的集合 组成并集
print(l.union({'96','99','1'}))

#   ⑥交集   .intersection()   返回一个新集合 是 .前的集合 和() 中的集合 的交集
print(l.intersection({'96','99','1','4'}))

#   ⑦差集   .difference()   返回一个新集合 是 .前的集合 比()中的集合 多出来的集合
print(l.difference({'96','99','1','4'}))

print(l.difference({'96','99','1','4'},'1','5'))  # 这样出来的就是空set了

#   下面这个方法不能多参数
#   ⑧对称差集   .symmetric_difference   返回一个新集合 是 .前 和集合 ∪ ()里的集合，再 减去  .前和集合 ∩ ()的集合
print(l.symmetric_difference('546'))    # 所以只剩1,6了


# 集合 set 的运算符号

#   运算符两边必须是集合类型才行
#   <=  检测 左 是否是 右 的子集
print(l<=set('12345'))

#   <   检测 左 是否是 右 的真子集
print(l<set('114514'))

#   >=  检测 右 是否是 左 的子集

#   >   检测 右 是否是 左 的真子集

#   |   (在backspace 的下面) 管道符   将左右组合成并集
print(l|set('114514')|set('abc'))

#   &   返回 左集合 ∩ 右集合
print(1111,l&set('5678'))

#   -   返回左边集合 比 右边集合 多出来的集合  差集
print(l-set('4567'))

#   ^   返回  左∪右 -  左∩右  对称差集
print(l^set('567'))

'''
///////////////////////////////////////////////////
'''
# 集合分为可变对象 set()    与不可变对象 frozenset()
# 创建
q=frozenset('114514')  # 集合q就不可被修改了

#   集合方法
#   会对集合中的内容产生改动的方法

w=set('xb1234')
print(w)
e=set('1999')

#   .update()  把 .前的集合 改变为 它与()中集合的并集
w.update(e)
print(w)

#   .intersection_update()   把 .前的集合 改变为  它与()中集合的交集
w.intersection_update(e)
print(w)

#   .difference_update()   把  .前的集合 变更为  它与()中集合的差集
w.difference_update(e)
print(w)

#   .symmetric_difference_update  把  .前的集合 变更为 它与()中集合的对称差集
w.symmetric_difference_update(e)
print(w)

#   .add()  将() 中的元素 添加到 .前面的集合中
w.add('114514')  #  传入的字符串将作为整个元素，并不会被分割
print(w)

#   .remove()    删除 set 中的某个元素，如果不存在，会error
#   .discard()    删除 set 中的某个元素，如果不存在，则静默处理


#   .pop()  随机弹出一个集合中的元素，原来集合中会失去这个元素
print(w.pop(),w)

#   .clear()    清空集合，变为 空集

# 可哈希
#   hash()  获得() 中对象的哈希值
#   dict的键key   tuple  str  set里的元素elem  frozenset()  这些不可变，都是可哈希
#   list 一直可变，就是不可哈希
#   set 也是可变的容器，也不可哈希

print(hash(1),hash(1.000),hash(1.001))  #   整数的哈希值就是其本身,相等值的数字 哈希值相等

x={1,2,3}
x=frozenset(x)
y={x,4,5,6}
print(y)  # 这样就可以在集合里 创建 集合了

a=[1,1,2,3]
b=set(a)
print(b)

