def fact(i):
    if(i==1):
        return 1
    return i*fact(i-1)
    

num=int(input("Enter a number:"))
print(fact(num))

    
