# python 字典类型讲解
# 字典是一种无序的键值对集合，字典中的键必须是唯一的，值可以重复。
# 字典的创建方式有两种：
# 1. 使用{}创建字典，键值对之间用冒号:分隔，键值对之间用逗号,分隔。 
# 2. 使用dict()函数创建字典，传入一个序列，序列中的元素必须是元组，或者列表，列表中的元素必须是键值对。
# 字典
cityCodes = {'北京': '101010100', '上海': '201100101', '广州': '301010100', '深圳': '401010100'}
# print(cityCodes)
# 字典的访问方式

# print(cityCodes['北京'])

# 字典的添加方式
# cityCodes['天津'] = '101030100'
# print(cityCodes)

# 字典的删除方式
del cityCodes['上海']
# del cityCodes['001']
print(cityCodes)