
a = input("Введите первую строку ")
b = input("Введите вторую строку ")


def main(a,b):
    if (isinstance(a,str)==True and isinstance(a,str)==True):      
        if a == b:
            return 1
        else:
            if len(a) > len(b):
                return 2
            elif b=='learn':
                return 3
            else: 
                return 1
    else:
        return 0

print(main(a,b))