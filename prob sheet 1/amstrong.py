a=int(input("Enter the number:"))
c=0
d=a
while a!=0:
    b=a%10
    c+=(b*b*b)
    a=a//10
if d==c:
    print(d,"is an amstrong number")
else:
    print(d,"is not an amstrong number")
    
