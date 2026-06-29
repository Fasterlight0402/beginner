print('Hello World')
print("                \n\
          @            \n\
        * * *          \n\
      *  *  *  *       \n\
   *  *   *  *  *  *   \n\
        * * *          \n\
        * * *          \n\
      *  *  *  *       \n\
    *  *  *  *  * *   \n\n")   # \n  换行  在加\代表续行

poetry =  '''      
     山村怀咏
一去二三里，烟村四五家。
亭台六七座，八九十枝花。
'''
#  双''' '''  或者 """  """  中间可以保留长字符串 可以不需要再用 \n\ 进行换行
print(poetry)

myteacher = '小甲鱼'
yourteacher = myteacher
myteacher = '黑夜'
print(yourteacher)

# 计算一年有多少秒
daysperyear = 365
hoursperday = 24
secondsperhour = 3600
print(daysperyear*hoursperday*secondsperhour)

#  %s  ：字符串   %f  ：浮点   %d ：整数
'大家好，我是xb，今年30，身高178，体重69.5'
name='bx'
age=30
height=178
weight=69.5

print('大家好，我是%s,今年%d,身高%d,体重%.1f' %(name,age,height,weight)) #方法一

print('大家好，我是{},今年{},身高{},体重{}' .format(name,age,height,weight)) #方法二

print(f'大家好，我是{name},今年{age},身高{height},体重{weight}' ) #方法三




