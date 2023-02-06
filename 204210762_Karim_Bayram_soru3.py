import random
x=[]
for i in range(10):
    x.append(random.random()*100)
print(x)
y=x.copy()
for i in range(len(y)):
    for j in range(len(y)-1-i):
        if y[j]>y[j+1]:
            temp=y[j]
            y[j]=y[j+1]
            y[j+1]=temp
print(y)
print(y==sorted(x))
y=input()