print('Задача 1')
# Создайте класс EvenIterator, который возвращает 
# чётные числа от 2 до n

class EvenIterator():
    def __init__(self, n):
        self.n=n
        self.chet=2
    def __iter__(self):
        return self
    def __next__(self):
        if self.chet>self.n:
            raise StopIteration
        
        valie=self.chet
        self.chet +=2
        return valie

for x in EvenIterator(10):
    print(x)

print('Задача 2')
# Создайте класс ReverseList, который итерируется по 
# списку с конца.

class ReverseList():
    def __init__(self, data):
        self.data = data
        self.index=len(data)-1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index<0:
            raise StopIteration
        value=self.data[self.index]
        self.index -=1
        return value
    
data=[10,20,30]
for x in ReverseList(data):
    print(x)


print('Задача 3')
# Дан массив:
# arr = np.array([3, 7, 1, 9, 4])
# Найдите:
# максимальный элемент
# среднее значение массива

import numpy as np
arr = np.array([3, 7, 1, 9, 4])
print(arr.max())
print(arr.mean())

print('Задача 4')
# Дан массив:
# arr = np.array([2, 8, 4, 10, 3])
# Получите все элементы больше 5.
arr = np.array([2, 8, 4, 10, 3])
print(arr[arr>5])

print('Задача 5')
# Даны два массива:
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# Найдите сумму массивов.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)


print('Задача 6')
# Дан массив:
# arr = np.array([1, 2, 3, 4])
# Создайте новый массив, где каждый элемент умножен на 3.

arr = np.array([1, 2, 3, 4])
print(arr * 3)