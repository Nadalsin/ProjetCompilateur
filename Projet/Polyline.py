class Polygon:
    """class for storing values of Polyline parsed by the parser"""

    def __init__(self):
        self.points = []

    def setPoints(self, pointsList):
        self.points = pointsList