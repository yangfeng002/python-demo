# 该程序用于查询保留字与标识符。
import keyword # 引入keyword模块

# 打印保留字
print(keyword.kwlist)
print(len(keyword.kwlist))


# 常量定义， 不能修改
CONST = 100
print(CONST)