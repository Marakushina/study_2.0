my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = 0
print(my_list)
while start < len(my_list):
    start = start + 1
    number = my_list[start]
    if number == 0:
        continue
    elif number < 0:
        break
    elif number == len(my_list):
        print(number)
        print('Список закончился')
    else:
        print(number)


