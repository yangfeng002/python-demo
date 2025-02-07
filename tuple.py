# python 元组类型  Tuple
# 元组是另一种有序列表，但是元组一旦初始化就不能修改。元组用括号()括起来，元素之间用逗号隔开。

# 定义元素
# tuple1 = ()
# tuple1 = (1, 2, 3, "hello")
# print(tuple1)

# 访问元素
# print(tuple1[2])

# 元组可以嵌套
# tuple2 = (1, 2, (3, 4), 5)
# print(tuple2[2][0])

# 修改元组的值  报错，元组一旦初始化就不能修改
# tuple1[0] = 4
# print(tuple1)

# 删除元组 报错 元组一旦初始化就不能删除
# del tuple1[0]
# print(tuple1)

# 元组和字典结合使用
# 字典是无序的，而元组是有序的，所以可以将元组作为字典的键。
# condiates = {
#     (106.4, 20.2): "Sunny",
#     (106.3, 20.1): "Cloudy",
#     (106.2, 20.3): "Rainy"
# }
# print(condiates[(106.4, 20.2)])

# 示例 将手机里的电话通讯录通过元组形式表现出来
phone_book = {
    ("小米"): "123-456-7890",
    ("chaozong", 1): "234-567-8901",
    ("chaozong", 2): "345-678-9012"
}

print(phone_book[("chaozong", 1)])