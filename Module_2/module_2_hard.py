
import random
numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = random.choice(numbers)
print('Случайное число: ',n)
list_ = []
for i in range(1, n):
    for j in range(1, n):
            sum = (i+j)
            if n % sum == 0 and i!=j and i<j :
                list_.append(i)
                list_.append(j)

result_ = "".join(map(str,list_))
print(result_)