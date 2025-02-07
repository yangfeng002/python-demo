# print('hello world')
""" lover = '1556666520'
ex_lover = '1556668520'
print("现在女朋友联系："+lover)
print("前女朋友联系：" + ex_lover) """

# print("Hello, World!")
""" print(type(True))
print(type(False))
print(type(None)) # NoneType 空值 """


# 缩进4个空格用来表示代码块，不要使用tab键，因为tab键的宽度是不固定的。
""" mood = True
if mood:
    print("I'm happy today!")
    print("I'm learning Python.")
else:
    print("I'm sad today.")
 """

# 老婆心情60分-100分，分数越高表示老婆越开心，反之表示老婆越不开心。
""" mood = 80
if mood < 60:
    print("回家做家务吧，老婆不开心。")
else:
    print("老婆开心得一塌糊涂。") """

# 输入年龄，判断是否可以结婚. input是Python的内置函数，用来获取用户输入。
age = input("请输入您的年龄：")
age = int(age) # 将字符串转换为数字类型
if age >=25:
    print("恭喜您，您可以结婚！")
else:
    print("抱歉，您未满25周岁，无法结婚。")