class Rectangle:
    def __init__(self, width, height):
        self.width =width
        self.height=height
    def area(self):
        return self.width* self.height
    def perimeter(self):
        return 2*(self.width + self.height)
    #instance
rect=Rectangle(2,3)
#access
print('Width',rect.width)
print('height:',rect.height)
print('area',rect.area())
print('perimeter',rect.perimeter())
        