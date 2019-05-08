import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = ['INT', #int and float: data types
        'FLOAT',
        'TYPEINT',
        'TYPEFLOAT',
        'PERCENTFLOAT',
        'PERCENTINT',
        'NAME',     #variable name
        'PLUS',     #arithmetic + - * /
        'MINUS',
        'DIVIDE',
        'MULTIPLY',
        'EQUALS',
        'EXP',
        'OPENPAR', 'CLOSEPAR',
        'EOL',   #end of line
        'RETURN',    #return from function
        'FUNCNAME',
        'COMMENT',
        'INPUT',    #input func only accepts one char at a time
        'OUTPUT',
        'COMMA',
        'QUOTEMARK',
        'AND'
]
t_COMMA = r'\,'
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EXP = r'\^'
t_EQUALS = r'\='
t_ignore = r' '
t_AND = r'\&'
t_QUOTEMARK=r' " '
def t_COMMENT(t):
    r'\$.*'
    pass
    #no return value, discard token
def t_EOL(t):
    r'p0h'
    return t
def t_PERCENTFLOAT(t):
    r'%f'
    return t
def t_TYPEFLOAT(t):
    r'lut4n6'
    return t
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_PERCENTINT(t):
    r'%d'
    return t
def t_TYPEINT(t):
    r'b174n6'
    return t
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_NAME(t):
    r'j3j3[a-zA-Z_][a-zA-Z_0-9]*'
    return t
def t_INPUT(t):
    r'p450k'
    return t
def t_OUTPUT(t):
    r'l4b45'
    return t
def t_error(t):
    print("Illegal character '%s' " %t.value[0])
    t.lexer.skip(len(t.value))
def t_newline(t):          #line number tracker
     r'\n+'
     t.lexer.lineno += len(t.value)

lexer = lex.lex()
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left','MULTIPLY' ,'DIVIDE'),
    ('left', 'EXP')
)

#Grammar Rules
def p_code(p):
    '''
    code : vardeclare EOL 
        | io EOL
        | expression EOL
        | empty
    '''
    p[0] = p[1]
    print(p[1])

def p_io(p):
    '''
    io : inputoutput OPENPAR iodata CLOSEPAR
    '''
    p[0] = (p[1],p[3])
def p_io_error(p):
    'io : inputoutput error '
    print("Error in I/O statement. Bad expression.")
def p_inputoutput(p):
    '''
    inputoutput : INPUT
                | OUTPUT
    '''
    p[0] = p[1]
def p_iodata(p): # "%d" , var OR "%f" , &var 
    '''
    iodata : QUOTEMARK percenttype QUOTEMARK COMMA AND NAME
    '''
    p[0] = (p[2],p[6]) # check if %d/%f == NAME datatype
def p_percenttype(p):
    '''
    percenttype : PERCENTFLOAT
                | PERCENTINT
    '''
    p[0] = p[1]
def p_datatype(p):
    '''
    datatype : TYPEFLOAT
            | TYPEINT
    '''
    p[0] = p[1]
def p_expression_math(p):
    '''
    expression : expression EXP expression
                | expression  MULTIPLY expression
                | expression DIVIDE expression
                | expression PLUS expression
                | expression MINUS expression
    '''
    p[0] = (p[2],p[1],p[3])
def p_expression_par(p):
    '''
    expression : OPENPAR expression CLOSEPAR
    '''
    p[0] = (p[2],p[1],p[3])
def p_vardeclare(p):   #declare a variable  
    '''
    vardeclare : datatype NAME
    '''
    global env
    p[0] = ('var', id(p[1]),p[2])   #to add:if p in varlist??
    env[p[2]] = -1          #default value of -1
def p_expression_var_assign(p):
    '''
    expression : NAME EQUALS expression
    '''
    # ERROR REMEMBER TO ADD THIS ERROR TO NOT COMPILE LIST
    if p[1] in env.keys():
        p[0] = ('=', p[1],p[3])
    else:
        print(p[1] + " not found in scope") 

def id(s):                          #identifies data type of NAME
    if s == 'b174n6':
        return 'INT'
    else:
        return 'FLOAT'
def p_expression_int_float(p):
    '''
    expression  :   INT
                | FLOAT
    '''
    p[0] = p[1]

def p_empty(p):       
    '''
    empty : 
    '''
    p[0] = None
def p_error(p):       #Error Handling
    print('Syntax error in input')
    #look for terminating 'p0h'
    tok = parser.token()
    if not tok or tok.type == 'EOL': 
        print("p0h not found at end of expression")
    return tok

parser = yacc.yacc()

env = {}
#this was for executing code but I dont know if we still need it so im keeping it lol
""" def run(p):
    global env
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == 'var':
            if p[1] not in env:
                return p[1] + ' undeclared'
            return env[p[1]]
        elif p[0] == '=':
            env[p[1]] = run(p[2])
            print(env)
    else:
        return p """
f = input("Enter j3j3 file name: ")
if(f == ""):        #testing for indiv statements
    while True:
        try:
            s = input('>> ')
            if(s == "exit()"):  #exit command line
                break
        except EOFError:
            break
        parser.parse(s)
else:               #there's a legit file u wanna read
    inp = open(f + ".txt","r")
    inp = [i for i in inp.readlines()]
    i = 0
    while i < len(inp):
        print(inp[i])  
        try:
            s = inp[i]
        except EOFError:
            break
        parser.parse(s)
        i+=1

        


