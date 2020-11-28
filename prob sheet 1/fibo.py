ent=int(input("Enter number of numbers required in series"))

def fib(a):
    if a==0:
        return 0
    if a==1:
        return 1
    return fib(a-1)+fib(a-2)
for i in range (ent):
    value=fib(i)
    print(value)
