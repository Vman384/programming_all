import random
array=[]
for i in range(1,101):
    array.append(random.randint(1,100))
dict={}
for i in array:
    x=0
    for j in array:
        if i==j:
            x+=1
            array.remove(j)
    dict.update({str(i):x})
print(dict)