# 格式化输出  format()方法 f-字符串   既可以对字符串进行格式化，也可以对数字进行格式化
# 格式化输出 字符串
names = ['Alice', 'Bob', 'Charlie']
year = "蛇"

#format()方法的第一种用法
# for name in names:
#     content = """
#            祝：{0}生日快乐！
#            一帆风顺，万事如意！
#            {1}年大吉
#         """.format(name, year)
#     print(content)

# format() 方法的第二种用法
# for name in names:
#     content = """
#             祝{currentName}生日快乐！
#             一帆风顺，万事如意！
#              {currentYear}年大吉""".format(currentName = name, currentYear = year)
#     print(content)

# f-string（Python 3.6 引入） f-字符串的使用
# for name in names:
#     content = f"""
#             祝{name}生日快乐！
#             一帆风顺，万事如意！
#             {year}年大吉"""

# 练习作业： 请使用字符串格式化输出，班里每个人对应的成绩，要求成绩保留2位小数
scores = {'Alice': 89.5678, 'Bob': 92.3456, 'Charlie': 88.1234}

# 方式1： f-string
# for name, score in scores.items(): 
#     content = f"""{name}的成绩：{score: .2f}"""
#     print(content)

# 方式2 format()方式
for name, score in scores.items(): 
    content = """{name}的成绩：{score:.2f}""".format(name= name, score=score)
    print(content)