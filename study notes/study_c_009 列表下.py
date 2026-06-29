x=[1,2,3]
y=x
#  当x赋值给y时，是将y应用x的数据

# 浅拷贝
z=x.copy()
k=x[:]

p=[[1,2,3],[4,5,6],[7,8,9]]
q=p.copy()

p[1][1]=0
print(p)
print(q)                    # q的[1][1]也被改变了，所以还是会有影响

import copy
#导入copy模块
i=[[1,2,3],[4,5,6],[7,8,9]]
o=copy.deepcopy(i)          # 深层拷贝
i[2][2]=0
print(i)
print(o)                    # 这时候的列表o就不会被改变了，常用浅拷贝为了效率

# 什么是方法   什么是函数，在学类之前可以认为是一样的

# 列表推导式
oho=[1,2,3,4,5,6,7]
for i in range(len(oho)):
    oho[i]=oho[i]*2
print(oho)                   # 可以把oho中每个元素变为两倍

hoo=[1,2,3,4,5,6,7]
hoo=[i*2 for i in hoo]       # 列表推导式，效率比循环语句高一倍左右
print(hoo)

# [存放的元素 for 数值 in 函数 ]
ooh=[i for i in range(10)]
print(ooh)

# 相当于以下：
"""
ooh=[]
for i in range(10):
    ooh.append(i+1)
"""
"""
y=[c*2 for c in 'yihe']
y==['yy','ii','hh','ee']

code = [ord(c) for c in 'yihe']  # 将'yihe'对应的字符串转化成编码
"""

code = [ord(c) for c in 'yihe']  # 将'yihe'对应的字符串转化成编码
print(code)                      # 输出对应的编码


matrix=[[1,2,3],                # 矩阵列表
        [4,5,6],
        [7,8,9]]
co12=[row[1] for row in matrix]  # 提取矩阵的每个子集，再提取每个子集的序号1的元素
print(co12)

diag=[matrix[i][i] for i in range(len(matrix))] # 取出矩阵的对角线的元素为一组

diag_1=[matrix[i][2-i] for i in range(len(matrix))]  # 取出矩阵的右向左下斜的数据

# 利用列表推导式创建二维列表
S=[[0]*3 for i in range(3)]  # 这里的i并不需要新的定义
print(S)

#[元素或子集 for i in 函数 if 筛选条件 ]
even=[i for i in range(10) if i%2==0]  # 筛选出0-9之间的所有偶数  even number - 偶数
#  先执行for 再执行 if  最后再是开头的赋值


# 练习 筛选出F开头的单词
words=['Great','Well','Fish','Fantastic']

words_F=[words[i] for i in range(len(words)) if words[i][0]=='F' ]
print(words_F)
#   修改后代码  words_F=[w for w in words if w[0]=='F']

# 嵌套的列表推导式
# [元素或子集 for 目标1 in 函数1
#           for 目标2 in 函数2
#           for 目标3 in 函数3]

mx=[[1,2,3],[4,5,6],[7,8,9]]
flatten =[col for row in mx       # row 是mx 的每一个子集
              for col in row]     # col 又是 cow 中的每一个元素
print(flatten)

mi=[x+y for x in'DAEK' for y in 'dark']
print(mi)

# 嵌套列表推导式的终极用法，每个循环后面接上一个条件判断语句
# [元素或子集 for 目标1 in 函数1 if 条件1
#           for 目标2 in 函数2 if 条件2
#           for 目标3 in 函数3 if 条件3]

mm=[[x,y] for x in range(10) if x%3==0
          for y in range(10) if y%2==0]
print(mm)

# 程序 KISS 原则  Keep It Simple & Stupid  弱保软，尽量简洁易懂
