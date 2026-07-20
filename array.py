'                             ARRAY -                                          '

import array

# Creation

arr1=array.array('i',[10,20,30,40,50])
print(arr1)

# Access

arr1[1]
arr1[4]    # Here 1 and 4 are the index of the array so will fetch the value at the index 1 and 4

# Traversal

for i in arr1:
    print(i)
    
# Insertion
''' For eg- Insert 45 between 40 and 50 
            then so the resulting array must look like this -
            [10,20,30,40,45,50]
            here 45 is at 4th index so we will insert at the same index'''
            
arr1.insert(4,45) # Here 4 is the index and 45 is the value
print(arr1)

#  Deletion

arr1.remove(45)
print(arr1)

# Updation

arr1[3]=60
print(arr1)

# Sorting

arr2=array.array(i,[1,0,7,5,3])
print(arr2)

sorted(arr2) # This will give the result in the form of a list

array.array(i,sorted(arr2)) # This will give the result in the form of an array

# Merging

arr1 + arr2

# Splitting

arr3 = arr1 + arr2

ix = int(len(arr3)/2)
'''Slicing'''
arr3[:ix]
arr3[ix:]
