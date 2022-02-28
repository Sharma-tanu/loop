# n=int(input("Enter number"))
# count=0
# i=1
# while (i<=n):
#     if (n%i==0):
#         count=count+1
#     i=i+1
# if(count==2):
#     print("prime")
# else:
#     print("not prime")  

n=1
while(n<=100):
    count=0
    i=2
    while(i<=n//2):
        if(n%i==0):
            count=count+1
            # break
        i=i+1
    if(count==0 and n!=1):
        print(n)
    n=n+1


