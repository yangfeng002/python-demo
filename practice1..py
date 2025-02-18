# 测试  输出到文件中  人生苦短，我用python!
fp = open('test.txt', 'w', encoding='utf-8') # 打开文件
print('人生苦短，我用python!', file=fp) # 输出到文件中
fp.close() # 关闭文件