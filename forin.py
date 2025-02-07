# python for循环的使用
# 1. for循环的基本语法
phone_numbers = {
    "张三": 15872365555,
    "henry": 1357924680,
    "李四": 18976543210,
    "王五": 12345678901,
    123: 12345678901
}

# keys()方法获取字典的键，values()方法获取字典的值 items()方法获取字典的键值对
# for key in phone_numbers.keys():
#     print(key)

# for value in phone_numbers.values():
#     print(value)

phone = input("请输入用户名：")
for key, value in phone_numbers.items():
    if key == phone:
        print("你查找的手机号码为：" + str(value))
    else:
       print("没有找到该用户")