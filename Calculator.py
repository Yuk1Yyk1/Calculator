
def calculate(expression):
    return eval(expression)

expression = input("Введите математическое выражение: ")
result = calculate(expression)
print("Результат:", result)