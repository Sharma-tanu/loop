i=int(input("enter number to check for armstrong:-"))
sum=0
orig=i
while (i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=1//10
if orig==sum:
    print("armstrong")
else:
    print("not armstrong")