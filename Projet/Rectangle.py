class Rectangle:
    """class for storing values of rectangles parsed by the parser"""

    def __init__(self, x , y,width, height, rx=0, ry=0 ):
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.width = width
        self.height = height