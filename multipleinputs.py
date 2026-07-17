nums = input()   #only takes input as string

nums = input().split()  #takes input in string format and split on blank spaces and return the value in list format 
'''for eg - if input is given as 2 3 4 5
            it will take input in string format and then return the value in list format
            i.e ['2','3','4','5']   '''
            
nums = map(int(),input().split())
'''Here , to convert all the numbers into integer either we can use a for loop to take  each string and turn it as integer or
            we can MAP function .
            In the above line of code int() is used to convert into integer but to apply all it to all the numbers 
            we use the MAP function 
            map fucntion works in the following manner -
            int() - convert string into integer
            input().split() - converts string into list format but the elements are still string
            map() - it applies int() funtion to all the elements of input().split() 
            so the answer of 2 3 4 5 beomes [2,3,4,5]  '''
            
'''NOTE - Python reads line by line so if the input is of more than 1 line it'll only read  the first line ''' 

#Now for input of more than one line

nums = int(input()) #This is the number of number of inputs are to be taken 
n = input()
a=[] #This is an emoty to store the inputs
for i in range(n):  #This is a loop running the number of times the input is to be taken 
    store = map(int(),input().split()) #This is used to store every input in list format where every input is in integer format
    a.append(i)  #This is used to put the input in the list a[]