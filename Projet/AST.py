# coding: latin-1

''' AST.py, version 0.2

Petit module utilitaire pour la construction, la manipulation et la
reprÃ©sentation d'arbres syntaxiques abstraits.

SÃ»rement plein de bugs et autres surprises. Ã€ prendre comme un
"work in progress"...
Notamment, l'utilisation de pydot pour reprÃ©senter un arbre syntaxique cousu
est une utilisation un peu "limite" de graphviz. Ã‡a marche, mais le layout n'est
pas toujours optimal...

2008-2009, Matthieu Amiguet, HE-Arc
'''
import sys

sys.path.insert(0, './pydot-1.0.3')
sys.path.insert(0, './pyparsing-1.5.5')
import pydot


class Node:
    count = 0
    type = 'Node (unspecified)'
    shape = 'ellipse'

    def __init__(self, children=None):
        self.ID = str(Node.count)
        Node.count += 1
        if not children:
            self.children = []
        elif hasattr(children, '__len__'):
            self.children = children
        else:
            self.children = [children]

    def asciitree(self, prefix=''):
        result = "%s%s\n" % (prefix, repr(self))
        prefix += '|  '
        for c in self.children:
            if not isinstance(c, Node):
                result += "%s*** Error: Child of type %r: %r\n" % (prefix, type(c), c)
                continue
            result += c.asciitree(prefix)
        return result

    def __str__(self):
        return self.asciitree()

    def __repr__(self):
        return self.type

    def addNext(self, next):
        self.next.append(next)

    def makegraphicaltree(self, dot=None, edgeLabels=True):
        if not dot: dot = pydot.Dot()
        dot.add_node(pydot.Node(self.ID, label=repr(self), shape=self.shape))
        label = edgeLabels and len(self.children) - 1
        for i, c in enumerate(self.children):
            c.makegraphicaltree(dot, edgeLabels)
            edge = pydot.Edge(self.ID, c.ID)
            if label:
                edge.set_label(str(i))
            dot.add_edge(edge)
            # Workaround for a bug in pydot 1.0.2 on Windows:
            # dot.set_graphviz_executables({'dot': r'C:\Program Files\Graphviz2.16\bin\dot.exe'})
        return dot


class ProgramNode(Node):
    type = 'Program'


class TokenNode(Node):
    type = 'token'

    def __init__(self, tok):
        Node.__init__(self)
        self.tok = tok

    def __repr__(self):
        return repr(self.tok)


class DessinsNode(Node):
    type = "dessins"

# A FAIRE !!
class DessinNode(Node):
    type = "dessin"

    def __init__(self,children):
        Node.__init__(self,children)


class TypeNode(Node):
    type = "type"

class AttributesNode(Node):
    type = "attributes"


class AttributeNode(Node):
    type = "attribute"

    def __init__(self, attributeName, attributeValue):
        Node.__init__(self)
        self.attributeName = attributeName
        self.attributeValue = attributeValue

    def __repr__(self):
        return repr(self.attributeName)  + " = " + repr(self.attributeValue)

class EntryNode(Node):
    type = 'Entry'

    def __init__(self):
        Node.__init__(self,None)

def addToClass(cls):
    ''' Décorateur permettant d'ajouter la fonction décorée en tant que méthode
    à une classe.

    Permet d'implémenter une forme élémentaire de programmation orientée
    aspects en regroupant les méthodes de différentes classes implémentant
    une même fonctionnalité en un seul endroit.

    Attention, après utilisation de ce décorateur, la fonction décorée reste dans
    le namespace courant. Si cela dérange, on peut utiliser del pour la détruire.
    Je ne sais pas s'il existe un moyen d'éviter ce phénomène.
    '''

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator