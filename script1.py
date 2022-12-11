def check(password):
    if len(password) < 6:
        return False
    elif not any(map(str.isdigit, password)):
        return False
    elif password.isdigit():
        return False
    elif "password" in password.lower():
        return False
    else:
        return True

password = input("Придумайте пароль: ")

if check(password):
    print("Пароль прошёл проверку.")
else:
    print("Пароль не удовлетворяет условиям!")
