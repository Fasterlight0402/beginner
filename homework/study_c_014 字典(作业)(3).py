# 0. 请问可以使用下面方法来更新字典的值吗？
# >>> d = dict.fromkeys("FishC")
# >>> d.update([('F',70), ('i',105), ('s',115), ('h',104), ('C',67)])

# 不能，update() 里要么是字典，要么是等式


# 1. 请问下面代码执行之后，变量 e 的内容是？
# d = {"小甲鱼":"千年王八，万年龟。"}
# e = d.copy()
# d["小甲鱼"] = "666"
#
# print(d)
# {'小甲鱼':'666'}

# 2. 请问下面代码执行之后，变量 e 的内容是？
# d = {"小甲鱼":{"数学":99, "英语":88, "语文":101}}
# e = d.copy()
# d["小甲鱼"]["语文"] = 100
#
# print(d)
# {"小甲鱼":{"数学":99, "英语":88, "语文":100}}

# 3. 请问下面代码执行之后，字典 d 的内容是？
# d = {}
# d[1] = "千年王八"
# d[1.0] = "万年龟"   # 1.0 就是1，把之前的覆盖了
# print(d)
#
# {1:'万年龟'}


# 4. items()、keys() 和 values()
# 三个方法分别用于获取字典的键值对、键和值三者的视图对象，你如何理解 “视图对象” 的含义？
# 用来观察对象的，对象改变，视图对象也随之改变

# 5. 请问如何判断某一个值是否在字典中？
# 先用 新字典={y:x for x,y in 字典.items()}   再用   新字典.get(某一值) 找

# 6. 请问视频最后演示的代码，为什么字典 d 打印出来的结果是酱紫的？
# >>> d = {x:y for x in [1, 3, 5] for y in [2, 4, 6]}
# >>> d
# {1: 6, 3: 6, 5: 6}
#
# 先是 1：1 还然后 1:2 这样就把之前 1：1 给覆盖掉了，以此类推 最后只有1：3   2：3  3：3

# 动动手
# 0. 请按照要求编写一个网站的注册模块
# 我们知道，通常一个网站的用户名都是唯一的，这就要求注册的时候，系统代码可以识别当前输入的用户名是否已经存在？T
# 如果存在，则不允许注册！
# 那么现在请大家一起来动手，编写一个网站的注册模块。
# 要求：
# 用户名不允许重复
# 数据库需要保存用户名及密码
# 初始用户及密码（"小甲鱼":"I_love_FishC"，"不二如是":"FishC5201314"）
#
# 程序实现如下：

user_library={'小甲鱼':'I_love_FishC','不二如是':'FishC5201314'}
aw=[]

new=input('请输入用户名：')
while True :
    if new in user_library:
        print('该用户已被注册！')
        new=input('请重新输入用户名：')
    else:
        new_mm=input('请输入密码：')
        user_library[new]=new_mm            # 新用户的密码会变成可读的，不安全
        break
import hashlib

user_jm=tuple(user_library.values())
user_name=list(user_library.keys())

for i in user_jm:
    j=bytes(i,'utf-8')
    result = hashlib.md5(j)
    k=result.hexdigest()
    aw.append(k)

user_library_jm=dict(zip(user_name,aw))
print('-------------------\n目前已注册的用户有：')
for i,j in user_library_jm.items():
    print(i,j,sep=':')


# 1. 提升网站的安全性来自：
# 作为一个成熟的网站，是不可能会去保存用户的明文密码。
# 换句话说，用户的密码在传输到服务器数据库之前，会被单向加密为密文。
# 也就是说，服务器数据库保存的是加密后的密文，而非用户的明文密码（很多鱼油密码忘了之后跑来问小甲鱼，其实我也是无能为力的……）。
# 那么这里就涉及到一个单向加密的算法实现（单向加密，即仅通过密码无法逆向获得明文的加密手段），譬如 MD5 就是一种朴素的单向加密方案。
# 使用 Python 如何将明文通过 MD5 加密算法生成密文呢？
# 简单，小甲鱼给大家来个 1 秒钟教学~
# 直接举个例子你们就知道怎么玩了：

import hashlib
result = hashlib.md5(b"FishC")
# print(result.hexdigest())
# 9d22182e926ca703cd0f5926e7d57782
#
# 好了，那么请大家将上一题代码中的明文密码，使用 MD5 进行加密吧~
# 请务必做到跟下图一样噢^o^P
#
# 友情提示：
# hashlib.md5() 的参数是需要一个 b 字符串（即 bytes 类型的对象），
# 这里可以使用 bytes("123", "utf-8") 的方式将 "123" 转换为 b"123"。

'''
参考答案：
import hashlib
    
fc_db = {"小甲鱼":hashlib.md5(b"I_love_FishC"), "不二如是":hashlib.md5(b"FishC5201314")}
    
name = input("请输入用户名：")
while True:
    if fc_db.get(name) != None:
        print("该用户名已被注册！")
        name = input("请重新输入用户名：")
    else:
        break
    
passwd = input("请输入密码：")
bstr = bytes(passwd, "utf-8")
passwd = hashlib.md5(bstr)
fc_db[name] = passwd                # 从这存入的新用户的密码就已经被加密过了，不再可读了
    
print("------------------")
print("目前已注册的用户有：")
for each in fc_db.items():
    print(each[0], each[1].hexdigest(), sep="：")

'''

