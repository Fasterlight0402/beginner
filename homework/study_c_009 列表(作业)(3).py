_=[[123],'123',123]
print(_)

# 获取列表的最后一个元素
# length=list1[len(list1)-1]  或者 length=list1[-1]

z=[1,2,3,4,5]
print(z[:3])    # 打印序号3之间的元素

print(z[::2])   # 全部元素中，序号每隔2个的元素


x=[5, "上", 4, "山", 3, "打", 2, "老", 1, "虎"]
print(x[-2::-2])    # 从序号-2 开始，每隔-2个序号的元素 ，就是每次倒着数2个

# 请问如何将 list2 列表中的全部元素，添加到 list1 列表中第 2 和第 3 个元素的中间
list1 = [1, 2, 8, 9]
list2 = [3, 4, 5, 6, 7]

list1[2:2]=list2
# 在序号2到序号2间插入list2，就是多加了一个序号2的子集，原本的序号2变成序号3
print(list1)


# 如给定的列表 nums = [2, 7, 11, 15]，
# 目标值 target = 9，
# 那么由于 nums[0] + nums[1] = 2 + 7 = 9，所以打印结果是：[0, 1]
nums = [2, 7, 11, 15]
nums_9=[]
length=len(nums)
for p in range(4):
    for q in range(4):
        if nums[p]+nums[q]==9:
            nums_9=[p,q]
print(nums_9)

# 学习过的 random 模块，生成一个由 10000 个整数（范围是 1 ~ 65535）构成的随机列



# _ 暂存的变量，可修改

# 请使用列表推导式创建一个 4 * 5 的二维列表，并将每个元素初始化为数字 8
ma1=[[8]*4 for i in range(5)]
print(ma1)

# 请将下面列表推导式还原成循环语句的实现形式
# result = [i / 2 for i in range(10) if i % 2 == 0]
result=[]
for i in range(10):
    if i%2==0:
        result.append(i)
print(result)

# 3请将下面的嵌套循环语句使用列表推导式实现
"""
result = []
for x in range(10):
     if x % 2 == 0:
         for y in range(10):
             if y % 2 != 0:
                 result.append([x, y])
"""

result_1 = [[x,y] for x in range(10) if x%2==0
                  for y in range(10) if y%2!=0]
print(result_1)

# 4请将下面 matrix 矩阵反向展开，即使得最终的结果为 [9, 8, 7, 6, 5, 4, 3, 2, 1]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rhyme=matrix[::-1]
flatten=[rhyme[i][2-j] for i in range(3)
                       for j in range(3)]
print(flatten)

# 参考答案更简单 ： flatten = [col for row in matrix for col in row][::-1]


# 5.供了有 2 种颜色（"BLACK", "WHITE"）和
# 10 个码数（"WS", "WM", "WL", "S", "M", "L", "XL", "2XL", "3XL", "4XL"）的
# 请使用列表推导式统计所有颜色和尺码的组合

colors = ["BLACK", "WHITE"]
sizes = ["WS", "WM", "WL", "S", "M", "L", "XL", "2XL", "3XL", "4XL"]

length1=len(colors)
length2=len(sizes)

clo=[[colors[i],sizes[j]] for i in range(length1)
                          for j in range(length2)]

print(clo)


# 动动手0
# 请使用列表推导式，获得 matrix 矩阵的转置矩阵 Tmatrix
# （将 matrix 的行列互换之后得到的矩阵，称为 matrix 的转置矩阵）

# 什么是转置矩阵？
# 一个矩阵 matrix，把它的第一行变成第一列，第二行变成第二列，……，最末一行变为最末一列，
# 从而得到一个新的矩阵 Tmatrix。这一过程称为矩阵的转置

matrix03 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]

hang=len(matrix03[0])
lie=len(matrix03)

Tmatrix03=[[matrix03[i][j]  for i in range(lie)]
                            for j in range(hang)]
print(Tmatrix03)

# 动动手1
# 请按照顺时针螺旋顺序输出矩阵中的所有元素 spiral
matrix04 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
         [9, 10, 11, 12]]

left,chang=0,len(matrix04[0])
top,gao=0,len(matrix04)

spiral=[]
while left<chang and top<gao:
    for i in range(left,chang,1):
        spiral.append(matrix04[top][i])  # 从左往右
    top+=1

    for i in range(top,gao,1):
        spiral.append(matrix04[i][chang-1])  # 从最右的上+1到 最下
    chang-=1

    if left>=chang or top>=gao:
        break

    for i in range(chang-1,left-1,-1):
        spiral.append(matrix04[gao-1][i])  # 从gao-1 个的 倒数第二个往左
    gao-=1

    for i in range(gao-1,top-1,-1):
        spiral.append(matrix04[i][left])  # 从 高-1行 到 top+1 行
    left+=1

print(spiral)


# 动动手2   举一反三
# 请按照逆时针螺旋顺序输出矩阵中的所有元素 spiral02

matrix05 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
         [9, 10, 11, 12]]

spiral02=[]

zuo,you=0,len(matrix05[0])
shang,xia=0,len(matrix05)

while zuo<you and shang<xia:
    for i in range(you-1,zuo-1,-1):
        spiral02.append(matrix05[shang][i])
    shang+=1

    for i in range(shang,xia,1):
        spiral02.append(matrix05[i][zuo])
    zuo+=1

    if shang>=xia or zuo>=you:
        break

    for i in range(zuo,you,1):
        spiral02.append(matrix05[xia-1][i])
    xia-=1

    for i in range(xia-1,shang-1,-1):
        spiral02.append(matrix05[i][you-1])
    you-=1

print(spiral02)

