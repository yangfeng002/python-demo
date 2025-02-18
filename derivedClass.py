# devired class 派生类

# 父类，基类 超类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")

# 派生类 子类  继承父类
class Dog(Animal):
    pass  # pass是占位符，表示什么都不做，可以用pass来作为占位符


# dog = Dog('Willie')
# dog.speak()


# 继承父类，但是自己有构造函数
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name) # 调用父类的构造函数
        self.color = color

cat  = Cat('花猫', '白色')
print(cat.name)
print(cat.color)