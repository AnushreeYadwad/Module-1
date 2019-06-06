n=(int(input("Enter a number:")))
a=n
sum=0
while(n>0):
    dig=n%10
    sum=sum+dig
    n=n//10
print("The sum of digits of ",a," is:",sum) 
