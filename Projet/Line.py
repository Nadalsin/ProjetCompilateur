class Line:
    """class for storing values of Line parsed by the parser"""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def c_functionName(self):
        return "droite("

    def c_X1Attribute(self):
        return str(self.x1)

    def c_X2Attribute(self):
        return str(self.x2)

    def c_Y1Attribute(self):
        return str(self.y1)

    def c_Y2Attribute(self):
        return str(self.y2)

