# from math import sqrt

# class Triangle:
#     def __init__(self):
#         self.a_x = 0
#         self.a_y = 0
#         self.b_x = 3
#         self.b_y = 0
#         self.c_x = 0
#         self.c_y = 4
#     def side_1(self):
#         """Длина AB"""
#         return sqrt((self.b_x - self.a_x)**2 + (self.b_y - self.a_y)**2)

#     def side_2(self):
#         """Длина AC"""
#         return sqrt((self.c_x - self.a_x)**2 + (self.c_y - self.a_y)**2)

#     def side_3(self):
#         """Длина BC"""
#         return sqrt((self.b_x - self.c_x)**2 + (self.b_y - self.c_y)**2)

#     def perimetr(self):
#         return self.side_1() + self.side_2() + self.side_3()
        
# obj = Triangle()
# print(obj.side_1())
# print(obj.side_2())
# print(obj.side_3())
# print(obj.perimetr())

'''
Основные принципы ООП
1) инкапсуляция (скрытие интерфейса)
2) наследование (взятие функционала родительского класса)
3) полиморфизм (различное поведение объекта с 
        разными типами данных)
'''

# Инкапсуляция
'''
class Car:
    def __init__(self, name, color, max_speed):
        # для того, чтобы скрыть поля от пользователя, перед ними надо поставить
        # 2 нижних подчеркивания (эти поля стали недоступны на чтение и запись)
        # инкапсулрованные поля недоступны в основной части программы, но
        # ВНУТРИ КЛАССА ОНИ ДОСТУПНЫ
        self.color = color
        self.__name = name
        self.__max_speed = max_speed

    # аксессоры (геттеры/сеттеры)
    # геттеры
    def get_name(self):
        return self.__name
    
    def get_max_speed(self):
        return self.__max_speed
    
    # сеттер
    def set_max_speed(self, value):
        if value > 0 and value <= 200:
            self.__max_speed = value


c1 = Car('Lada', 'red', 110)
print(c1.get_name(), c1.color, c1.get_max_speed())
c1.set_max_speed(200)
print(c1.get_name(), c1.color, c1.get_max_speed())
c1.set_max_speed(-1)
print(c1.get_name(), c1.color, c1.get_max_speed())
'''

# Наследование
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
    # переопределение предыдущего конструктора
    def __init__(self):
        # super вызывает метод родительского класса и передает
        #   туда self
        # 1 параметр super - имя текущего класса
        # 2 параметр super - self
        super(Human, self).__init__()
        self.iq = 0
        
    def think(self):
        print('я думаю')

h1 = Human()
h1.think()
h1.sleep()
h1.eat()
print(h1.iq, h1.name)
'''

# Полиморфизм
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # self - то, что слева от +
    # other - то, что справа от +
    # метод должен вернуть новый объект
    def __add__(self, other):
        # isinstance(obj, class) - если obj это объект класса class, 
        #       функция вернут True (False в ином случае)
        if isinstance(other, Point):
            # tmp = Point()
            # tmp.x = self.x + other.x
            # tmp.y = self.y + other.y
            # return tmp
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Point(self.x + other, self.y + other)
    
    def __repr__(self):
        return f'<Point ({self.x} ; {self.y})>'

p1 = Point(1, 2)
p2 = Point(5, 6)
print(p1)
print(p2)
p3 = p1 + p2
print(p3)
p4 = p1 + 4
print(p4)

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
