# OOP class to handle following scenarios :
   # A user can create and view 2D coordinates
   # A user can find distance between 2 coordinates
   # A user can find the distance of a coordinate from origin
   # A user can check if a point lies on a given line
   # A user can find the distance between a given 2D point and a given line
class coordinates:
    
    def __init__(self,x,y):
        self.x_cord=x   # taking x and y coordinates
        self.y_cord=y
        
    # A user can create and view 2D coordinates
    def __str__(self):
        return '<{},{}>'.format(self.x_cord,self.y_cord) #gives the format of coordinates --> <3,4> or <5,10>
    
    # A user can find distance between 2 coordinates
    def euclidean_distance(self,other):
        # fomula used --> sqrt[(x2-x1)^2 + (y2-y1)^2]
        return ((self.x_cord-other.x_cord)**2 + (self.y_cord-other.y_cord)**2)**0.5
    
    # A user can find the distance of a coordinate from origin
    def distance_from_origin(self):
        return self.euclidean_distance(coordinates(0,0)) # Here coorinates is called as  an object to give the coordinates of origin as <0,0>
    
class line:
    
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
        
    def __str__(self):
        return "{}x + {}y + {} = 0 ".format(self.A,self.B,self.C)
    
    # A user can check if a point lies on a given line
    def point_on_line(line,coordinates):
        if line.A*coordinates.x_cord + line.B*coordinates.y_cord + line.C == 0:
            print("Point lies on the line")
        else:
            print("Point does not lie on the line")
            
    # A user can find the distance between a given 2D point and a given line
    def shortest_distance(line,coordinates):
        return abs((line.A*coordinates.x + line.B*coordinates.y + line.C) / (line.A**2 + line.B**2))