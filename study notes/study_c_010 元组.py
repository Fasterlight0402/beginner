# 元组 (元素1,元素2，元组……)

rhyme=(1,2,3,4,"上")

# 元组也可以用切片
# 元组不可变，修改元组的行为是不可取的
# rhyme[0]=2  则会报错

# 元组可以用切片导出
a,b=rhyme[:3],rhyme[3:]
print(a,b)

"""
元组只支持查   
.count()   查找某个元素出现几次
.index()    查找某个元素第一次出现的序号
nums=(1,1,3,4,5,3,2,1,4)

nums.count(1)
nums.count(-2)
nums.index(4)

"""
s=(1,2,3)
t=(4,5,6)
q=s+t           # t会接在s的后面
print(q)

p=s*3           # s元组会重复3次
print(p)

w=s,t           # s和t元组嵌套在w元组内
print(w)

for each in w:
    print(each)  # 元组也支持迭代

for each in w:
    for i in each:   # 元组也支持嵌套循环
        print(i)

r=(1,3,5,7)
y=[i*2 for i in r]  # 可以用元组推导式生成新的列表
print(y)

# z=(i*2 for i in r) # 没有元组推导式这种东西，这个是生成器

x=(512,) # 这样才是生成只有一个元素的元组
c=(512)  # 这样生成的变成了int

print(type(x))   # tuple 元组类型
print(type(c))   # int 整数类型

# 生成一个元组也叫做元组的打包
h=(123,"123",1.23)
g,k,j=h             # 将元组内的东西赋值给几个东西，叫做解包
print(g,k,j)        # 赋值等号最后变量数量要相等

nu,ni,*no="Lord"

# 虽然元组本身不可变，但元组内被指向的是列表则依然可以被改变
ns=[1,1,3]
nm=[5,1,4]
nw=(ns,nm)
nw[0][2]=4
print(nw)


