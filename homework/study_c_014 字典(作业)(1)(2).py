# 0. 请问下面变量 d 是典吗？
# >>> d = {}
# 不是，这是一个集合set

# 1. 字典中，同样一个值是否可以出现两次？
# 值可以出现两次，键不能出现两次

# 2. 请问下面代码创建的字典中，键和值分别是什么？
# >>> d = {}.fromkeys("吕布", 999)
# 键是 '吕' 值999     '布' 999
d = {}.fromkeys("吕布", 999)
print(d)

# 3. 请问下面代码中，del d 这个语句，是单独删除 d 变量还是将 d 变量和其指定的字典一起干掉呢？
d = dict.fromkeys("Fish", 250)
del d
# 将 d 变量和其指定的字典一起干掉

# 4. 请问下面创建字典的 8 种方法中，哪几种是正确的。
a = {99:"吕布", 90:"关羽", 60:"刘备"}
# b = dict(99:"吕布", 90:"关羽", 60:"刘备")             # 要用等号，不能用：
# c = dict(99="吕布", 90="关羽", 60="刘备")             # 不能用数字吧
d = dict([(99, "吕布"), (90, "关羽"), (60, "刘备")])
e = dict({99:"吕布", 90:"关羽", 60:"刘备"})
# f = dict({99="吕布", 90="关羽", 60="刘备"})           # {}内不用等号
# h = dict({99:"吕布", 90:"关羽"}, 60="刘备")           # =前不能数字
i = dict(zip([99, 90, 60], ["吕布","关羽","刘备"]))

# bcfh 错误  adei正确

# 5. 请问下面代码执行之后，变量 b 中的内容是？
a2 = {"小甲鱼":"You are my superstar."}
b = a2
a2.clear()
# {} b也被清空了
print(b)


# 动动手：
# 0. 请利用字典类型，改进上一节课后作业的电影查询小程序。
# 需要存放的数据如下：
# 电影名称
# 上映时间
# 导演（可能多人）
# 主演（可能多人）
# 电影评分


u,v,w,x,name_list=dict(),dict(),dict(),dict(),[]

print('欢迎进入影评小程序\n1.数据录入\n2.查询数据\n3.退出程序')
l,k=0,0
while l==0:
    gong = input('输入想查询的功能(1/2/3):')
    if gong=='1':
        while k==0:
            name_shu=input('请输入电影名称：')
            day=input('请输入上映日期：')
            director=input('请输入导演名字(多人请用/分隔)：')
            actor=input('请输入演员名字(多人请用/分隔)：')
            rating=input('请输入电影评分：')

            name_list.append(name_shu)
            u[name_shu],v[name_shu],w[name_shu],x[name_shu] = day,director,actor,rating

            ques_1 = input('请问是否继续录入(Y/N)')
            if ques_1=='Y':
                continue
            else:
                break

    elif gong=='2':
        name_cha=input('请输入电影名称：')
        if name_list.count(name_cha)==0:
            print('查无次片！')
            exit()
        else:
            print(f'电影名称：{name_cha}\n上映日期：{u[name_cha]}'
                  f'\n导演名单：{v[name_cha]}\n演员名单：{w[name_cha]}\n当前评分：{x[name_cha]}')
    else:
        l=1
'''
参考答案：
movies = {}                         # 创建空字典
    
print("欢迎进入鱼C影评小程序")
print("1.数据录入")
print("2.查询数据")
print("3.退出程序")
op = int(input("请输入想要的功能(1/2/3)："))
    
while op != 3:
    if op == 1:
        go = True
        while go:
            movie = input("请输入电影名称：")
            date = input("请输入上映日期：")
            directors = [i.strip() for i in input("请输入导演名字（多人请用 / 分隔）：").split('/')]  # 原来还能这样创建列表
            actors = [i.strip() for i in input("请输入演员名字（多人请用 / 分隔）：").split('/')]
            scores = input("请输入电影评分：")
            movies[movie] = [date, directors, actors, scores]  # 键值对 中的值可以是一个列表  
    
            if 'N' == input("请问是否继续录入(Y/N):"):
                go = False
    
    if op == 2:
        name = input("请输入电影名称：")
        if name in movies:
            print(f"电影名称：{name}")
            print(f"上映日期：{movies[name][0]}")  # 键对应值是列表，拿出列表中的 序号0 的元素
            print(f"导演名单：{movies[name][1]}")
            print(f"演员名单：{movies[name][2]}")
            print(f"当前评分：{movies[name][3]}")
        else:
            print("查无此片！")
    
    op = int(input("\n请输入想要的功能(1/2/3)："))


'''



# 1. 请编写一个电话簿程序。
# 程序实现如下：

'''
参考答案：
phone_book = {}
    
print("欢迎进入鱼C电话簿")
while True:
    ins = input("请输入命令（I:录入 / C:查询 / D:删除 / P:打印 / E:退出）：")
    
    if ins == 'I':
        print("\n-- 录入模式 --")
        while True:
            name = input("请输入姓名：")
            if name in phone_book:
                print("该姓名已录入，手机号码是：", phone_book[name])
                if input("请问是否修改(Y/N)：") == 'Y':
                    phone = input("请输入新的手机号码：")                 # phone被input()改变，替换了原来的phone
                    while not phone.isnumeric() or len(phone) != 11:
                        phone = input("输入不合法，请重新输入：")
                else:
                    phone = phone_book[name]                          # 不修改 则phone 还是 phone_book 中的[name]键对应的值
            else:
                phone = input("请输入手机号码：")                        # 这里input 了 phone
                while not phone.isnumeric() or len(phone) != 11:      # 进行判断，phone不合法就循环
                    phone = input("输入不合法，请重新输入：")              # 这里再次 input 了 phone，phone又被定义了一遍，实现小循环
            phone_book[name] = phone                                  # 把phone 录入 phone_book 中[name]键 对应的 值
            if input("是否继续录入(Y/N)：") != 'Y':                     # 原来 input 和 if 可以放一句中，以后Y/N 就这样写
                print()
                break
    
    elif ins == 'C':
        print("\n-- 查询模式 --")
        while True:
            name = input("请输入姓名：")
            if name in phone_book:
                print(name, phone_book[name], sep="：")     # sep=':'意思是print()中的多个要素，用： 分开
            if input("是否继续查询(Y/N)：") != 'Y':           # 这里直接不回答Y就是退出小循环，回到大循环，省去continue了
                print()
                break
    
    elif ins == 'D':
        print("\n-- 删除模式 --")
        while True:
            name = input("请输入姓名：")
            if name in phone_book:
                phone_book.pop(name)
            if input("是否继续删除(Y/N)：") != 'Y':
                print()
                break
    
    elif ins == 'P':
        print("\n-- 打印模式 --")
        for each in phone_book:
            print(each, phone_book[each], sep="：")
        print()
    
    elif ins == 'E':
        break
'''



