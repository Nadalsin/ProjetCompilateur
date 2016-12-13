class Circle:
    """class for storing values of Circle parsed by the parser"""

    def __init__(self, r, cx=0, cy=0):
        self.cx = cx
        self.cy = cy
        self.r = r

    def c_code(self):
        return "cercle("+self.cx+", "+self.cy+", "+self.r+");"

