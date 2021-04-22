'''
ООП - Объектно-Ориентированное Программирование

ООП - способ программирования, при котором мы используем классы и 
    объекты
класс - некий шаблон, который описывает то, что есть у объекта (поля)
    и то, что может делать объект (методы)
объект - экземпляр класса (что-то конкретное)

'''

# синтаксис создания класса
class Human:
    # конструктор класса (вызывается во время создания класса)
    # self - пустой объект класса, у которого мы указываем параметры
    def __init__(self, name='nameless', age=0, height=0):
        self.name = name
        self.age = age
        self.height = height

    # метод класса.
    # self - объект перед точкой
    def say_hi(self):
        print(f'{self.name} говорит "привет"')

    # метод, который форматирует то, как выводится объект
    def __repr__(self):
        return f'<Human {self.name} {self.age} {self.height}>'

# синтаксис создания объекта
h1 = Human('John', 12, 149) # в этот момент вывызывается конструктор (__init__)
# # поля объекта доступны через название объекта и точку
# h1.name = 'John'
# h1.age = 12
# h1.height = 149

h2 = Human()
print(h1.name, h2.name)

h3 = Human(age=90, name='Alice')

h1.say_hi()
h2.say_hi()

print(h1)
print(h2)
print(h3)








# from tkinter import *
# root = Tk()

# b = Button(root, width=12, text='lalala')
# b.pack()

# root.mainloop()
