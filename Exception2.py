
def get_summ(num_one,num_two):
    sum=0
    try:
        sum=int(num_one)+int(num_two)
        print(sum)
    except ValueError:
        print("Нужно вводить числа")

get_summ(2, 2)
get_summ(3, "3")
get_summ("4", "4")
get_summ("five", 5)
get_summ("six", "шесть")