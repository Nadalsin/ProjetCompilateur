class Polygon:
    """class for storing values of Polyline parsed by the parser"""

    def __init__(self):
        self.lines = []

    def setPoints(self, linesList):
        self.lines = linesList

    def c_code(self):
        code = ""
        for p in self.lines:
            code += p.c_code()
        return code
