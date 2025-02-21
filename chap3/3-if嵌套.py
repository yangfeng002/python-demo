# answer = input("请输入你的答案：")
# if answer == 'y':
#     # 测试下酒精含量
#    alcohol = eval(input("请输入你的酒精含量："))
#    if alcohol < 20:
#        print("你没有酒驾, 祝你一路平安")
#    elif alcohol < 80:
#        print("已构成酒驾，请不要开车")
#    elif alcohol >= 80:
#        print("请勿驾驶，否则可能导致醉驾")
# elif answer == 'n':
#     print("你可以走了")

# and 多个条件连接
# username = input("请输入用户名：")
# password = input("请输入密码：")
# if username == 'admin' and password == '123456':
#     print("欢迎管理员")
# else:
#     print("用户名或密码错误")

# or 多个条件连接
age = int(input("请输入你的年龄："))
if age >= 18 or age <= 60:
    print("你是成年人")
elif age < 18:
    print("你还未成年")
else:
    print("你已经老了")
