# 类的示例代码
class  Test:
    def prt(self):
        print(self)
        print(self.__class__)

# t = Test()
# t.prt()
# 输出结果： <__main__.Test object at 0x000001> <class '__main__.Test'>

# self不是python的关键字，可以自定义变量名，但最好不要用self，因为它已经被python默认使用了。
class Test2:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)

t2 = Test2()
t2.prt() # 输出结果： __main__.Test2 object at 0x000001148D8F6900> <class '__main__.Test2'>