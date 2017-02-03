class Rectangle:
    """class for storing values of rectangles parsed by the parser"""

    def __init__(self, x=0 , y=0,width=0, height=0, rx=0, ry=0 ):
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.width = width
        self.height = height

    def c_functionName(self):
        return "rectangle("

    def c_X1Attribute(self):
        return str(self.x)

    def c_Y1Attribute(self):
        return str(self.y)

    def c_WIDTHAttribute(self):
        return str(self.width)

    def c_HEIGHTAttribute(self):
        return str(self.height)



