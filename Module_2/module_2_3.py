my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = 0
print(my_list)
while start < len(my_list):
    number = my_list[start]
    start = start + 1
    if number == 0:
        continue
    elif number < 0:
        break
    else:
        print(number)


