# 模块的测试
import datetime

# 获取当前时间
# now = datetime.datetime.now()
# print("当前时间：", now)

import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')