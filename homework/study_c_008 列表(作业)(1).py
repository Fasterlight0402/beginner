# 有列表 name = ['F', 'i', 'h', 'C']，
# 如果小甲鱼想要在元素 'i' 和 'h' 之间插入元素 's'，
# 应该使用什么方法来插入？

name = ['F', 'i', 'h', 'C']
name.insert(2,'s')
print(name)

# 假设给定以下列表：
# member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
# 要求将列表修改为：
# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

# 方法一：使用 insert() 和 append() 方法修改列表。
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']

member.insert(1,'88')
member.insert(3,'90')
member.insert(5,'85')
member.insert(7,'90')
member.insert(9,'88')
print(member)

# 方法二：重新创建一个同名字的列表覆盖。
name_1=['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
name=name_1.copy()

# 利用 for 循环打印上边 member 列表中的每个内容
for i in range(len(member)):
    print(member[i])

print()

# 上一题打印的样式不是很好，
# 能不能修改一下代码打印成下图的样式呢？【请至少使用两种方法实现】
for j in range(len(name)):
    if j%2==0:
        print(name[j],end=' ')
    else:
        print(name[j])

print()

k=0
length=len(name)
while k <= length-1:
    if k%2==0:
        print(name[k],end=' ')
    else:
        print(name[k])
    k+=1

print()

# 参考答案的方法
for l in range(len(name)):
    if l%2==0:
        print(name[l],name[l+1])  #  print(,) 直接同时打印一排两个东西

