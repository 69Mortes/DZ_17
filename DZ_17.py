# Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальное.
# Результат вывести в виде кортежа.
print("Чтобы вставить готовый текст, введите - 1\nЕсли желаете ввести текст вручную, введите - 2")
g1 = int(input("Введите 1 или 2 : "))
if g1 == 1:
    stroka = input("введите предложение: ") # просим пользователя ввести строку
else:
    stroka = "The sun is shining"
print("Нашe предложение: ", stroka)  # выводим исходный результат
# Разделим нашу строку на отдельные символы:
a1 = []  # создаем пустой список, в котором будут уникальные элементы
# проверим нашу строку на дубляж символов
for spisok1 in stroka: # прогон букв по индексу из строки
    a1.append(spisok1) # добавляем поочередно элементы списка
    k1 = a1.count(spisok1) # создаем переменную для поиска дубляжа
    if k1 == 2: # создаем условие, при нахождении дубляжа
        print("удаляем дубляж:   ", a1.pop()) # сообщаем какой элемент повторился и удаляем его
print("полученный кортеж", tuple(a1)) # Результат выводим в виде кортежа
