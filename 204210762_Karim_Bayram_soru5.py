x=int(input("Please enter a number"))
y=set()
for i in range(x+1):
    if i>1:
        for j in range(2,x):
            if i%j ==0:
                break
            else:
                y.add(i)
print(y)
print(f'The number of primes is {len(y)}')
y=input()