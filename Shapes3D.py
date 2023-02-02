#lets get it started in HA! Lets get it started in HEER!
import math
from Shapes import Polygon

#generating an "Abstract Class" (classes in python are all public). This will allow me to use this class in any subclasses i make that are instances of Shape3D
class Shape3D:
    def GetSurfaceArea(self) -> float:
        raise NotImplementedError()

    def GetVolume(self) -> float:
        raise NotImplementedError()

#This will define a Subclass of Shape3D.
class Cuboid(Shape3D):
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def GetVolume(self) -> float:
        return self.length * self.width * self.height

    def GetSurfaceArea(self) -> float:
        return 2 * ((self.length * self.height) + (self.width * self.height) + (self.length * self.width))
    
#this will make cuboid a child class of Cuboid
class Cube(Cuboid):
    def __init__(self, side_length):
        #the 'super()' method allows you to use the parent classes methods and properties.
        super().__init__(side_length, side_length, side_length)

    def GetVolume(self) -> float:
        return super().GetVolume()
    
    def GetSurfaceArea(self) -> float:
        return super().GetSurfaceArea()


#cylinder class
class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.height = height
        self.radius = radius

    def _GetBaseArea(self) -> float:
        return math.pi * math.pow(self.radius, 2)

    def GetSurfaceArea(self) -> float:
        return 2 * math.pi * self.radius * (self.height + self.radius)

    def GetVolume(self) -> float:
        return self._GetBaseArea() * self.height
    
#Sphere class
class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def GetSurfaceArea(self) -> float:
        return 4 * math.pi * math.pow(self.radius, 2)

    def GetVolume(self) -> float:
        return (4/3) * math.pi * math.pow(self.radius, 3)
    
#Prism class (Uses the Polygon class in shapes.py. Is imported at the top of the file)
class Prism(Shape3D):
    def __init__(self, side_length, faces, height):
        self.polybase = Polygon(side_length, faces)
        self.height = height
        self.area = (self.polybase.GetArea() * 2) + (self.polybase.GetPerimeter() * self.height)
        self.volume = self.polybase.GetArea() * self.height

    def GetSurfaceArea(self) -> float:
        return self.area

    def GetVolume(self) -> float:
        return self.volume