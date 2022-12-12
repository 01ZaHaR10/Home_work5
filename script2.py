def sum(*args):
    rezault = 0
    for i in args:
        rezault += i
    return rezault

try:
    print(f"Результат: {sum()}")
    print(f"Результат: {sum(1, 2)}")
    print(f"Результат: {sum(1, 2, 3, 4, 5)}")
    print(f"Результат: {sum(2.6, 3.4, 1/2, 4**0.5, 16*10)}")
except TypeError:
    print("Передаваемые параметры должны быть числами!")
