# 面向对象编程
# 要求： 定义一个学生，名字 班级  成绩
# 动态修改学生成绩
# 动态打印学生信息

class Student:
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade
        self.score = 0  #刚开始默认学生成绩为0
    # 设置学生成绩
    def set_score(self, score):
        self.score = score
    # 打印学生信息
    def print_info(self):
        print(f"""学生姓名：{self.name}, 学生成绩：{self.score}, 班级：{self.grade}""")

# student = Student('张三', '二年级')
# student.set_score(90)
# student.print_info()

# 私有属性定义
class Person:
    def __init__(self, name,age):
        # 私有属性定义
        self.__name = name
        self.__age = age
     # 私有方法定义
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    # 公共方法
    def say_hello(self):
        print(f"Hello, my name is {self.__name} and I am {self.__age} years old.")

# 创建对象
person = Person('李四', 35)
# print(person.__name, person.__age)  # 私有属性不能直接访问, 会报错
# print(person.get_name(), person.get_age())  # 公共方法可以访问私有属性
person.say_hello()  # 公共方法调用