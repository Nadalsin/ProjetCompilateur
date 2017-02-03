class Ellipse:
    """class for storing values of Ellipse parsed by the parser"""

    def __init__(self, rx=0 , ry=0, cx=0, cy=0):
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry

    def c_functionName(self):
        return "ellipse("

    def c_CXAttribute(self):
        return str(self.cx)

    def c_CYAttribute(self):
        return str(self.cy)

    def c_RXAttribute(self):
        return  str(self.rx)

    def c_RYAttribute(self):
        return str(self.ry)
