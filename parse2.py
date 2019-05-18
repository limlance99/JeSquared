import ply.lex as lex
import ply.yacc as yacc
import sys


tokens = ['INT',    # Data Types: int and float
        'FLOAT',
        'TYPEINT',
        'TYPEFLOAT',
        'PERCENTINT',
        'PERCENTFLOAT',
        'NAME',     # Variable Name
        'PLUS',     # PEMDAS  + - * / = ( )
        'MINUS',
        'DIVIDE',
        'MULTIPLY',
        'EXP',
        'EQUALS',
        'OPENPAR', 
        'CLOSEPAR',
        'OPENCURL',
        'CLOSECURL',
        'EOL',      # End of Line
        'RETURN',   # Return from Function
        'FNAME',      
        'COMMENT',  # Comments
        'INPUT',    # Input Function Only Accepts One Character at a Time
        'OUTPUT',
        'COMMA',
        'AMP',
        'QUOTEMARK',
        'AND',       # Logical Operators
        'OR',    
        'NOT',
        'EQ',        # Comparison Operators
        'NEQ',
        'LSS',
        'GTR',
        'LEQ',
        'GEQ',
        #RESERVED
        'IF',       # Conditionals and Iterators
        'ELSE',
        'WHILE',
        'NEWLINE',
        'BREAK'
] 
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EXP = r'\^'
t_EQ = r'=='
t_NEQ = r'!='
t_LSS = r'\<'
t_GTR = r'\>'
t_LEQ = r'<='
t_GEQ = r'>='
t_EQUALS = r'\='
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_OPENCURL = r'\{'
t_CLOSECURL = r'\}'
t_COMMA = r'\,'
t_QUOTEMARK = r'\"'
t_AMP = r'\&'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_ignore = ' \t'
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_TYPEFLOAT(t):
    r'lut4n6'
    return t
def t_TYPEINT(t):
    r'b174n6'
    return t
def t_PERCENTFLOAT(t):
    r'%f'
    return t
def t_PERCENTINT(t):
    r'%d'
    return t

def t_NAME(t):
    r'j3j3[a-zA-Z_][a-zA-Z_0-9]*' 
    return t
def t_FNAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*m0n'
    return t
def t_EOL(t):
    r'p0h'
    return t
def t_BREAK(t):
    r's1r4'
    return t
def t_RETURN(t):
    r'b471k'
    return t
def t_COMMENT(t):
    r'\$.*'
    pass           # It has no return value so discard the token.
def t_INPUT(t):
    r'p450k'
    return t
def t_OUTPUT(t):
    r'l4b45'
    return t
def t_IF(t):
    r'kUn6'
    return t
def t_ELSE(t):
    r'ed1'
    return t
def t_WHILE(t):
    r'h4b4n6'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Invalid token at line: ", t.lineno)
    print(t.value)
    t.lexer.skip(1)


lexer = lex.lex()
precedence = (  # PEMDAS => Comparison Operators => Logical Operators
    ('right','NOT'),        
    ('left','AND','OR'),
    ('left','EQ','NEQ','LSS','GTR','LEQ','GEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left','MULTIPLY' ,'DIVIDE'),
    ('left', 'EXP')
)

# Grammar Rules

def p_begin(p):#START 
    '''
    begin : function
    '''
    p[0] = p[1]

def p_function(p):
    '''
    function : function funcname OPENCURL code RETURN expression EOL CLOSECURL
             | empty
    '''
    # CHECK DATA TYPE OF EXPRESSION 


    if len(p) > 2:
        p[0] = ("func", p[1], p[2], p[4], p[6])
        #       function , funcname, code, expression
    else:
        p[0] = p[1]

    run(p[0])

def p_funcname(p):
    '''
    funcname : datatype FNAME OPENPAR parameters CLOSEPAR 
    '''

    # global VarStack
    # VarStack.append({})
    
    p[0] = (id(p[1]), p[4])

def p_parameters(p):
    '''
    parameters : vardeclare COMMA parameters
                | vardeclare
                | empty
    '''
    if len(p) > 2:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]

