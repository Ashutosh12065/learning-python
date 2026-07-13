'''
***
 ***
  ***
'''

n = int(input("Enter any number"))
for i in range (0,n):
    for j in range (0,i):
        print(" ",end="")
    for k in range (0,n):
        print("*",end="")
    print()