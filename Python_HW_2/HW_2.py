# Arithmetic
#
#  1. Создать переменную item_1 типа integer.
import math

item_1 = 9

#  2. Создать переменную item_2 типа integer.
item_2 = 2

#  3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
result_sum = item_1 + item_2

#  4. Вывести result_sum в консоль.
print('Сложение', result_sum)

#  5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
result_subtr = max(item_1, item_2) - min(item_1, item_2)

#  6. Вывести result_subtr в консоль.
print('Вычитание:', result_subtr)

#  7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
result_multi = item_1 * item_2

#  8. Вывести result_multi в консоль.
print('Умножение:', result_multi)

#  9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
result_exp = item_1 ** item_2

#  10. Вывести result_exp в консоль.
print('Возведение в степень:', result_exp)

#  11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
result_m_exp = math.pow(item_1, item_2)

#  12. Вывести result_m_exp в консоль.
print('Возведение в степень с использование math:', result_m_exp)

#  13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
result_s_root = item_1 ** (0.5)

#  14. Вывести result_s_root в консоль.
print('Корень квадратный из item_1:', result_s_root)

#  15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
result_m_s_root = math.sqrt(item_1)

#  16. Вывести result_m_s_root в консоль.
print('Корень квадратный из item_1 с использованием math:', result_m_s_root)

#  17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
result_mp_s_root = math.pow(item_1, 0.5)

#  18. Вывести result_mp_s_root в консоль.
print('Корень квадратный из item_1 с использованием math,pow:', result_mp_s_root)

#  19. Присвоить переменной item_1 odd значение
item_1 = 5

#  20. Присвоить переменной item_2 even значение
item_2 = 2
#  21. Создать переменную result_division в которой вы разделите item_1 на item_2.
result_division = item_1 / item_2

#  22. Вывести result_division в консоль.
print('Результат деления item_1 на item_2:', result_division)

#  23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
result_m_floor = math.floor(result_division)

#  24. Вывести result_m_floor в консоль.
print('Округление result_division через floor:', result_m_floor)

#  25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
result_m_ceil = math.ceil(result_division)

#  26. Вывести result_m_ceil в консоль.
print('Округление result_division через ceil:', result_m_ceil)

#  27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = int(result_division)

#  28. Вывести result_int в консоль.
print('Округление result_division через явное приведение типов:', result_int)

#  29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss = item_1 / item_2

#  30. Вывести result_no_division_loss в консоль.
print('Деление без остатка:', result_no_division_loss)

#  31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2

#  32. Вывести result_division_loss в консоль.
print('Деление c остатком:', result_division_loss)

# Дальше будет реализация через арифметические действия с присваиванием.
#
#  33. Создать переменную item_3 и присвоить ей целое число
item_3 = 6

#  34. Прибавить 10 к item_3 с присвоением.
item_3 += 10

#  35. Вывести item_3 в консоль.
print('Прибавление с присвоением:', item_3)

#  36. Отнять 5 от item_3 с присвоением.
item_3 -= 5

#  37. Вывести item_3 в консоль.
print('Вычитание с присвоением:', item_3)

#  38. Умножить item_3 на 3 с присвоением.
item_3 *= 3

#  39. Вывести item_3 в консоль.
print('Умножение с присвоением:', item_3)

#  40. Разделить item_3 на 2 с присвоением.
item_3 /= 2

#  41. Вывести item_3 в консоль.
print('Деление с присвоением:', item_3)

#  42. Возвести в степень 2 item_3 с присвоением.
item_3 **= 2
#  43. Вывести item_3 в консоль.
print('Возведение в квадрат с присвоением:', item_3)

#  44. Найти квадратный корень item_3 с присвоением.
item_3 **= 0.5

#  45. Вывести item_3 в консоль.
print('Квадратный корень с присвоением:', item_3)

#  46. Присвоить остаток от деления item_3
item_3 %= 2
#  47. Вывести item_3 в консоль.
print('Отстаток от деления:', item_3)

# Boolean
#
#  48. Создать переменную b_item_t и присвоить True
b_item_t = True

#  49. Создать переменную b_item_f и присвоить False
b_item_f = False

#  50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
b_item_result_sum = b_item_t + b_item_f

#  51. Вывести b_item_relult_sum в консоль.
print('Результат сложения True и False:', b_item_result_sum)

#  52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
b_item_result_substr = b_item_t - b_item_f

#  53. Вывести b_item_relult_subtr в консоль.
print('Результат вычитания True и False:', b_item_result_substr)

#  54. Создать переменную b_item_result_multi и присвоить умножение b_item_t и b_item_f
b_item_result_multi = b_item_t * b_item_f

#  55. Вывести b_item_result_multi в консоль.
print('Результат умножения True и False:', b_item_result_multi)

#  56. Создать переменную b_item_result_division и присвоить деление b_item_t и b_item_f
#  57. Вывести b_item_result_division в консоль. (Получить ошибку)
try:
    b_item_result_division = b_item_t / b_item_f
except:
  print('На ноль делить нельзя')

#  58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
b_item_1_int = int(b_item_t)

#  59. Вывести b_item_1_int в консоль.
print('Приведение True к int:', b_item_1_int)

#  60. Создать переменную b_item_2_int и присвоить явное приведение b_item_f к int
b_item_2_int = int(b_item_f)

#  61. Вывести b_item_2_int в консоль.
print('Приведение False к int:', b_item_2_int)