def p_code(p): 
    '''
    code : code vardeclare EOL 
        | code varassign EOL
        | code io EOL
        | code expression EOL
        | code while 
        | code if
        | empty
    '''
    if len(p) > 2:
        p[0] = ("code", p[1], p[2])
    print(p[1])

def p_io(p):
    '''
    io : INPUT OPENPAR iodatain CLOSEPAR
        | OUTPUT OPENPAR iodataout CLOSEPAR
    '''
    p[0] = (p[1],p[3])
#def p_io_error(p):
#    'io : inputoutput error '
#    print("Error in I/O Statement: Bad Expression")
def p_iodatain(p): # "%d" , var OR "%f" , &var 
    '''
    iodatain : QUOTEMARK percenttype QUOTEMARK COMMA AMP NAME
    '''
    p[0] = (p[2],p[6]) # check if %d/%f == NAME datatype
def p_iodataout(p): # "%d" , var OR "%f" , &var 
    '''
    iodataout : QUOTEMARK percenttype QUOTEMARK COMMA NAME
    '''
    p[0] = (p[2],p[5]) # check if %d/%f == NAME datatype
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

def p_bool(p):
    '''
    bool : expression boolop expression
         | bool boolop bool
         | expression boolop bool
         | bool boolop expression
         | NOT bool
         | OPENPAR bool CLOSEPAR
    '''
    if len(p) < 4:
        p[0] = (p[2],p[1])
    else:
        p[0] = (p[2],p[1],p[3])

def p_boolop(p):
    '''
    boolop : EQ
           | NEQ
           | LSS
           | GTR
           | LEQ
           | GEQ
           | AND
           | OR
    '''
    p[0] = p[1]  
def p_if(p):
    '''
    if : IF OPENPAR bool CLOSEPAR block else
       | IF OPENPAR bool CLOSEPAR block 
    '''
    if len(p) > 6:
        p[0]=('if_else',p[3], p[5], p[6])
    else:
        p[0]=('if',p[3], p[5])
    
def p_else(p):
    '''
    else : ELSE block
    '''
    p[0] = p[2]

def p_while(p):
    '''
    while : WHILE OPENPAR bool CLOSEPAR block

    '''
    p[0]=('while',p[3],p[5])

def p_block(p): #control block (while, if-else, regular statements)
    '''
    block : OPENCURL while CLOSECURL
        |   OPENCURL if CLOSECURL
        |   OPENCURL bcode CLOSECURL
    '''
    p[0] = p[2]

def p_bcode(p): #NESTED REGULAR STATEMENTS
    '''
    bcode : bcode io EOL
        | bcode expression EOL
        | bcode BREAK EOL
        | empty
    '''
    if len(p) > 2:
        p[0] = ('code', p[1], p[2])
    print(p[1])


def p_expression_math(p):
    '''
    expression :  expression oper expression
               |  OPENPAR expression CLOSEPAR
    '''
    p[0] = (p[2],p[1],p[3])
    print(p[0])

def p_oper(p):
    '''
    oper :  EXP
         |  MULTIPLY
         |  DIVIDE
         |  PLUS
         |  MINUS
         |  EQUALS 
    '''
    p[0] = p[1]

def p_vardeclare(p):   #declare a variable  
    '''
    vardeclare : datatype NAME
    '''
    # global VarStack
    # VarStack[-1][p[2]] = -1                  #default value of -1
    p[0] = ('var', id(p[1]),p[2])   #to add:if p in varlist??
    print(p[0])

def p_varassign(p):
    '''
    varassign : NAME EQUALS expression
               | NAME EQUALS NAME
    '''
    # ERROR REMEMBER TO ADD THIS ERROR TO NOT COMPILE LIST
    p[0] = ('=', p[1],p[3])
    print(p[0])

def p_expression_function(p):
    '''
    expression : FNAME OPENPAR varname CLOSEPAR 
    '''
    p[0] = (p[1], p[3])

def p_varname(p):
    '''
    varname : NAME COMMA varname
            | NAME
            | empty
    '''
    if len(p) > 2:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]
        

