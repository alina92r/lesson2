
def ask_user ():
    user_say = input("Как дела?")
    while True:
        user_say = input("Как дела?")
        if user_say == 'Хорошо':
            print("Отлично")
            break

ask_user()