# ДЗ
'''
from math import sqrt
class Triangle:
    def __init__(self):
        self.a_x = 0
        self.a_y = 0
        self.b_x = 3
        self.b_y = 0
        self.c_x = 0
        self.c_y = 4

    def side_1(self):
        """а-b"""
        return sqrt((self.b_x - self.a_x)**2 + (self.b_y - self.a_y)**2)

    def side_2(self):
        """а-c"""
        return sqrt((self.c_x - self.a_x)**2 + (self.c_y - self.a_y)**2)

    def side_3(self):
        """b-c"""
        return sqrt((self.b_x - self.c_x)**2 + (self.b_y - self.c_y)**2)

    def perimetr(self):
        return self.side_1() + self.side_2() + self.side_3()

obj = Triangle()
print(obj.side_1())
print(obj.side_2())
print(obj.side_3())
print(obj.perimetr())
'''

# Основные принципы ООП
'''
1) инкапсуляция (скрытие функционала от пользователя)
2) наследование (наследование функционала предыдущего класса)
3) полиморфизм (различное поведение объекта с 
        разными типами данных)
'''

# инкапсуляция
'''
class Human:
    def __init__(self):
        self.name = 'nameless'
        self.email = 'qwerty@mail.ru'
        # чтобы инкапсулировать поле, пишем 2 нижних подчеркивания
        #       перед ним
        # инкапсулированное поле ДОСТУПНО ТОЛЬКО внутри класса
        # (за пределами его, к ниму нет доступа)
        self.__age = 10
    
    # чтобы разрешить доступ, пишем аксессоры (геттеры/сеттеры)
    # геттер
    def get_age(self):
        return self.__age
    
    # сеттер
    def set_age(self, value):
        if 0 < value < 100:
            self.__age = value

h1 = Human()
print(h1.name, h1.email, h1.get_age())
h1.set_age(88)
print(h1.name, h1.email, h1.get_age())
h1.set_age(199)
print(h1.name, h1.email, h1.get_age())
h1.set_age(-1)
print(h1.name, h1.email, h1.get_age())
h1.set_age(5)
print(h1.name, h1.email, h1.get_age())
'''

# наследование:
'''
class Animal:
    def __init__(self):
        self.name = 'nameless'
        self.age = 0

    def sleep(self):
        print('я сплю')
    
    def eat(self):
        print('я ем')

# Animal - родительский класс (от него наследуемся)
# Human - дочерний класс
class Human(Animal):
    def __init__(self):
        # переопределение предыдущего конструктора
        # super вызывает метод родительского класса и передает
        #   туда self
        # 1 параметр super - имя текущего класса
        # 2 параметр super - self
        super(Human, self).__init__()
        self.iq = 0

    def think(self):
        print('я думаю')

h1 = Human()
print(h1.iq)
print(h1.age)
print(h1.name)
h1.think()
h1.eat()
h1.sleep()
'''

# полиморфизм
'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # перегрузка сложения:
    # other - то, с чем складываем
    # __add__ вызывается во время сложения объекта с чем-то
    # self - объект слева от +
    # other - объект справа от +
    def __add__(self, other):
        # isinstance(obj, class) - если obj это объект класса class, 
        #       функция вернут True (False в ином случае)
        if isinstance(other, Point):
            tmp = Point()
            tmp.x = self.x + other.x
            tmp.y = self.y + other.y
            return tmp
        elif isinstance(other, int):
            tmp = Point()
            tmp.x = self.x + other
            tmp.y = self.y + other
            return tmp
        else:
            print('ERROR')

    def __repr__(self):
        return f'<Point ({self.x} ; {self.y})>'


a = Point(1, 2)
b = Point(5, 6)
print(a)
print(b)
c = a + b
print(c)
d = a + 1
print(a)
print(d)
'''

# практика:
'''
    задача 1:
    написать класс Person
    в классе будут поля: name, age, height
    поле age и height должны быть приватными (инкапсулированными)
    для них создать геттеры и сеттеры
    так же добавить в класс 2-3 метода (присущих только человеку)

    задача 2:
    создать класс Employee (сотрудник), унаследованный от класса Person
    класс Employee должен расширить конструктор клаасса человек 
    полями "position" (должность) и paycheck (зарплата)
    эти поля тоже будут приватными с ограничениями через геттеры/сеттеры
    так же добавить несколько методов
'''

