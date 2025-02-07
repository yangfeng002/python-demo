# python 列表的使用

# 1.获取列表的长度  len() 函数
# list = [1, 2, 3, 'hello', 'world']
# print(len(list))

# 2. 访问列表中的元素， 采用索引的方式，从0开始
# list = [1, 2, 3, 'hello', 'world']
# print(list[0])

""" 3.向list中添加元素 
 list = [1, 2, 3, 'hello', 'world']
  append() 方法, 列表末尾添加一个元素
  insert() 方法，在指定位置插入一个元素
  extend() 方法，将一个列表中的元素添加到另一个列表中(批量添加)
"""
list = [1, 2, 3]
# list.append('python') # 列表的末尾添加指定的元素
# list.insert(0, 'xxxx')  # 在索引为2的位置插入某个元素
# list.extend(['java', 'c++']) # 将列表 ['java', 'c++'] 中的元素添加到列表 list 中, 从列表末尾添加
# print(list)


""" 
  4. 删除元素
  remove() 方法，删除指定元素
 """
# list2 = [1, 2, 3, 4, 6, 4]
# print(list2)
# list2.remove(4) # 删除列表中第一个出现的指定元素
# list2.remove() # remove() 函数中如果不出现参数会报错
# list2.pop(5) # 删除指定索引的元素
# list2.pop() # pop() 函数中如果不出现参数，则默认删除的是最后一个元素
# res = list2.pop(2) # 删除指定索引的元素并返回该元素的值
# print(res)
#list2.clear() # 清空列表中的所有元素


