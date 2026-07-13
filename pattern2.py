# Pattern 2
'''
1
121
12321
1234321

'''
for i in range (1,5):
    for j in range (1,i+1):
        print(j,end="")
    for k in range (i,1,-1):
        print(k-1,end="")     # end = "" (to get both the loops output in one line)
    print() #to change line

