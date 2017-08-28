class Test:
    def f(self):
        print(self)
        print(self.__class__)

t = Test()
t.f()
