import ply.yacc as yacc
from lex import tokens
import AST

def p_programme(p):
    '''programme : DEBUT_PROGRAMME FIN_LIGNE dessins FIN_PROGRAMME FIN_LIGNE'''
    p[0] = AST.ProgramNode(p[3])

def p_dessins(p):
    '''dessins : dessin'''
    p[0] = AST.DessinsNode(p[1])

def p_dessins_recursive(p):
    '''dessins : dessin dessins'''
    p[0] = AST.DessinsNode([p[1]] + p[2].children)


def p_dessin(p):
    '''dessin : type attributes FIN_LIGNE'''
    p[0] = AST.DessinNode([p[1],p[2]])

def p_type(p):
    '''type : DEBUT_LIGNE TEXTE'''
    srtType = AST.TokenNode(p[2])
    p[0] = AST.TypeNode(srtType)

def p_attributes(p):
    '''attributes : attribute'''
    p[0] = AST.AttributesNode(p[1])

def p_attributes_recursive(p):
    '''attributes : attribute attributes'''
    p[0] = AST.AttributesNode([p[1]] + p[2].children)


def p_attribute(p):
    '''attribute : TEXTE EGAL GUILLEMET VALEUR GUILLEMET'''
    texte = AST.TokenNode(p[1])
    valeur = AST.TokenNode(p[4])
    p[0] = AST.AttributeNode(texte,valeur)

def p_error(p):
    print("Syntax error in line %d" % p.lineno)
    yacc.errok()

def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir='generated')


if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()
    result = parse(prog)
    print(result)

