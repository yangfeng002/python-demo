# 元组使用
# t = (1,2,3)
# print(t, type(t))

# 只有一个元素的元组, 需要在元素后面加上逗号, 否则会被当作括号
# t = (1,)
# # t = (1)
# print(t, type(t))

# 删除元组
# del t
# print(t) 

# 元组可以支持序列操作, 是不可变序列
# t = (10, 10, 30, 20, 4)
# print( 10 in t)
# print(10 not in t)
# print(t.index(30))
# print(max(t))
# print(min(t))
# print(t.count(10))

# t = ('python', 'java', 'c++', 'javascript')
# # 循环遍历元组
# for item in t:
#     print(item)

# # for 和len()配合使用
# for i in range(len(t)):
#     print(i, t[i])


# # for 和enumerate()配合使用
# for i, item in enumerate(t):
#     print(i, item)

# 元组生成式
t = tuple(x for x in range(5))
print(t)