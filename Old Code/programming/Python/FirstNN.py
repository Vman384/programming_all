import random

x = [5,7,26]
y = [13,17,55]

n1 = random.uniform(-1,1)
n2 = random.uniform(-1,1)

random.seed(1)


error = 7
while error > 6:
    error = 0
    newerror = 0



    for i in range(len(x)):
        error += abs(n1 * x[i] + n2 - y[i])


    newn1 = n1 + random.uniform(-error,error)
    newn2 = n2 + random.uniform(-error,error)


    for i in range(len(x)):
        newerror += abs(newn1 * x[i] + newn2 - y[i])

    if newerror < error:
        n1 = newn1
        n2 = newn2

    print(error, n1, n2)



print(n1,n2)