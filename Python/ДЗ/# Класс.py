 # Класс
class Cat:
     def __init__(self, name): #Конструктор класса 
        self.name=name  #Атрибуты класса 
     def make_sound(self): #Метод класса
         print('Мяу')
cat=Cat('Мурка') #Объект класса

cat = Cat("Мурка", 5)
cats = [cat, Cat('Пенис', 4), Cat('Хуй', 3)]
for cat in cats:
    cat.make_sound()

class Bank:
    def __init__(self, owner, balance):
        self.owner=owner
        self.__balance=balance
    def dep (self,mony):
        self.__balance+=mony
    def withdraw(self,mony):
        if self.__balance>=mony:
            self.__balance-=mony
        else:
            print('Ты нищий')
# Обращение к родительскому классу
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Human):
    def __init__(self,group,name,age):
        super().__init__(name,age)
        self.group=group
hm=Human()
