# 0. 请问下面代码会打印 True 还是 False 呢？
# s1 = set([1, 1, 2, 3, 5])
# s2 = frozenset([1, 1, 2, 3, 5])
# s1 == s2
#
#   False

# 1. 既然有了 set() 集合，为什么还要创造 frozenset() 来冻结集合（换句话说，frozenset() 的优势是什么）？
#
#   frozenset() 不可被修改，可以在集合中创建集合

# 2. 集合中，difference(*others) 和 difference_update(*others) 这两个方法都是用于计算差集，那么它们有什么区别呢？
#
#   前者是返回一个新的集合，后者是修改原本的集合


# 3. 由于 frozenset 对象是不可修改的，所以我们说它也是可哈希的，对吗？
#
#   是

# 4. 请问集合对象的 update(*others) 方法和 add(item) 方法有什么不同？
#
#   update()可以加多个对象，并且会被分解， add()加的是变成作为整体的元素


# 5. 请问集合对象的 remove(elem) 方法和 discard(elem) 方法有什么不同？
#
#   remove()找不到会 error   discard()找不到会静默处理


# 6. 请问下面代码输出的内容是什么？
# >>> {x for x in 'FishCChsiF' if x not in 'ish'}
#
#   {'C','F'}


# 动动手：
# 0. 最开始的时候，Python 是没有 set() 的，那么当时伟大的程序猿是如何实现 “集合” 这个的概念呢？
# 现在我们将时间回拨到那个 “一穷二白” 年代，现在大家没有 set() 可用了，只能利用 dict() 来实现交集和并集。
# 题目要求：
#   生成一个随机数列表，一共有 100 个元素，每个元素取 1~100 的随机值，赋值给变量 x
#   生成另一个随机数列表，一共有 100 个元素，每个元素取 50~150 的随机值，赋值给变量 y
#   利用字典的 “键” 不会重复的特点，计算 x 和 y 的交集（就是两者共有的元素）

import random

x=dict.fromkeys([random.randint(1,100) for i in range(100)])
y=dict.fromkeys([random.randint(50,150)for j in range(100)])

p={k:None for k in x.keys() if k in y.keys()}
print(p)


# 1. 破解 MD5 哈希加密！！
# 虽然说单向哈希加密是无法逆向，但聪明的黑客们想出了彩虹表破解法：
# 彩虹表是一个用于加密散列函数逆运算的预先计算好的表，常用于破解加密过的密码散列。
# 彩虹表常常用于破解长度固定且包含的字符范围固定的密码（如信用卡、数字等）。
# 这是以空间换时间的典型实践，比暴力破解（Brute-force attack）使用的时间更少，空间更多；
# 但与储存密码空间中的每一个密码及其对应的哈希值（Hash）实现的查找表相比，其花费的时间更多，空间更少。

# 说人话就是：所谓的彩虹表，其实就是将所有可能的字符串组合都给预先哈希一遍，
# 然后将映射结果保存起来，当黑客拿到一个哈希值时，通过查表的方式获取密码明文。

# 题目要求：
# 生成 0~999999 所有整数组成密码的哈希值
# 将上面生成的哈希值保存为映射类型
# 通过查表的方式，计算下面 3 个哈希值对应的明文密码
# 021bbc7ee20b71134d53e20206bd6feb
# e10adc3949ba59abbe56e057f20f883e
# 655d03ed12927aada3d5bd1f90f06eb7

# 友情提示：
# hashlib.md5() 的参数是需要一个 b 字符串（即 bytes 类型的对象），
# 这里可以使用 bytes("123", "utf-8") 的方式将 "123" 转换为 b"123"。

import hashlib
k=dict()
mm=['021bbc7ee20b71134d53e20206bd6feb','e10adc3949ba59abbe56e057f20f883e','655d03ed12927aada3d5bd1f90f06eb7']

for i in range(1000000):
    p=bytes(str(i), "utf-8")
    o=hashlib.md5(p).hexdigest()
    k[i]=str(o)

anti_k={j:i for i,j in k.items()}       #   这里创建了一个键值对反过来的 字典，其实可以创建k的时候，就把键值对反过来
for i in range(len(mm)):
    print(mm[i],'对应:',anti_k[mm[i]])
