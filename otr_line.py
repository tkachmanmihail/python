from graphics import * # импортируем библиотеку graphics
win = GraphWin("Окно для графики", 400, 400) # создаём окно для графики размером 400 на 400 пикселей
obj = Line(Point(x1, y1), Point(x2, y2))
obj.draw(win) # отображаем точку в окне для графики
win.getMouse() # ждём нажатия кнопки мыши
win.close() # закрываем окно для графики
-------------------------------------------------------
from graphics import *
win = GraphWin("Окно для графики", 400, 400)
obj = Circle(Point(200, 200), 50)
obj.draw(win)
win.getMouse()
win.close()
---------------------------------------------------------
from graphics import *
win = GraphWin("Окно для графики", 400, 400)
obj = Circle(Point(200, 200), 50)
obj.draw(win)
win.getMouse()
win.close()
--------------------------------------------------------------
Пример программы на Python, которая отображает прямоугольник в графическом окне.
from graphics import *
win = GraphWin("Окно для графики", 300, 300)
obj = Rectangle(Point(50, 50), Point(200, 250))
obj.draw(win)
win.getMouse()
win.close()
-------------------------------------------------------------------------
Для отображения эллипса в Python используется процедура
obj = Oval(Point(x1, y1), Point(x2, y2))
x1, y1 – координаты первого фокуса эллипса,
x2, y2 – координаты второго фокуса эллипса.
Пример программы на Python, которая отображает эллипс в графическом окне.
from graphics import *
win = GraphWin("Окно для графики", 300, 300)
obj = Oval(Point(100, 100), Point(250, 200))
obj.draw(win)
win.getMouse()
win.close()
-------------------------------------------------------
Для отображения многоугольника в Python используется процедура
obj = Polygon(Point(x1, y1), Point(x2, y2),…, Point(xn, yn))
x1, y1, x2, y2,…, xn, yn – координаты вершин многоугольника.
Пример программы на Python, которая отображает пятиугольник в графическом окне.
from graphics import *
win = GraphWin("Окно для графики", 400, 400)
obj = Polygon(Point(10, 10), Point(300, 50), Point(200, 300), Point(150, 150), Point(70, 70))
obj.draw(win)
win.getMouse()
win.close()
-------------------------------------------------------------------
from graphics import *
win = GraphWin("Окно для графики", 400, 400)
obj = Circle(Point(200, 200), 50)
obj.setFill("blue")
obj.draw(win)
win.getMouse()
win.close()









