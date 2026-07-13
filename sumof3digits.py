#sum of digits of a 3 digit number
num=int(input("Enter a 3 digt number :"))
sum=0
while num!=0:
    a=num%10
    num=num//10
    sum=sum+a
print(sum)
    