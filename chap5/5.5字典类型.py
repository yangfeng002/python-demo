# 字典类型定义
dict1 = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(dict1, type(dict1))

# 字典类型创建方式2， 使用zip函数
lst1 = [10, 20 , 30]
lst2 = ['apple', 'banana', 'orange']
dict2 = zip(lst1, lst2)
dict3 = dict(dict2)
print(dict3, type(dict3))

# 字典类型创建方式3
score = dict(first = 20, second = 30, third = 40)
print(score, type(score))
print(score.get('first'))
print(score.get('fourth', 'not found'))