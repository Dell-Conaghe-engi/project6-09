'''python
x = 10
if x > 0:
 print("Число положительное")
elif x == 0:
 print("Ноль")
else:
 print("Число отрицательное")
'''
'''python
age = 20
has_passport = True
if age >= 18 and has_passport:
 print("Вход разрешен")
else:
print("Вход запрещен")'''
#`for` — проход по коллекции или диапазону:
'''for i in range(5):# от 0 до 4
 print(i)'''
#`while` — выполняется, пока условие истинно:
'''
n = 3
while n > 0:
 print(n)
 n -= 1'''
'''name = "Аня"
age = 22
print(f"Привет, {name}! Тебе {age} года.")'''
#Список (`list`)
'''```
numbers = [1, 2, 3, 4]
numbers.append(5) # добавление
print(numbers[0]) # доступ по индексу
```
'''
#Кортеж (`tuple`) — как список, но **нельзя изменять**:
'''```
point = (10, 20)
```'''
#Множество (`set`) — хранит только уникальные значения:
'''```
unique = {1, 2, 2, 3}
print(unique) # {1, 2, 3}
```
'''
# Словарь (`dict`)
'''```
person = {"name": "Иван", "age": 30}
print(person["name"])
```
'''
''''''
''''''