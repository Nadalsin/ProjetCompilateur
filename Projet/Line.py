class Line:
    """class for storing values of Line parsed by the parser"""

    def __init__(self, x1 , y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def c_code(self):
        return "droite("+", "+self.x1+", "+self.y1+", "+self.x2+", "+self.y2+");"