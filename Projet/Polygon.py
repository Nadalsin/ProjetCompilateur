class Polygon:
    """class for storing values of Polygon parsed by the parser"""

    def __init__(self):
        self.lines = []

    def setlines(self, linesList):
        self.lines = linesList

    def c_code(self):
        code = ""
        for l in self.lines:
            code += l.c_code
        return code
