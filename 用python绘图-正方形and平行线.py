import turtle #引入绘图模块，引入就是告诉python你要用它，引入用：import
t = turtle.Pen()  #调用turtle模块中的Pen函数，它会自动创建一个画布
t.forward(50)  #forward指令是让箭头向前移动，括号里的参数是移到的像素值
t.left(90) #left指令是让箭头左转90度
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.reset() #让箭头回到原点，下面我们开始画平行线
t.backward(100)
t.up()  #让箭头抬起，意思停止作画
t.right(90) #像右转90度
t.forward(20)   #让箭头放下，意思开始作画
t.left(90)
t.down()
t.forward(100)
