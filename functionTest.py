# 函数定义， 计算圆面积，参数为直径, **是幂运算
# def roundArea(diameter):
#     pi = 3.1415926
#     area = pi * (diameter / 2) ** 2
#     return area

# # 调用函数，计算圆面积, 直径为5
# diameter = 5
# area = roundArea(diameter)
# print("圆的直径为", diameter, "，圆的面积为", area)

# 阶乘计算
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 调用函数，计算5的阶乘
result = factorial(5)
print("5的阶乘为", result)