import ply.lex as lex
import ply.yacc as yacc
from translate import translate 
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
        'MODULO',
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
t_EQ = r'=='
t_NEQ = r'!='
t_LEQ = r'<='
t_GEQ = r'>='
t_LSS = r'\<'
t_GTR = r'\>'
t_AND = r'&&'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_MODULO = r'\%'
t_DIVIDE = r'\/'
t_EXP = r'\^'

t_EQUALS = r'\='
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_OPENCURL = r'\{'
t_CLOSECURL = r'\}'
t_COMMA = r'\,'
t_QUOTEMARK = r'\"'
t_AMP = r'\&'

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
def t_FNAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*m0n'
    return t
def t_NAME(t):
    r'j3j3[a-zA-Z_][a-zA-Z_0-9]*' 
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
    global errors
    global SynError
    print("Line %d: Invalid token." %t.lineno)
    t.lexer.skip(1)
    errors += 1
    SynError = True


lexer = lex.lex()
precedence = (  # PEMDAS => Comparison Operators => Logical Operators
    ('right','NOT'),        
    ('left','AND','OR'),
    ('left','EQ','NEQ','LSS','GTR','LEQ','GEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left','MULTIPLY' ,'DIVIDE'),
    ('left','MODULO'),
    ('left', 'EXP')
)

# Grammar Rules

def p_begin(p):#START 
    '''
    begin : function
    '''
    global Runner
    p[0] = p[1]
    Runner = p[0]

def p_function(p):
    '''
    function : function funcname OPENCURL code return EOL CLOSECURL
             | empty
    '''
    # CHECK DATA TYPE OF EXPRESSION 

    if len(p) > 2:
        p[0] = ("func", p[1], p[2], p[4], p[5], p.lexer.lineno)
        #       function , funcname, code, expression
        
    else:
        p[0] = p[1]

def p_e1(p):
    '''
    function : function funcname error
             | function funcname OPENCURL code error
             | function funcname OPENCURL code return error
             | function funcname OPENCURL code return EOL error
    '''
    if len(p) == 4:
        print("(Expected '{').")
    if len(p) == 6:
        print("(Function has no return statement).")
    if len(p) == 7:
        print("(Expected 'p0h' at end of previous expression).")
    if len(p) == 8:
        print("(Expected '}').")

def p_funcname(p):
    '''
    funcname : datatype FNAME OPENPAR parameters CLOSEPAR 
    '''

    # global VarStack
    # VarStack.append({})
    
    p[0] = ('funcname', id(p[1]), p[4], p[2],p.lexer.lineno)

def p_e2(p):
    '''
    funcname : datatype error 
             | datatype FNAME error 
             | datatype FNAME parameters error
    
    '''    
    if len(p) == 3:
        print("(Expected function name).")
    if len(p) == 4:
        print("(Expected '(').")
    if len(p) == 6:
        print("(Expected ')').")

def p_parameters(p):
    '''
    parameters : vardeclare COMMA parameters
                | vardeclare
                | empty
    '''
    if len(p) > 2:
        p[0] = ('parameters', p[1], p[3], p.lexer.lineno)
    else:
        p[0] = ('parameters', p[1], p.lexer.lineno)

def p_e3(p):
    '''
    parameters : vardeclare error
               | vardeclare COMMA error
    '''
    if len(p) == 3:
        print("(No ',' found).")
    if len(p) == 4:
        print("(Unwanted ',' found).")

def p_code(p): 
    '''
    code : code vardeclare EOL 
        | code varassign EOL
        | code io EOL
        | code expression EOL
        | code while 
        | code if
        | code return EOL
        | empty
    '''
    if len(p) > 2:
        p[0] = ("code", p[1], p[2])

def p_e3(p):
    '''
    code : code vardeclare error 
        | code varassign error
        | code io error
        | code expression error
    '''
    print("(Expected 'p0h' at end of previous expression).")

def p_return(p):
    '''
    return : RETURN expression
    '''
    p[0] = ('return', p[2], p.lexer.lineno)

