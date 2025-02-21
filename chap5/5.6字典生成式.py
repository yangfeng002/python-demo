# 字典生成式
import random

# 第一种方式
dict1 = { item: random.randint(1, 100) for item in range(4) }
print(dict1)

# 第二种方式，用zip() 函数
list1 = [1, 2, 3, 4]
list2 = ['apple', 'banana', 'orange', 'grape', 'pear']
# print(zip(list1, list2))
dict2 = { item:value for item,value in zip(list1, list2)}
print(dict2)