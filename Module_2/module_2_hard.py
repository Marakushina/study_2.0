
import random
numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = random.choice(numbers)
print('Случайное число: ',n)
list_ = []
for i in range(1, n):
    for j in range(1, n):
            sum = (i+j)
            if n % sum == 0 and i!=j :
                list_.append([i,j])
def remove(list_):
    return ([list(k) for k in {*[tuple(sorted(k)) for k in list_]}])
result = sorted(remove(list_))
result_str = str(result)
result_ = "".join(n for n in result_str if  n.isdecimal())
print(result_)