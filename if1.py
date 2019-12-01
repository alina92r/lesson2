

age=int(input("Введите свой возраст "))

def main(age):
    if age < 7:
        return "Вы должны ходить в детский сад"
    elif 7 <= age < 18:
        return "Вы должны учиться в школе"
    elif 18 <= age <24:
        return "Вы должны учиться в университете"
    else:
        return "Вы должны работать"

print(main(age))
