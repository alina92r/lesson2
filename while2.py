
dict={"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
def ask_user_dict():
    try:
        while True:
            ask_user = input("Введи вопрос ")
            if ask_user in dict:
                print(dict[ask_user])
                break
    except KeyboardInterrupt:
        print(" Пока! ")

ask_user_dict()
