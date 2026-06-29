# 字符串方法⑥
# 截取
# lstrip(chars=None)   strip(chars=None)  rstrip(chars=None)
# removeprefix(prefix) removesuffix(suffix)

print('         左边空着干嘛'.lstrip())   # 去掉字符串左侧的空白
print('右边空着干嘛          '.rstrip())  # 去掉字符串右侧空白
print('     两边空着干嘛     '.strip())     # 去掉字符串左右的空白

print('www.bilibili.com'.strip('.wcom'))  # 将'.''w''c''o''m'这几个字符串全部去掉

print('www.bilibili.com'.removeprefix('www.'))  # 将前缀的'www.'去除

print('www.bilibili.com'.removesuffix('.com'))  # 将后缀的'.com'去除


# 字符串方法⑦
# 拆分和拼接
# partition(sep) rpartition(sep) 将字符串以参数为指定的分割符为依据进行切割，并且将返回切割后的三元素元组
# split() 切割   splitlines()
# '拼接符号'.join(列表或者元组) 拼接


print('www.bilibili.com'.partition('.'))   # '.'前，'.'本身，还有'.'后，分成三段，序号数最小的'.'为分界线

print('www.bilibili.com'.rpartition('.')) # 序号数最大的'.'为分界线，

print('www bilibili com'.split())  # 默认将字符串中的 空格 分割，打碎放到一个列表中

print(1,'www.bilibili.com'.split('.'))  # 将字符串中'.'去掉，然后打碎，放到一个列表中

print('www.bilibili.com'.split('.', 1)) # 从左往右，分割 1 次
print(2,'www.bilibili.com'.rsplit('.', 1)) # 从右往左，分割 1次

print('www\nbilibili\ncom'.splitlines())  # 按换行将字符串分割

print('www\nbilibili\ncom'.splitlines(True))  # 换行符本身也放入列表中


print('.'.join(['www','bilibili','com']))  # 将列表或元组中的几个片段字符串用'.'从左往右拼接起来,返回字符串
print('^'.join(('www','bilibili','com')))

y='bili'
y=''.join((y,y))  # 用join将字符串进行拼接，比+=拼接有更高的效率
print(y)

# 字符串方法⑧
# 格式化
#   .format()
#  [[fill]align] [sign] [#]          [0]  [width] [grouping_option] [.precision] [type]
# 填充的东西 对齐方式       添加进制的前缀       字符宽度                   精度或截取     输出类型

year=2026
print('今年是{}年'.format(year))   # 用{}占用一个坑位，后面调用format括号中的方法

q='{}一看到，{}就很……'.format('别人','我')
print(q)
q_1='{1}一看到，{0}就很……'.format('别人','我') # {}中的数字代表format后元组中的元素序号数，但不能有负数
print(q_1)

print('{},{{}},{}'.format(1,2))  # 想单纯打出大括号就用{{}}，或者format中有{}注释

w='{1:>10}{0:<10}'.format(514,114)
# {元素序号数：对齐方式 字符串宽度}
print(w)

print('{:04}'.format(10))
print('{:04}'.format(-10))
print('{:0<10}'.format('你好'))
# {默认元素 ： 用0填充空白 一共4个符号宽度}，负号会被自动识别,format中的元组默认右对齐

print('{:%<5}'.format('你好'))  # 用%代替0进行填充
print('{:%>5}'.format('你好'))

print('{:+}{:-}'.format(10,-11)) # 会多+ 表示正数，负数会多-表示(默认的)

print('{:,}'.format(114514),'{:_}'.format(114514))   # 在10³处 使用, 或者用_ 代表千分位符

print('{:.3f}\t'.format(3.14159),'{:.3g}'.format(3.14159))
# .3f 代表保留小数点后3位，四舍五入    .3g 代表一共保留3位有效数字，四舍五入

print('{:.6}'.format('The World!'))
# .6 代表字符串一直截取到 序号5 的元素，空格也是一位元素，不能对纯数字使用，会报错

# 对int数字类的处理
# b 以二进制输出
# c 以Unicode字符的形式输出
# d 以十进制输出
# o 以八进制输出
# x 以十六进制输出
# n 与d类似，不同之处在于它会使用当前语言环境设置的分隔符插入到恰当的位置
# None  就是默认 十进制输出

print('{:b}'.format(114),'{:#b}'.format(114))
# 用二进制输出114  #代表添加进制的前缀

# 对浮点数或者复数数字进行[type]处理
# e 以科学计数法方式输出，e来表示指数，默认精度为6
# E 以科学计数法方式输出，E来表示指数，默认精度为6
# f 以定点表示法的形式输出(不是数 'nan' , 无穷数 'inf' ,  默认精度6 )
# F 以定点表示法的形式输出(不是数 'NAN' , 无穷数 'INF' ,  默认精度6 )
# g 通用格式，小数以'f'形式输出，大数以'e'形式输出
# G 通用格式，小数以'F'形式输出，大数以'E'形式输出
# n 跟g类似，不同之处在于它会使用当前语言环境设置的分隔符插入到恰当的位置
# % 以百分比的形式输出  数字会乘以100 后面再加上 %
# None 类似'g' ,不同之处在于当使用定点表示法时，小数点后将至少显示一位，默认精度与给定数值的精度一致

print('{:e}'.format(114514),'{:e}'.format(0.000114514)) # e+05 就是 ×10^5 ,e-04 就是 ×10^-4

print('{:f}'.format(1.14514)) # 默认小数点后6位

print('{:.2%}'.format(0.25)) # 进度为小数点后2位的百分数


print('{:.{er}f}'.format(1.14514,er=4))  # 设置精度为er，而er=4，等于设置精度为小数点后4位

print('{:{fill}{align}{width}.{pr}{ty}}'.format(1.14514,fill='.',align='^',width=11,pr=4,ty='g'))
# fill='.'用.填充  align='^'居中对齐  width=11 字符宽度11  pr=4 精度数4  ty='g'采用 有效数字方式 输出

# f 字符串语法糖
# 语法糖：(syntacticsugar)计算机语言中添加的某种语法，这种语法对语言功能没有影响，但更方便程序员使用。
# 由于f字符串语法糖是python3.6版本之后的，所以一些开源代码仍然使用.format()方法

print(f'今年是{year}年')

print(f'{-114:010}\t{114514:,}\t{1.14514:.3g}')

print(f'{1.14514:.^11.4g}')   # 和上面的东西输出方式相同
