# Дано натуральное число. Выведите его последнюю цифру.
# Входные данные: вводится единственное число (гарантируется, что оно не превышает 10 000).
# Выходные данные: выведите ответ на задачу.

a = int(input("введите натуральное число"))
if a <= 10000:
    print(a)
    c = a%10
    print(c)
