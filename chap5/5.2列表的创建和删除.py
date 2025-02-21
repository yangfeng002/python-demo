list1 = [12, "nnn", '3.12', True]
print(list1)

# list2 = list([1, 222, "3333", True]) # list()函数智能传入一个参数
# print(list2)

# # del list1 # 删除列表
# print(list1, "----------", list2)

# enumerate()函数可以同时迭代索引和值
for index, item in enumerate(list1):
    print(index, item)