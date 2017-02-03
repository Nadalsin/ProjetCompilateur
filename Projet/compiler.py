import AST
from Circle import Circle
from Rectangle import Rectangle
from Ellipse import Ellipse
from Line import Line
from Polygon import Polygon
from Polyline import Polyline
from AST import addToClass


objectList = {}
objectList['circle'] = Circle()
objectList['rect'] = Rectangle()
objectList['line'] = Line()
objectList['ellipse'] = Ellipse()
objectList['polygon'] = Polygon()
objectList['polyline'] = Polyline()

currentShapeBitch = None

def initCode():
    bytecode = '#include "declarations.h"\n#include "cinematique.h"\n#include "liste.h"\n#include "dessins.h"\n\n'
    bytecode += 'void setup() {\n    Serial.begin(9600);\n    Serial.println("Setup");\n    s1.attach(S1, MIN_US, MAX_US);\n    s2.attach(S2, MIN_US, MAX_US);\n    delay(100);\n}\n\n'
    bytecode += 'void loop() {\n    Serial.println("Loop");\n    lectureCorrectif();\n'
    return bytecode

def endCode():
    bytecode = '    Serial.println("End");\n    Serial.flush();\n    exit(0);\n}'
    return bytecode


# noeud de programme
# retourne la suite de tous les enfants
@addToClass(AST.ProgramNode)
def compile(self):
	bytecode = initCode()
	for c in self.children:
		bytecode += c.compile()
	return bytecode


@addToClass(AST.DessinsNode)
def compile(self):
    bytecode = ""
    for c in self.children:
        bytecode += c.compile()
    bytecode += endCode()
    return bytecode

@addToClass(AST.DessinNode)
def compile(self):
    bytecode = ""
    for c in self.children:
        bytecode += c.compile()
    bytecode += ");\n"
    return bytecode

@addToClass(AST.TypeNode)
def compile(self):
    global currentShapeBitch
    bytecode = "    "
    if self.children[0].compile() == "circle":
        bytecode += objectList['circle'].c_functionName()
        currentShapeBitch = objectList['circle']
    elif self.children[0].compile() == "rect":
        bytecode += objectList['rect'].c_functionName()
        currentShapeBitch = objectList['rect']
    elif self.children[0].compile() == "line":
        bytecode += objectList['line'].c_functionName()
        currentShapeBitch = objectList['line']
    elif self.children[0].compile() == "ellipse":
        bytecode += objectList['ellipse'].c_functionName()
        currentShapeBitch = objectList['ellipse']
    elif self.children[0].compile() == "polygon":
        currentShapeBitch = objectList['polygon']
    elif self.children[0].compile() == "polyline":
        currentShapeBitch = objectList['polyline']

    return bytecode

@addToClass(AST.AttributesNode)
def compile(self):
    bytecode = ""
    for c in self.children:
        bytecode += c.compile()
    return bytecode

@addToClass(AST.AttributeNode)
def compile(self):
    bytecode = ""
    if isinstance(currentShapeBitch,Circle):
        if self.attributeName.compile() == "cx":
            currentShapeBitch.cx = self.attributeValue.compile()
            bytecode += currentShapeBitch.cx + ","
        elif self.attributeName.compile() == "cy":
            currentShapeBitch.cy = self.attributeValue.compile()
            bytecode += currentShapeBitch.cy + ","
        elif self.attributeName.compile() == "r":
            currentShapeBitch.r = self.attributeValue.compile()
            bytecode += currentShapeBitch.r
    elif isinstance(currentShapeBitch,Rectangle):
        if self.attributeName.compile() == "x":
            currentShapeBitch.x = self.attributeValue.compile()
            bytecode +=  currentShapeBitch.x + ","
        elif self.attributeName.compile() == "y":
            currentShapeBitch.y = self.attributeValue.compile()
            bytecode += currentShapeBitch.y + ","
        elif self.attributeName.compile() == "width":
            currentShapeBitch.width = self.attributeValue.compile()
            bytecode += str(int(currentShapeBitch.x) + int(currentShapeBitch.width))+ ","
        elif self.attributeName.compile() == "height":
            currentShapeBitch.height = self.attributeValue.compile()
            bytecode += str(int(currentShapeBitch.y) + int(currentShapeBitch.height))
    elif isinstance(currentShapeBitch, Line):
        if self.attributeName.compile() == "x1":
            currentShapeBitch.x1 = self.attributeValue.compile()
            bytecode += currentShapeBitch.x1 + ","
        elif self.attributeName.compile() == "y1":
            currentShapeBitch.y1 = self.attributeValue.compile()
            bytecode += currentShapeBitch.y1 + ","
        elif self.attributeName.compile() == "x2":
            currentShapeBitch.x2 = self.attributeValue.compile()
            bytecode += currentShapeBitch.x2 + ","
        elif self.attributeName.compile() == "y2":
            currentShapeBitch.y2 = self.attributeValue.compile()
            bytecode += currentShapeBitch.y2
    elif isinstance (currentShapeBitch,Ellipse):
        if self.attributeName.compile() == "cx":
            currentShapeBitch.cx = self.attributeValue.compile()
            bytecode += currentShapeBitch.cx + ","
        elif self.attributeName.compile() == "cy":
            currentShapeBitch.cy = self.attributeValue.compile()
            bytecode += currentShapeBitch.cy + ","
        elif self.attributeName.compile() == "rx":
            currentShapeBitch.rx = self.attributeValue.compile()
            bytecode += currentShapeBitch.rx + ","
        elif self.attributeName.compile() == "ry":
            currentShapeBitch.ry = self.attributeValue.compile()
            bytecode += currentShapeBitch.ry
    elif isinstance (currentShapeBitch,Polygon):
        if self.attributeName.compile() == "points":
            currentShapeBitch.points = str.split(self.attributeValue.compile())
            bytecode += currentShapeBitch.c_code()
    elif isinstance(currentShapeBitch,Polyline):
        if self.attributeName.compile() == "points":
            currentShapeBitch.points = str.split(self.attributeValue.compile())
            bytecode += currentShapeBitch.c_code()

    return bytecode

@addToClass(AST.TokenNode)
def compile(self):
    bytecode = ""
    bytecode += self.tok
    return bytecode


if __name__ == "__main__":
    import sys,os
    from parser1 import parse
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    print(ast)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0] + '.c'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()
    print ("Wrote output to", name)
