import ply.lex as lex
import ply.yacc as yacc

tokens = [

    'OR',
    'AND',
    'NAME',
    'INT',
    'STRING',
    'EQUALS',
    'DECLARE',
    'NOTEQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_OR_EQUAL',
    'LESS_OR_EQUAL',
    'L_BRACKET',
    'R_BRACKET',
    'PERCENT',
    'FILTER',
    'SEMICOLON',
    'DOT',
]

t_EQUALS = r'=='
t_DECLARE = r'='
t_NOTEQUAL = r'!='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GREATER_OR_EQUAL = r'>='
t_LESS_OR_EQUAL = r'<='
t_L_BRACKET = r'{'
t_R_BRACKET = r'}'
t_PERCENT = r'%'
t_FILTER = r'\|'
t_SEMICOLON = r':'
t_DOT = r'.'

t_ignore = r' '


def t_OR(t):
    r'or'
    t.type = 'OR'
    return t


def t_AND(t):
    r'and'
    t.type = 'AND'
    return t


def t_STRING(t):
    r'\"[a-zA-Z0-9 \t,().:;?!*=/<>{}+-]+\"'  # egy string. ami alfanumerikus karaktereken felül néhány speciális karaktert is tartalmazhat (a teljesség igénye nélkül)
    t.type = 'STRING'
    return t


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]+'
    t.type = 'NAME'
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Illegal character!")
    t.lexer.skip(1)


lexer = lex.lex()


def p_accepter(p):
    '''
    accepter : expression
             | empty
    '''
    print(run(p[1]))


def p_expression(p):
    '''
    expression : object
               | tag
    '''
    p[0] = p[1]


def p_object(p):
    '''
    object  : L_BRACKET L_BRACKET expression_2 R_BRACKET R_BRACKET
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])


def p_tag(p):
    '''
    tag : L_BRACKET PERCENT expression_2 PERCENT R_BRACKET
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])


def p_expression_2(p):
    '''
    expression_2 : expression_3
                 | filter
                 | var
                 | boolean
                 | not_condition
                 | less_great_condition
                 | nis
    '''
    p[0] = p[1]

def p_nis(p):
    '''
    nis : var_name
        | INT
        | STRING
    '''

def p_expression_3(p):
    '''
    expression_3 : expression_2 expression_2
    '''
    p[0] = (p[1], p[2])


def p_filter(p):
    '''
    filter : FILTER NAME expression_4
    '''
    p[0] = (p[1], p[2], p[3])


def p_var(p):
    '''
    var : var_name DECLARE nis
    '''
    p[0] = (p[1], p[2], p[3])


def p_var_name(p):
    '''
    var_name : NAME subname
    '''
    p[0] = (p[1], p[2])


def p_subname(p):
    '''
    subname : subsubname
             | empty
    '''
    p[0] = (p[1])


def p_subsubname(p):
    '''
    subsubname : DOT NAME
    '''
    p[0] = (p[1], p[2])


def p_boolean(p):
    '''
    boolean : nis OR nis
            | nis AND nis
            | nis EQUALS nis
    '''
    p[0] = (p[2], p[1], p[3])


def p_not_condition(p):
    '''
    not_condition : NAME NOTEQUAL nis
    '''
    p[0] = (p[1], p[2], p[3])


def p_less_great_condition(p):
    '''
    less_great_condition : NAME LESS_THAN INT
                         | NAME GREATER_THAN INT
                         | NAME LESS_OR_EQUAL INT
                         | NAME GREATER_OR_EQUAL INT
    '''
    p[0] = (p[1], p[2], p[3])


def p_expression_4(p):
    '''
    expression_4 : filter
                 | SEMICOLON
    '''
    p[0] = p[1]


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

'''
def p_error(p):
    print("Syntax error!")
'''

def run(p):
    print(p)

parser = yacc.yacc()


while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)
