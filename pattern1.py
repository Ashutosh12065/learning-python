#pattern 1
'''
*
**
***
****
'''
for i in range(1,5):
        print("*"*i)
        
# Using nested loops with proper understanding 
n = int(input("Enter a number :"))
for i in range (1,n+1):
    for i in range (1,i+1):
        print("*")