'''                               2D Lists                      '''

# "Creation" 
matrix = [
    [1,2,3],
    [4,5,6],
    [8,9,10]
]
print(type(matrix))

# "Display"

def display_matrix():
    for row in matrix:
        print(row)

# "Traversal"

'''Can be done in two ways - element wise or index wise'''

'''index wise'''
# method 1
for row in matrix:
    print(row,type(row))

# method 2    
for row in matrix:
    for element in row:
        print(element,end=" ")
    print() #This is used to print in matrix form as this is used to change the line

# method 3
m=len(matrix) # this gives the number of rows
n=len(matrix[0]) # this gives the number of columns
for i in range(m):
    for j in range(n):
        print(matrix[i][j])
    print()   # this is used to change the line so as to give the output in matrix form

# "Updation"

matrix[i][j]="value you want change" # this is the suntax of updation
# here i,j is the index of which you want to change the value of 
'''for eg - '''

matrix[1][2]=900
display_matrix(matrix)

# "Insertion"

matrix("index of row").insert("index at which you want to insert the element","the element you want to insert") 
# this is the syntax of insertion

# append
matrix["index of row in which element needs to be appended"].append("elements which is to be appended") # this is the syntax to append

# "Deletion"
matrix["index of row which the element is to be removed"].remove("elemmet which is to be removed")
'''pop() can also be used'''
