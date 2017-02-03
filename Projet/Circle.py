class Circle:
    """class for storing values of Circle parsed by the parser"""

    def __init__(self, r=0, cx=0, cy=0):
        self.cx = cx
        self.cy = cy
        self.r = r

    def c_functionName(self):
        return "cercle("

    def c_CXAttribute(self):
        return str(self.cx)

    def c_CYAttribute(self):
        return str(self.cy)

    def c_RAttribute(self):
        return str(self.r)


