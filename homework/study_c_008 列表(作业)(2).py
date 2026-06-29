"""""'''
'''"""""
'''
a=list1[2:5]
print(a)

b=list1[0]      # 提取的是列表 序号0 的元素
c=list1[0:1]    # 提取的是列表 序号0-序号1 之间的列表
print(b,c)

'''

list1 = [1, 3, 2, 9, 7, 8]
print(list1)
list3=list1[:]

list1_dao = list1[-1:]
list1_sheng=list1.pop()     # 删除最后一位，并访问被删除的元素，不是列表

print(list1_sheng)
'''
list1=list1_dao+list1_sheng
print(list1)

'''


# 参考答案的方法
list3.insert(0,list3.pop())  # 删除末尾，把末尾插入序号0位置
print(list3)

