# 1) Создать переменную типа String
string = "Homework_1"
type_string = type(string)
print(type_string)

# 2) Создать переменную типа Integer
age = 25
type_age = type(age)
print(type_age)

# 3) Создать переменную типа Float
float_digit = 39.99
type_float_digit = type(float_digit)
print(type_float_digit)

# 4) Создать переменную типа Bytes
byte_var = bytes(104)
type_byte_var = type(byte_var)
print(type_byte_var)

# 5) Создать переменную типа List
list_var = list_type = ['123', '425', 23, 48, True, ['1', '2']]
type_list_var = type(list_var)
print(type_list_var)

# 6) Создать переменную типа Tuple
fruit_tuple = ("apple", "apricot", "banana", "lime", "lemon")
type_fruit_tuple = type(fruit_tuple)
print(type_fruit_tuple)

# 7) Создать переменную типа Set
set_var = set('hello')
type_set_var = type(set_var)
print(set_var)
print(type_set_var)

# 8. Создать переменную типа Frozen set
frozen_set_var = frozenset('goodbye')
type_frozen_set_var = type(frozen_set_var)
print(frozen_set_var)
print(type_frozen_set_var)

# 9) Создать переменную типа Dict
dict_person = {'name': 'Inna', 'age': 21, 'job': 'QA engineer'}
type_dict_person = type(dict_person)
print(type_dict_person)

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print("String: ", string, ',' "type:", type_string)
print("Integer: ", age, ',' "type:", type_age)
print("Float: ", float_digit, ',' "type:", type_float_digit)
print("Bytes: ", byte_var, '\n',  "type:", type_byte_var)
print("List: ", list_var, ',' "type:", type_list_var)
print("Tuple: ", fruit_tuple, ',' "type:", type_fruit_tuple)
print("Set: ", set_var, ',' "type:", type_set_var)
print("Frozen set: ", frozen_set_var, ',' "type:", type_frozen_set_var)
print("Dict: ", dict_person, ',' "type:", type_dict_person)

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
str1 = "Hello"
str2 = "QA engineer!"
str_concat = str1 + "," + str2
print(str_concat)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(string, age)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(string + ' ' + str(age))

