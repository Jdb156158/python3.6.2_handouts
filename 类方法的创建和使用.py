#类定义
class people:
    #定义基本属性
    name = ""
    age = 0
    #定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print(self.name,"说：我",self.age,"岁。体重：",self.__weight)

#实例化类
p = people("jason",26,130)
p.speak()
