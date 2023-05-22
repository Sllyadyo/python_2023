import math
import random

def Mini_Calculate():
    def calculate(operator, *args):
        if operator == "+":
            return sum(args)
        elif operator == "-":
            return args[0] - sum(args[1:])
        elif operator == "*":
            result = 1
            for arg in args:
                result *= arg
            return result
        elif operator == "/":
            try:
                result = args[0]
                for arg in args[1:]:
                    result /= arg
                return result
            except ZeroDivisionError:
                return "Ошибка: деление на ноль"
        elif operator == "^":
            return args[0] ** args[1]
        elif operator == "mod":
            return abs(args[0])
        elif operator == "rand":
            return random.randint(args[0], args[1])
        elif operator == "fact":
            return math.factorial(args[0])
        elif operator == "acos":
            if abs(args[0]) <= 1:
                return math.acos(args[0])
            else:
                return "Ошибка: значение за пределами допустимого диапазона"
        else:
            return "Неизвестная операция"

    while True:
        operator = input("Выберите операция (+, -, /, *, ^, mod, rand, fact, acos): ")
        if operator not in ["+","-","/","*","^","mod","rand","fact","acos"]:
            print('Неверная операция')
            continue

        args = []
        if operator in ["+","-","/","*","^"]:
            args.append(float(input("Введите число: ")))
            args.append(float(input("Введите число: ")))
        elif operator == "mod":
            args.append(float(input("Введите число: ")))
        elif operator == "rand":
            args.append(int(input("Введите минимальное значение: ")))
            args.append(int(input("Введите максимальное значение: ")))
        elif operator == "fact":
            args.append(int(input("Введите число для вычисления факториала: ")))
        elif operator == "acos":
            args.append(float(input("Введите число: ")))
        
        print("Результат:", calculate(operator, *args))

        answer = input("Хотите продолжиться работу калькулятора? (Yes/No): ")
        if answer.lower() != "yes":
            print('The program is completed')
            break

if __name__ == "__main__":
    Mini_Calculate()