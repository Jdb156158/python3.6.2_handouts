class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      name = "重写父类的方法"
      print ('调用子类方法----',name)
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
