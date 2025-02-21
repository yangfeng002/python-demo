# 列表的添加和删除
# list1 = [1]
# print(list1, id(list1))

# # 添加一个元素 append()
# list1.append('test')
# print(list1, id(list1))

# # insert()方法可以将元素插入到指定位置
# list1.insert(1, 'insert')
# print(list1, id(list1))

# # clear()方法可以清空列表
# list1.clear()
# print(list1, id(list1))

# reverse()方法可以反转列表
# list2 = [1, 2, 3, 4, 5]
# list2.reverse()
# print(list2)

# # sort()方法可以对列表进行排序, 默认是升序
# list3 = [5, 3, 1, 4, 2]
# list3.sort()
# print(list3)

# # reverse设置为True可以进行降序排序
# list3.sort(reverse=True)
# print(list3)

# sorted()函数可以对列表进行排序, 会返回一个新的列表, 原始列表不会改变
list4 = [5, 3, 1, 4, 2]
list5 = sorted(list4)
print(list4, id(list4))
print(list5, id(list5))