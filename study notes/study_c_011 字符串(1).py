# 用字符串检验回文数字
x=input('请输入数字')
if x==x[::-1]:
    print('是回文数')
else:
    print('不是回文数')


# 字符串方法①
# 大小写字母换来换去方法
# capitalize()  casefold()  title()  swapcase()  upper()  lower()

z='I Love World'
print(z.capitalize()) # 首字母大写，其他变为小写，生成新的字符串

print(z.casefold())   # 所有字母都是小写，也适用非英语

print(z.title())      # 将每个单词首字母大写，其他字母都变成小写

print(z.swapcase())   # 将所有字母的大小写反转

print(z.upper())      # 将所有字母变成大写

print(z.lower())      # 将所有字母小写，只能处理英语



# 字符串方法②
# 左中右对齐
# center(width,fillchar='')    lijust()   rjust()  zfill()
# width 字符串的指定宽度，如果输出宽度<=原字符串，则输出原本字符串
# fillchar 填充，不输入默认为空格

y='有内鬼，停止交易！'  # 字符串宽度为9
print(len(y))
print(y.center(5))  #  输入宽度小于原来的，输出原本字符串

print(y.center(15)) #  左右会用空格输出

print(y.rjust(15))  #  右对齐

print(y.ljust(15))  #  左对齐

print(y.zfill(15))  #  用0填充左侧

print(y.center(15,'/'))  # 用/ 填空空余部分



# 字符串方法③
# 查找
# count(目标[,start[,end]])
# find()  rfind() index() rindex()

v='我一把把把把住了'

print(v.count('把'))  # 查找'把'字符串出现的次数，输出4

print(v.count('把',0,5))  # 查找字符串序号0到序号5之间'把'出现次数

print(v.find('把'))  # 从左往右，找到'把'，输出第一个找到的序号数 与index()类似
print('1')
print(v.rfind('把')) # 从右往左，找到'把'，输出第一个找到的序号数 与rindex()类似

print(v.find('车'))  # 找不到则输出 -1，  用index('车')则会error



# 字符串方法④
# 替换
# expandtabs([tabsize=8])   replace(old,new,count=-1)  translate(table)

code='''
    print('114')
    print('514')
'''

new_code=code.expandtabs(4)  # 将字符串中的所有 tab空格 转化为 space空格，1 tab =4 space
print(new_code)

code1='你好！你好！你好！'
code2=code1.replace('！','？')  # 最后还可以 ,次数 指替换几次，默认 -1 全部替换
print(code2)

table=str.maketrans('ABCDEFG','1234567')  # 意思是A对应1，B对应2 等等一类的一种表格
print("2B2C2B2F".translate(table))        # 将"2B2C2B2F"运用刚刚的table表格方法输出

table1=str.maketrans('ABCDEFG','1234567','2B') # 最后代表表格忽略掉'2''B'
print("2B2C2B2F".translate(table1))            # 所有的'2'和'B'都不会被转换输出了

# 字符串方法⑤
# 判断  以下都返回布尔类型 True False
# startswith(prefix[,start[,end]])   endswith(suffix[,start[,end]])
# isupper()    islower()  istitle()  isalpha()  isascii()  isspace()
# isprintable()  isdecimal()  isdigit()  isnumeric()  isalnum()  isidentifier()


print(v.startswith('我'))  # startswith用于判断参数指定的子字符串是否出现在字符串的起始位置

print(y.endswith('！'))   # endswith用于判断参数指定的子字符串是否出现在字符串的末尾位置

print(v.startswith('我',1))  # 从元组序号1 开始找，所以输出False

a='她爱Python'
if a.startswith(('你','我','她','他')):  # startswith endswith 支持查询元组，只要元组中有一个元素符合，就True
    print('总有人喜欢Python')

print(z.istitle())  # 每个单词开头字母大写，则返回 True

print(z.isupper())  # 所有字母都是大写，则返回True

print(z.upper().isupper())  # 多个函数，从左往后依次进行，先全部变成大写，再检测是否全是大写

print(z.islower())  # 所有字母都是小写，则返回True

print(z.isalpha())  # 字符串全都是字母组成，则返回True，因为有 空格，所以为False

print(z.isspace())  # 字符串是空字符串 空格或者tab ，则返回True

print(z.isprintable())  # 字符串中所有内容可打印，则返回True    而\n 这类转义字符是不可打印的

x_1='12345'
x_2='ⅠⅡⅢⅣ'
x_3='一二三四五'
x_4='壹贰叁肆伍'
x_5='onetwothreefourfive'

print(x_1.isdecimal(),x_2.isdecimal(),x_3.isdecimal(),x_4.isdecimal(),x_5.isdecimal())
# isdecimal只用于最简单的十进制数字

print(x_1.isdigit(),x_2.isdigit(),x_3.isdigit(),x_4.isdigit(),x_5.isdigit())
# isdigit范围稍微大一点

print(x_1.isnumeric(),x_2.isnumeric(),x_3.isnumeric(),x_4.isnumeric(),x_5.isnumeric())
# isnumeric范围最大
# isalnum()是集大成者，前三者任意一个为True，便为True

print('I am rich'.isidentifier()) # isidentifier() 用于检测字符串是否是合法的变量名
print('I_am_rich'.isidentifier()) # _ 可以，所以为True

import  keyword
print(keyword.iskeyword('until'))  # 判断字符串是否是Python的内置保留标识符
