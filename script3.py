cache = {0: 1, 1: 1}

def f(n):
    global cache
    if n in cache:
        return cache[n]
    cache[n] = f(n-1) + f(n-2)
    return cache[n]

try:
    n = int(input("Введите число: "))
    print(f"Число Фибоначчи: {f(n)}")
except ValueError:
    print("Некорректный ввод!")
except RecursionError:
    print("Слишком большое число. Превышена глубина рекурсии.")
