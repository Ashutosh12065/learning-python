n = int(input("Enter any  number :")) #number which will be used to find the closest value
m = int(input("Enter any  number :")) #number by which the closest number will be divisble by
if n>0:    
    for i in range(n,0,-1):
        if i%m==0:  
            print(i)
            break
else:
    for i in range(n,0):
        if i%m==0:
            print(i)
            break
        