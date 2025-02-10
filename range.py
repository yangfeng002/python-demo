# range函数的使用
# 1. range函数的基本使用
# 打印出1到10的整数序列
# for i in range(1, 11): 
#     print(i)

# 打印 1- 100之间所有奇数的和
sum = 0 
for i in range(1, 100):
    if i % 2 == 0 :
      sum += i
print(sum) 