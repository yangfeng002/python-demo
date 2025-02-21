# eval 函数的使用， 去掉前后的引号，然后之前程序代码, 运行结果如下：
evaled = eval("1+2*3")
print(evaled)

print(eval('hello')) # 报错，去掉引号之后，就是一个变量名，不能直接执行