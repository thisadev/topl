import ply.lex as lex
import ply.yacc as yacc

tokens = ('PRINT', 'ADD', 'SET', 'GET', 'STRING', 'NUMBER', 'IDENTIFIER')

t_PRINT = r'PRINT'
t_ADD = r'ADD'
t_SET = r'SET'
t_GET = r'GET'
t_STRING = r'\".*?\"'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character {t.value[0]} at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

variables = {}

def p_statement_print(p):
    "statement : PRINT STRING"
    print(p[2][1:-1])  
    
def p_statement_add(p):
    "statement : ADD NUMBER NUMBER"
    print(p[2] + p[3])

def p_statement_set(p):
    "statement : SET IDENTIFIER NUMBER"
    variables[p[2]] = p[3]

def p_statement_get(p):
    "statement : GET IDENTIFIER"
    value = variables.get(p[2], None)
    if value is not None:
        print(value)
    else:
        print(f"Variable '{p[2]}' is not defined")

def p_error(p):
    print("Syntax error!")

parser = yacc.yacc()

print("Welcome to KLang! Type 'exit' to quit.")
while True:
    try:
        code = input(">>> ")
        if code == "exit":
            break
        parser.parse(code)
    except Exception as e:
        print(f"Error: {e}")