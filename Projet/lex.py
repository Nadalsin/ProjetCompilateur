import ply.lex as lex

tokens = (
    'DEBUT_PROGRAMME', 'FIN_PROGRAMME', 'FIN_LIGNE', 'DEBUT_LIGNE', 'TEXTE', "ATTRIBUT", 'EGAL',"VALEUR"
)

def t_DEBUT_PROGRAMME(t):
        r'\<svg'
        return t

def t_FIN_PROGRAMME(t):
        r'\<\/svg'
        return t

def t_FIN_LIGNE(t):
        r'\>'
        t.lexer.lineno += len(t.value)
        return t

def t_EGAL(t):
        r'\='
        return t

def t_DEBUT_LIGNE(t):
        r'\<'
        return t

def t_TEXTE(t):
        r'[A-Za-z]+'
        return t

def t_VALEUR(t):
        r'\"\d+\.?\d*[A-Za-z]*\"'
        t.value = t.value.replace('"','')
        t.value = t.value.replace('px', '')
        return t

t_ignore = ' \n /'

def t_error(t):
        print("Illegal caracter '%s'" % t.value[0])
        t.lexer.skip(1)

lex.lex()

if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()

    lex.input(prog)

    while 1:
        tok = lex.token()
        if not tok: break
        print("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))