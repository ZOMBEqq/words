user_input = input("Введите строку: ")

if len(user_input) > 10:
    words = user_input[:10] + "..."
else:
    words = user_input

print("Результат:", words)