def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(4,5,2)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [False, "любовь", 32]
values_dict = {'a':"зажигалочка", 'b':None, 'c':666 }
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ["високосный год", 12]
print_params(*values_list_2, 42)