def id(s):                          #identifies data type of NAME
    if s == 'b174n6':
        return 'INT'
    elif s=='lut4n6':
        return 'FLOAT'
    else:
        return 'STRING'

def p_expression_int_float(p):
    '''
    expression  : INT
                | FLOAT
                | NAME
    '''
    p[0] = p[1]

def p_empty(p):       
    '''
    empty : 
    '''
    p[0] = None
def p_error(p):
    print("Syntax error at line:", p.lineno)
    #print(p)
    #look for terminating 'p0h'
    tok = parser.token()
    if not tok or tok.type == 'EOL': 
        print("p0h not found at end of expression.")
    return tok

parser = yacc.yacc()

VarStack = []
# Executing Code

def run(p):
    global VarStack
    # print("Current p: ", p)
    if type(p) == tuple:
        if p[0] == '+':
            try: 
                return run(p[1]) + run(p[2])
            except TypeError:
                print("Unsupported operand type(s) for " + p[1] +" and " + p[2] + ".")
        elif p[0] == '-':
            try:
                return run(p[1]) - run(p[2])
            except TypeError:
                print("Unsupported operand type(s) for " + p[1] +" and " + p[2] + ".")
        elif p[0] == '*':
            try: 
                return run(p[1]) * run(p[2])
            except TypeError:
                print("Unsupported operand type(s) for " + p[1] +" and " + p[2] + ".")
        elif p[0] == '/':
            try: 
                return run(p[1]) / run(p[2])
            except TypeError:
                print("Unsupported operand type(s) for " + p[1] +" and " + p[2] + ".")
            except ZeroDivisionError:
                print("Division by 0.")
        elif p[0] == '^':
            try: 
                return run(p[1])**run(p[2])
            except TypeError:
                print("Unsupported operand type(s) for " + p[1] +" and " + p[2] + ".")
        elif p[0] == '==':
            return run(p[1]) == run(p[2])
        elif p[0] == '!=':
            return run(p[1]) != run(p[2])
        elif p[0] == '<':
            return run(p[1]) < run(p[2])
        elif p[0] == '>':
            return run(p[1]) > run(p[2])
        elif p[0] == '<=':
            return run(p[1]) <= run(p[2])
        elif p[0] == '>=':
            return run(p[1]) >= run(p[2])
        elif p[0] == '&&':
            return run(p[1]) and run(p[2])
        elif p[0] == '||':
            return run(p[1]) or run(p[2])
        elif p[0] == '!':
            return not run(p[1]) 
        elif p[0] == 'if':
            if run(p[1]) is True:
                run(p[2])
        elif p[0] == 'if_else':
            if run(p[1]):
                run(p[2])
            else:
                run(p[3])
        elif p[0] == 'while':
            run(p[1])
            run(p[2])

        elif p[0] == 'code':
            run(p[1]) # recursive step
            run(p[2]) # runs lines of code

        elif p[0] == "func":
            run(p[1]) # recursive step
            VarStack.append({})

            run(p[3]) # runs the code
            if (p[2][1] == 'INT' and type(run(p[4])) != int) or (p[2][1] == 'FLOAT' and type(run(p[4])) != float):
                print("invalid return value (must be %s)" %p[2][1])

            VarStack.pop()

        elif p[0] == 'var':
            if p[2] in VarStack[-1].keys():
                print(p[2] + " has already been declared") 
            else:    
                VarStack[-1][p[2]] = -1

        elif p[0] == '=':
            if p[1] not in VarStack[-1].keys():
                print("Undeclared Variable", p[1])
            else:
                VarStack[-1][p[1]] = run(p[2])
    else:
        if VarStack:                                # if i have things in my stack
            if type(p) == str:                      # if its a string then ill check if its in the stack
                if p in VarStack[-1].keys():
                    return VarStack[-1][p]
                else:
                    print("Undeclared Variable", p)  # hardcoded typechecking
        elif type(p) == str:
            print("Undeclared Variable", p)
        return p 

f = input("Enter j3j3 File Name: ")
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
    i = 0
    while 1:
        try:
            s = inp.read()
            if s == "":
                break
        except EOFError:
            print("Done reading File.")
            break
        parser.parse(s)

        


