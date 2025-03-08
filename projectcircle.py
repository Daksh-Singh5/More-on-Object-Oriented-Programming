
class circle:
    def __init__(self,radius,perimeter,area):
        self.radius = radius
        self.perimeter = 2*22/7*radius+perimeter
        self.area = 22/7*radius**2+area

circles = circle(7,0,0)

print(circles.area,"|",circles.perimeter)