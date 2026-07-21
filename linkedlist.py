class Node:
    
    def __init__(self,data):
         self.data = data
         self.next = None
         ''' In this (data) is the value stored in a node and next is the variable storing the (address of the next node) '''
        
class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def get_length(self):
        ''' This is used to get the length of a singly linked list '''
        length = 0
        current = self.head
        while current:
            length = length + 1
            current = current.next
        return length
    
    def display(self):
        ''' This is used to display the linked list '''
        if not self.head:
            return ("Empty List")
        else:
            current = self.head
            while current:
                print(current.data , end = ' ')   
                current = current.next
            print()
            
    def insert_at_beginning(self,value):
        node = Node(value)
        if self.head:        # This is the condition to assign the head to the new node when the head already connected to a node
            node.next = self.head
        self.head = node   # This is the condition when there is no node connected to the head so it is assigning head to the new node
    
    def insert_at_end(self,value):
        node = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
        
    def insert_in_middle(self,pos,value):
        n = self.get_length()
        if (pos < 0) or (pos > n):
            print("Invalid Position")
        elif pos == 0:
            self.insert_at_beginning(value)
        elif pos == n:
            self.insert_at_end(value)
        else:
            node = Node(value)
            p = self.head
            q = None
            for i in range(pos):
                q = p
                p = p.next
            q.next = node
            node.next = p         