def p_e4(p):
    '''
    return : RETURN error
    '''
    print("(Missing return value).")

def p_io(p):
    '''
    io : INPUT OPENPAR QUOTEMARK percenttype QUOTEMARK COMMA AMP NAME CLOSEPAR
        | OUTPUT OPENPAR QUOTEMARK percenttype QUOTEMARK COMMA NAME CLOSEPAR
    '''
    if len(p) > 9:
        p[0] = ('io', p[4], p[8], p.lexer.lineno)
    else:
        p[0] = ('io', p[4], p[7], p.lexer.lineno)

def p_e5(p):
    '''
    io : INPUT error
       | OUTPUT error
       | INPUT OPENPAR error
       | OUTPUT OPENPAR error
       | INPUT OPENPAR QUOTEMARK error
       | OUTPUT OPENPAR QUOTEMARK error
       | INPUT OPENPAR QUOTEMARK percenttype error
       | OUTPUT OPENPAR QUOTEMARK percenttype error
       | INPUT OPENPAR QUOTEMARK percenttype QUOTEMARK error
       | OUTPUT OPENPAR QUOTEMARK percenttype QUOTEMARK error
       | INPUT OPENPAR QUOTEMARK percenttype QUOTEMARK COMMA error
       | OUTPUT OPENPAR QUOTEMARK percenttype QUOTEMARK COMMA error  
    '''
    if len(p) == 3:
        print("(Expected '(').")
    if len(p) == 4 or len(p) == 6:
        print("(Expected quotation marks).")
    if len(p) == 5:
        print("(Expected formatting).")
    if len(p) == 7:
        print("(Expected ',').")
    if len(p) == 8:
        print("(Expected variable name).")

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

def p_e6(p):
    '''
    bool : expression error
         | bool error
         | expression boolop error
         | bool boolop error
         | NOT error
    '''
    print("(Invalid boolean expression).")

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
   
def p_e7(p):
    '''
    if : IF error
    ''' 
    print("(Expected boolean statement).")

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

def p_e8(p):
    '''
    while : WHILE error
    ''' 
    print("(Expected boolean statement).")        

def p_block(p): #control block (while, if-else, regular statements)
    '''
    block : OPENCURL bcode CLOSECURL
    '''
    p[0] = p[2]

def p_e9(p):
    '''
    block : error
    '''
    print("(Expected '{').")
    

def p_bcode(p): #NESTED REGULAR STATEMENTS
    '''
    bcode : bcode io EOL
        | bcode varassign EOL
        | bcode while
        | bcode if
        | bcode expression EOL
        | bcode BREAK EOL
        | bcode return EOL
        | empty
    '''
    if len(p) > 2:
        p[0] = ('code', p[1], p[2])
    else:
        p[0] = (p[1])

def p_e10(p):
    '''
    bcode : bcode BREAK error 
          | bcode varassign error
          | bcode io error
          | bcode expression error
          | bcode return error
    '''
    print("(Expected 'p0h' at end of previous expression).")

def p_expression_math(p):
    '''
    expression :  expression oper expression
               |  OPENPAR expression CLOSEPAR
    '''
    p[0] = (p[2],p[1],p[3], p.lexer.lineno)
    #print(p[0])

def p_e11(p):
    '''
    expression : expression oper error
    '''
    print("(Invalid expression).")

def p_expression_int_float(p):
    '''
    expression  : INT
                | FLOAT
                | NAME
    '''
    p[0] = p[1]

def p_expression_function(p):
    '''
    expression : FNAME OPENPAR varname CLOSEPAR 
    '''
    p[0] = ('funcall', p[1], p[3], p.lexer.lineno)

def p_e12(p):
    '''
    expression : FNAME error
               | FNAME OPENPAR varname error
    '''
    if len(p) == 3:
        print("(Expected '(').")
    if len(p) == 5:
        print("(Expected ')').")
    
