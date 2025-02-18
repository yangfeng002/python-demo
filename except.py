# 异常和错误

# 异常的处理
num1 = input("请输入第一个数字：")
num2 = input("请输入另一个数字：")

# try except
# try:
#     result = int(num1) / int(num2)
#     print("结果是：", result)
# except ZeroDivisionError:
#     print("除数不能为0") # 捕获到除数为0的异常

# try except else
# try:
#     result = int(num1) / int(num2)
#     print("结果是：", result)
# except ZeroDivisionError:
#     print("除数不能为0") # 捕获到除数为0的异常
# else:
#     print("程序正常执行") # 程序正常执行，没有异常发生

# try except else finally
try:
    result = int(num1) / int(num2)
    
except ZeroDivisionError as error:
    print(error)
else:
    print("结果是：", result)
finally:
    print('这句话，无论异常是否发生都会执行。')