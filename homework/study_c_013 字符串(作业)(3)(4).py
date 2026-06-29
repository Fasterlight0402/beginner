#3
# 0. 请问下面代码执行的结果是？
# x = "我爱Python"
# x.startswith(["你", "我", "她"])
# 会报错，类型不对，支持元组类型

# 1. 请问下面代码执行的结果是？
# "I love FishC\s".isprintable()
# 会报错，无效转义符

# 2. isdecimal()、isdigit() 和 isnumeric()
# 这 3 个方法都是判断数字的，那么请问这其中哪一个方法 “最严格”，哪一个又是 “最宽松” 的呢？
#
# isdecimal()只能十进制数，最严   isnumeric()最宽松


# 3. 请问下面代码执行的结果是？
print("一二三四五上山打老虎".isalnum())  # 判断是否为纯数字和字母，汉字也视作字母
# True


# 4. 请使用一行代码判断 s 字符串中，是否所有字符都是英文字母？
#
#s.isalpha()


# 5. 请问下面代码执行的结果是？
#
print("一二三木头人".isidentifier())
#True

# 动动手：
# 0. 给定一个字符串 text 和字符串列表 words，返回 words 中每个单词在 text 中的位置（要求最终的位置从小到大进行排序）。

# 举例：
# text："I love FishC and FishC love me"
# words："FishC"
# 输出：[[7, 11], [17, 21]]

# text："I love FishC and FishC love me"
# words："FishC love"
# 输出：[[2, 5], [7, 11], [17, 21], [23, 26]]

# text："FCFCF"
# words："FCF FC"
# 输出：[[0, 1], [0, 2], [2, 3], [2, 4]]

# 程序实现如下：
# 提示：分割字符串可以使用 split() 实现，按空格进行分割即 words = words.split()

text=input('请输入text的内容:')
words=input('请输入words的内容:')
k,h=[],[]

def serial(i):
    length=len(i)
    for j in range(len(text)-length+1):
        if text[j:j+length]==i:
            k.append([j,j+length-1])
    return k

words=words.split()
for j in words:
    h=serial(j)

for i in range(len(h)-1):        # 大小交换顺序
    if h[i][0]>h[i+1][0]:
        h[i],h[i+1]=h[i+1],h[i]
print(h)
'''
参考答案：
text = input("请输入text的内容：")
words = input("请输入words的内容：")
words = words.split()
    
result = []
for each in words:
    temp = text.find(each)
    while temp != -1:
        result.append([temp,temp+len(each)-1])
        temp = text.find(each, temp+1)
    
print(sorted(result))

'''

# 1. 编写一个程序，判断输入的字符串是否由多个子字符串重复多次构成。
# 输入："FCFC"
# 输出：True

# 输入："FishCFishc"
# 输出：False

# 提示：如果一个长度为 n 的字符串 s 可以由它的一个长度为 i 的子串 t 重复多次构成，那么必须要满足以下条件：
# n 一定是 i 的倍数
# t 一定是 s 的前缀子字符串
# n 除以 i 的结果必定是 t 在 s 中出现的次数

lib,lib2=[],[]
def zimu(x,y):
    lib.clear()
    for i in range(0,len(y)-len(x)+1,len(x)):
        if x!=y[i:i+len(x)]:
            go='False'
        else:
            go='True'
    lib.append(go)
    return lib

letters=input('请输入一个由字母构成的字符串：')
length=int(len(letters)/2)
for i in range(1,length+1,1):
    k=set(zimu(letters[0:i],letters))
    if k.intersection({'False'}):
        lib2.append('False')
    else:
        lib2.append('True')

if lib2.count('True')!=0:
    print(True)
else:
    print(False)

'''
参考答案：
s = input("请输入一个由字母构成的字符串：")
    
n = len(s)
for i in range(1, n//2+1):
    # 如果子字符串的长度为i，则n必须可以被i整除才行
    if n % i == 0:
        # 如果子字符串的长度为i，则i到i*2之间是一个重复的子字符串
        if s.startswith(s[i:i*2]) and s.count(s[i:i*2]) == n/i:
            print(True)
            break
# for...else的用法，小甲鱼希望大家还没有忘记哦^o^
else:
    print(False)

'''

#4


