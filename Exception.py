
def get_summ(num_one,num_two):
    sum=0
    try:
        #num_one=int(input("Введите первое число "))
        #num_two=int(input("Введите второе число "))
        sum=num_one+num_two
        print(sum)
    except ValueError:
        print("Нужно вводить числа")
#get_summ()

print(get_summ(2, 2))
print(get_summ(3, "3"))
print(get_summ("4", "4"))
print(get_summ("five", 5))
print(get_summ("six", "шесть"))