def p_oper(p):
    '''
    oper :  EXP
        | MODULO
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
    p[0] = ('var', id(p[1]),p[2],p.lexer.lineno)   

def p_e13(p):
    '''
    vardeclare : datatype error
    '''
    print("(Expected variable name).")
    
def p_varassign(p):
    '''
    varassign : NAME EQUALS expression
    '''
    p[0] = ('=', p[1],p[3],p.lexer.lineno)
    
def p_e14(p):
    '''
    varassign : NAME EQUALS error
    '''
    print("(Expected assignment expression).")

def p_varname(p):
    '''
    varname : NAME COMMA varname
            | NAME
            | empty
    '''
    if len(p) > 2:
        p[0] = ('varname', p[1], p[3], p.lexer.lineno)
    else:
        p[0] = ('varname', p[1], p.lexer.lineno) 

def p_e15(p):
    '''
    varname : error
    '''
    print("(Invalid parameters passed).")
        

def id(s):                          #identifies data type of NAME
    if s == 'b174n6':
        return 'INT'
    elif s=='lut4n6':
        return 'FLOAT'
    else:
        return 'STRING'


def p_empty(p):       
    '''
    empty : 
    '''
    p[0] = None

def p_error(p):
    global errors
    global SynError
    if p:
        print("Line %d: Syntax Error" %p.lexer.lineno, end=' ')
    else:
        print("Syntax Error (no '}' found at EOF).")
    errors += 1
    SynError = True

parser = yacc.yacc()

VarStack = []
FuncTypes = {}
FuncPmtrs = {}
errors = 0
index = 0
SynError = False
checkName = ''
Runner = 0

# Executing Code

def run(p):
    global VarStack
    global FuncTypes
    global FuncPmtrs
    global errors
    global index
    global checkName
    #print(FuncTypes)
    #print("Current p: ", p)
    if type(p) == tuple:
        if p[0] in '+-*^':
            run1 = run((p[1]))
            run2 = run((p[2]))
            temp1 = type(run1)
            temp2 = type(run2)

            if temp1 == str or temp2 == str:
                    print("Line %d: Cannot '%s' (undeclared variable)." %(p[-1], p[0]))
            elif temp1 != temp2: 
                print("Line %d: Cannot '%s' (different data type)." %(p[-1], p[0]))
                errors += 1
            else:
                return run1 + run2

        elif p[0] == '/':
            run1 = run((p[1]))
            run2 = run((p[2]))
            temp1 = type(run1)
            temp2 = type(run2)

            if temp1 == str or temp2 == str:
                    print("Line %d: Cannot '%s' (undeclared variable)." %(p[-1], p[0]))
            elif temp1 == int and temp2 == float:
                print("Line %d: Cannot '%s' (different data type)." %(p[-1], p[0]))
                errors += 1
            elif temp1 == int and temp2 == int: 
                try: 
                    return run1 // run2
                except ZeroDivisionError:
                    print("Line %d: Division by 0." %p[-1])
                    errors += 1
            else: 
                try: 
                    return run1 / run2
                except ZeroDivisionError:
                    print("Line %d: Division by 0." %p[-1])
                    errors += 1
            

        elif p[0] == '%':
            run1 = run((p[1]))
            run2 = run((p[2]))
            temp1 = type(run1)
            temp2 = type(run2)

            if temp1 == str or temp2 == str:
                    print("Line %d: Cannot '%s' (undeclared variable)." %(p[-1], p[0]))
            elif temp1 != int or temp2 != int:
                print("Line %d: Cannot '%s' (different data type)." %(p[-1], p[0]))
                errors += 1
            else:
                return run1 % run2

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
            run(p[1])
            run(p[2])
        elif p[0] == 'if_else':
            run(p[1])
            run(p[2])
            run(p[3])
        elif p[0] == 'while':
            run(p[1])
            run(p[2])

        elif p[0] == 'code':
            run(p[1]) # recursive step
            run(p[2]) # runs lines of code

        elif p[0] == 'io':
            if p[1] == '%d' and type(run(p[2])) != int:
                print("Line %d: Invalid format (MUST BE INT)" %p[-1])
                errors += 1
            elif p[1] == '%f' and type(run(p[2])) != float:
                print("Line %d: Invalid format (MUST BE FLOAT)" %p[-1])
                errors += 1

        elif p[0] == 'funcall':
            if p[1] not in FuncTypes:
                print("Line %d: function %s has not yet been declared." %(p[-1], p[1]))
                errors += 1
            else:
                index = 0
                checkName = p[1]
                run(p[2])
                if FuncTypes[p[1]] == "INT":
                    return 0
                elif FuncTypes[p[1]] == "FLOAT":
                    return 0.0

        elif p[0] == 'funcname':
            if p[3] in FuncPmtrs:
                print("Line %d: Function %s has already been declared." %(p[-1], p[3]))
                errors += 1
            else:
                FuncTypes[p[3]] = p[1]
                
                FuncPmtrs[p[3]] = []
                
                run(p[2])

        elif p[0] == 'parameters':
            run(p[1])
            temp = [i for i in FuncPmtrs.keys()]
            if p[1] != None:
                if p[1][1] == 'INT':
                    FuncPmtrs[temp[-1]].append(int)                   # data type
                elif p[1][1] == 'FLOAT':
                    FuncPmtrs[temp[-1]].append(float)                   # data type
                
            if len(p) > 3:
                index += 1
                run(p[2])


        elif p[0] == 'varname':
            run1 = run(p[1])
            type1 = type(run1)  

            if index == len(FuncPmtrs[checkName]):
                print("Line %d: Too many parameters passed." %p[-1])
                errors += 1
            else:
                if type1 == str:
                    print("Line %d: Undeclared Variable %s." %(p[-1], p[1]))
                    errors += 1
                elif FuncPmtrs[checkName][index] != type1 and p[1] != None:
                    print("Line %d: Incorrect data type passed for variable %s." %(p[-1], p[1]))
                    errors += 1

                if len(p) > 3:
                    index += 1
                    run(p[2])

                elif index < len(FuncPmtrs[checkName]) - 1 or (p[1] == None and len(FuncPmtrs[checkName]) >= 1):
                    print("Line %d: Not enough parameters passed." %p[-1])
                    errors += 1


        elif p[0] == 'return':
            temp = [i for i in FuncTypes.keys()]
            wow = FuncTypes[temp[-1]]
            if (wow == 'INT' and type(run(p[1])) != int) or (wow == 'FLOAT' and type(run(p[1])) != float):
                print("Line %d: Invalid return value (must be %s)" %(p[-1], wow))
                errors += 1


        elif p[0] == 'func':
            run(p[1])                       # recursive step
            VarStack.append({})             # creates new stack of variables
            
            run(p[2])                       # declares all parameters
            
            run(p[3])                       # runs the code
            run(p[4])
            
            VarStack.pop()

        elif p[0] == 'var':
            if p[2] in VarStack[-1].keys():
                print("Line %d: %s has already been declared." %(p[-1], p[2]))
                errors += 1 
            else:    
                if p[1] == 'INT':
                    VarStack[-1][p[2]] = 0
                elif p[1] == 'FLOAT':
                    VarStack[-1][p[2]] = 0.0

        elif p[0] == '=':
            if p[1] not in VarStack[-1].keys():
                print("Line %d: Undeclared variable %s." %(p[-1] , p[1]))
                errors += 1
            else:
                run2 = run((p[2]))
                temp2 = type(run2)

                if temp2 == str:
                    print("Line %d: Cannot assign (undeclared variable)." %p[-1])
                    errors += 1
                elif type(VarStack[-1][p[1]]) != temp2:
                    print("Line %d: Cannot assign (different data type)." %p[-1])
                    errors += 1
                else:
                    VarStack[-1][p[1]] = run2
    else:
        if VarStack and type(p) == str:      # if i have things in my stack                            
                if p in VarStack[-1].keys(): # if its a string then ill check if its in the stack
                    return VarStack[-1][p]
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
        if not SynError:
           run(Runner)
        print()
        if errors == 0:
            print("No errors found.")
            translate(f)
        else:
            if errors > 1:
                print("%d errors found.\nCould not create C file." %errors)
            else:
                print("%d error found.\nCould not create C file." %errors)
            

