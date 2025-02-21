# 设置变量
i = 0 
while i < 3:
    # 输入用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # 判断用户名和密码是否正确
    if username == "admin" and password == "123456":
        print("登录成功！")
        i = 8  # 退出循环
    else:
        if i < 2: 
         print('用户名或密码错误！, 您还可以继续',2-i,'次')
        i += 1  # 尝试次数+1
        
if i == 3:
    print("登录失败！")