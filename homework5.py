immutable_var = (10, 20.5, True, "TEST") # Присваиваем переменной кортеж из нескольких элементов разных типов данных
print("Immutable tuple:", immutable_var) # Выполняем операцию вывода кортежа immutable_var на экран
print(type(immutable_var))               # Выведем тип нашей переменной
immutable_var[0] = 33                    # Попытка изменить элемент 0 кортежа immutable_var (Ошибка)
# Кортежи — это контейнеры, хранящие объекты в определенном порядке.
# В отличие от списков, кортежи неизменяемы.
# Как только мы создали кортеж, значение какого-либо его элемента уже нельзя изменить,
# также нельзя добавлять и удалять элементы.
mutable_list = [1, 1.5, False, "test"]             # Присваиваем переменной mutable_list список из нескольких элементов
print("Mutable list (original):", mutable_list)    # Выводим на экран список mutable_list (для проверки)
mutable_list[3] = "Modified"                       # Изменяем элемент номер четыре из списка mutable_list на Modified
print("Mutable list:", mutable_list)               # Выводим на экран измененный список mutable_list
