'''     Dynamic Array    '''
import ctypes  # This is a library which provides c compatiable data types

class MyList:
    
    def __init__(self):
        self.size = 1  # This is the len of array
        self.n = 0  # This is the number of elements present in the array
        # Create a ctype array with size = self.size
        
        self.A = self.__make_array(self.size)
    
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()  # This is a code in C language and it Creates a ctype array (static,referential) with size capacity
    
    def __len__(self):
        return self.n  # This will return the number of elements present in the array
    
    def append(self,item):
        if self.n == self.size:
            # resize the array
            self.resize(self.size*2) # double the size of array
        
        # append
        self.A[self.n] = item
        self.n = self.n + 1 

    def resize(self,new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A  to B
        for i in range (self.n):
            B[i] = self.A[i]
        # reassign the array A to B
        self.A = B
        
    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
    
    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n = self.n - 1
        
    def clear(self):
        self.size = 1
        self.n = 0
    
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'Value Error - Value not found in the list'
    
    def insert(self,pos,item):
        if self.n == self.size:
            self.resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n = self.n + 1
        
    def __delitem__(self,pos):
        # delete the item at pos
        if 0 <= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n - 1
         
    def remove(self,item):
        pos = self.find(item)
        if type(pos) == int:
            # delete the item at pos
            self.__delitem__(pos)
        else:
            return pos