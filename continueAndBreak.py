numList = range(1, 101, 1) # 定义一个列表1-100

# 循环列表，并打印1-100之间的偶数，必须经过终止循环的过程才能打印
for num in numList:
    if num % 2 != 0:
        continue
    print(num)