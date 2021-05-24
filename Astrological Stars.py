n=int(input("No of lines"))
x=int(input("0 or 1"))
a=bool(x)
if x==1:
    for i in range(n+1):
     print(i*"*")

elif x==0:
    for j in range(n+1):
     print((n-j)*"*")
