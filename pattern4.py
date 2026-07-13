# Pattern 4
'''
****
*  *
*  *
****

'''

for i in range (1,5):
    if (i==1 or i==4):
        print("*"*4)
    else:
        for j in range (1,5):
            if (j==1 or j==4):
                print("*",end="")
            else:
                print(" ",end="")
        print()