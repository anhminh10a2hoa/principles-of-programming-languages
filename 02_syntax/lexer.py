import sys
import ply.lex
from datetime import datetime

# List of token names.   This is always required
tokens = (
    'WHITESPACE',
    'COMMENT',
    'VAR', 'IS', 'UNLESS', 'OTHERWISE', 'UNTIL', 'DO', 'DONE',
    'PROCEDURE', 'FUNCTION', 'RETURN', 'PRINT', 'END',
    'LPAREN', 'RPAREN', 'LSQUARE', 'RSQUARE', 'LCURLY', 'RCURLY',
    'APOSTROPHE', 'AMPERSAND', 'COMMA', 'DOT', 'EQ', 'LT', 'PLUS', 'MINUS', 'MULT', 'DIV',
    'STRING', 'DATE_LITERAL', 'INT_LITERAL', 'IDENT', 'FUNC_IDENT', 'PROC_IDENT', 'COLON'
)

# Reserved words
reserved = {
    'var': 'VAR',
    'is': 'IS',
    'unless': 'UNLESS',
    'otherwise': 'OTHERWISE',
    'until': 'UNTIL',
    'do': 'DO',
    'done': 'DONE',
    'procedure': 'PROCEDURE',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'print': 'PRINT',
    'end': 'END'
}

# Tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_APOSTROPHE = r"'"
t_AMPERSAND = r'&'
t_COMMA = r','
t_DOT = r'\.'
t_EQ = r'='
t_LT = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'

# Ignored characters
t_ignore_WHITESPACE = r'[ \n\r\t]+'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Comments
def t_COMMENT(t):
    r'\(%[^%]*%\)'
    pass

# Date literal
def t_DATE_LITERAL(t):
    r'\d{4}-\d{2}-\d{2}'
    try:
        datetime.strptime(t.value, '%Y-%m-%d')
    except ValueError:
        print("Error: Invalid date format:", t.value)
        sys.exit(1)
    return t

# String literal
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove quotes
    return t

# Integer literal
def t_INT_LITERAL(t):
    r'-?(0|[1-9][0-9]{0,2}(\'[0-9]{3})*|[1-9][0-9]*|(\'[0-9]{3})+)'    
    thousand_sep_count = t.value.count("'")
    if thousand_sep_count > 1 or (thousand_sep_count == 1 and len(t.value) % 4 != 0):
        print(f"line {t.lineno}: Malformed number: {t.value}")
        sys.exit(1)
    original_value = t.value.replace("'", "")  # Remove thousands separators
    t.value = int(original_value)  # Convert string to integer
    if abs(t.value) >= 10**12:
        print(f"line {t.lineno}: INT_LITERAL too large")
        sys.exit(1)
    return t


# Function identifier
def t_FUNC_IDENT(t):
    r'[A-Z][a-zA-Z0-9_]*'
    return t

# Procedure identifier
def t_PROC_IDENT(t):
    r'[A-Z][A-Z0-9_]{1,}'
    return t

# Identifier
def t_IDENT(t):
    r'[a-z][a-zA-Z0-9_]*\b'
    t.type = reserved.get(t.value, 'IDENT')  # Check for reserved words
    return t

# Error handling
def t_error(t):
    print("Illegal character '{}' at line {}".format(t.value[0], t.lexer.lineno))
    t.lexer.skip(1)

# Build the lexer
lexer = ply.lex.lex()
