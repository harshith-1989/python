import math # for sqrt function

class Point:
  number_of_instances = 0 #all the variables are can be made shared by accessing as <class name>.<variable name>
  
  def __init__(self,x=0,y=0,z=0):
    self.x = x
    self.y = y
    self.z = z
    Point.number_of_instances += 1
    
  def point_print(self): # is an instance method
    print ("point : (",self.x,",",self.y,",",self.z,")")
    
  def __str__(self): # print operator overloading
    return ("point : ({},{},{})".format(self.x,self.y,self.z))
  
  def __add__(self,point2): # add operator overloading
    return Point(self.x+point2.x, self.y+point2.y, self.z+point2.z)
  
  @staticmethod  # accepts only the arguments that are passed, no self arguments
  def distance_between_points(point1, point2):
    return math.sqrt( (point1.x-point2.x)**2 + (point1.y-point2.y)**2 + (point1.z -point2.z)**2 )
    
  @staticmethod
  def get_count_of_instances_generated():
    return Point.number_of_instances
  
  @classmethod
  def three_d_distance(self, point1, point2):
    return self(point1.x-point2.x, point1.y-point2.y, point1.z-point2.z)

############ End of class definition    
p1 = Point(2,4,6)
p2 = Point(3,5,9)

print (Point.distance_between_points(p1,p2))
print (Point.get_count_of_instances_generated())

three_d_distance = Point.three_d_distance(p1,p2)
print (three_d_distance)

sum_of_coordinates = p1+p2
print (sum_of_coordinates)
