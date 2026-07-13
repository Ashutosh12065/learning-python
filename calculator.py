class Calculator:
    
    #constructor --> superpower --> it gets called everytime an object is made without need to explicitly call it
    def __init__(self):
        self.a = 0
        self.b = 0
        self.opt = ""
        self.display()
        self.display2()
        self.operation()
        
    def display(self):
        print("Welcome to the calculator")
        
    def display2(self):
        print("Enter the numbers :")
        
    def operation(self):
        
        print('''What operation you want to perform -
              addition (+) , subtraction (-) , multiplication (*) or division (/):''')
        self.opt=input()
        self.inpt()
        
        if self.opt=="+":
            self.add()
        elif self.opt=="-":
            self.subtract()
        elif self.opt=="*":
            self.multiply()
        elif self.opt=="/":
            self.divide()
        else:
            print("Jaa be laude")
        
    def inpt(self):
        self.a=int(input("Enter number 1 :"))
        self.b=int(input("Enter number 2 :"))
    
    def add(self):
        print(self.a+self.b)
        
    def subtract(self):
        print(self.a-self.b)
    
    def multiply(self):
        print(self.a*self.b)
    
    def divide(self):
        if self.b==0:
            print("Cannot divide by zero")
        else:
            print(self.a/self.b)
        
obj=Calculator()