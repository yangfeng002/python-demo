# 变量相关的操作 局部变量  自由变量  全部变量  内部变量  遵循LEGB原则
# LEGB: Local(局部作用域) Enclosing(包含作用域, 也就是相对嵌套函数来说，属于外部) Global(全局作用域) Built-in(内置作用域)

from math import pi  # 内置变量

# pi = "global pi" # 全局变量

def outer():
    # pi = "outer pi" # 自由变量
    def inner():
        # pi = "inner pi"  # 局部变量
        print(pi)
    # 调用嵌套函数
    inner()
# 调用自定义函数
outer()