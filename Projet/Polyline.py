class Polyline:
    """class for storing values of Polygon parsed by the parser"""

    def __init__(self):
        self.points = []


    def line_code(self,point_a,point_b):
        point_xy = point_a.split(",")
        point_x2y2 = point_b.split(",")
        line = "droite("+point_xy[0]+","+point_xy[1] +","+point_x2y2[0]+","+point_x2y2[1]
        return line

    def c_code(self):
        code = ""
        for i in range(0,len(self.points)-1):
            if(i < len(self.points)-2):
                code += self.line_code(self.points[i],self.points[i+1]) +");\n    "
            else:
                code += self.line_code(self.points[i],self.points[i+1])


        return code
