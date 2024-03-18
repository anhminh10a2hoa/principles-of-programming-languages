import ply.yacc as yacc
import ply.lex
from lexer import tokens

# Helper function to print accepted symbols
symbolnum = 0

def debug_syntax(p):
    global symbolnum
    symbolnum = symbolnum + 1
    p[0] = symbolnum
    msg = ""
    for i, s in enumerate(p.slice):
        if s is not None:
            if type(s) is ply.lex.LexToken:
                msg = msg + str(s.type) + "<" + str(s.value) + "> "
            else:
                msg = msg + str(s) + "(" + str(p[i]) + ") " 
        else:
            msg = msg + "?? "
        if i == 0:
            msg = msg + ":: "
    print(msg)


# Grammar rules
def p_program(p):
    '''program : opt_definitions statement_list'''
    debug_syntax(p)

def p_opt_definitions_empty(p):
    '''opt_definitions : empty'''
    debug_syntax(p)

def p_opt_definitions(p):
    '''opt_definitions : definitions'''
    debug_syntax(p)

def p_variable_definition(p):
    '''variable_definition : VAR IDENT EQ expression'''
    debug_syntax(p)

def p_definitions(p):
    '''definitions : function_definition
                   | procedure_definition
                   | variable_definition'''
    debug_syntax(p)

def p_opt_var_defs_empty(p):
    '''opt_var_defs : empty'''
    debug_syntax(p)

def p_opt_var_defs(p):
    '''opt_var_defs : variable_definition opt_var_defs'''
    debug_syntax(p)

def p_function_definition(p):
    '''function_definition : FUNCTION FUNC_IDENT LCURLY opt_formals RCURLY RETURN IDENT opt_var_defs IS statement_list END FUNCTION'''
    debug_syntax(p)

def p_procedure_definition(p):
    '''procedure_definition : PROCEDURE PROC_IDENT LCURLY opt_formals RCURLY opt_return opt_var_defs IS statement_list END PROCEDURE'''
    debug_syntax(p)

def p_opt_formals_empty(p):
    '''opt_formals : empty'''
    debug_syntax(p)

def p_opt_formals(p):
    '''opt_formals : formal_arg_list'''
    debug_syntax(p)

def p_formal_arg_list(p):
    '''formal_arg_list : formal_arg
                       | formal_arg_list COMMA formal_arg'''
    debug_syntax(p)

def p_formal_arg(p):
    '''formal_arg : IDENT COLON IDENT'''
    debug_syntax(p)

def p_opt_return_empty(p):
    '''opt_return : empty'''
    debug_syntax(p)

def p_opt_return(p):
    '''opt_return : RETURN IDENT'''
    debug_syntax(p)


def p_statement_list(p):
    '''statement_list : statement
                      | statement_list COMMA statement'''
    debug_syntax(p)

def p_statement(p):
    '''statement : procedure_call
                 | assignment
                 | print_statement
                 | do_until_statement
                 | do_unless_statement
                 | return_statement'''
    debug_syntax(p)

def p_procedure_call(p):
    '''procedure_call : PROC_IDENT LPAREN opt_arguments RPAREN'''
    debug_syntax(p)

def p_opt_arguments_empty(p):
    '''opt_arguments : empty'''
    debug_syntax(p)

def p_opt_arguments(p):
    '''opt_arguments : arguments'''
    debug_syntax(p)

def p_arguments(p):
    '''arguments : expression
                 | arguments COMMA expression'''
    debug_syntax(p)

def p_assignment(p):
    '''assignment : lvalue EQ rvalue'''
    debug_syntax(p)

def p_lvalue(p):
    '''lvalue : IDENT
              | IDENT DOT IDENT'''
    debug_syntax(p)

def p_rvalue(p):
    '''rvalue : expression
              | unless_expression'''
    debug_syntax(p)

def p_print_statement(p):
    '''print_statement : PRINT print_item_list'''
    debug_syntax(p)

def p_print_item_list(p):
    '''print_item_list : print_item
                       | print_item_list AMPERSAND print_item'''
    debug_syntax(p)

def p_print_item(p):
    '''print_item : STRING
                  | expression'''
    debug_syntax(p)

def p_do_until_statement(p):
    '''do_until_statement : DO statement_list UNTIL expression'''
    debug_syntax(p)

def p_do_unless_statement(p):
    '''do_unless_statement : DO statement_list UNLESS expression opt_otherwise DONE'''
    debug_syntax(p)

def p_opt_otherwise_empty(p):
    '''opt_otherwise : empty'''
    debug_syntax(p)

def p_opt_otherwise(p):
    '''opt_otherwise : OTHERWISE statement_list'''
    debug_syntax(p)

def p_return_statement(p):
    '''return_statement : RETURN expression'''
    debug_syntax(p)

def p_expression(p):
    '''expression : simple_expr
                  | expression EQ simple_expr
                  | expression LT simple_expr'''
    debug_syntax(p)

def p_simple_expr(p):
    '''simple_expr : term
                   | simple_expr PLUS term
                   | simple_expr MINUS term'''
    debug_syntax(p)

def p_term(p):
    '''term : factor
            | term MULT factor
            | term DIV factor'''
    debug_syntax(p)

def p_factor(p):
    '''factor : MINUS atom
              | PLUS atom
              | atom'''
    debug_syntax(p)

def p_atom(p):
    '''atom : IDENT
            | IDENT APOSTROPHE IDENT
            | INT_LITERAL
            | DATE_LITERAL
            | function_call
            | procedure_call
            | LPAREN expression RPAREN'''
    debug_syntax(p)

def p_function_call(p):
    '''function_call : FUNC_IDENT LPAREN opt_arguments RPAREN'''
    debug_syntax(p)

def p_unless_expression(p):
    '''unless_expression : DO expression UNLESS expression opt_otherwise DONE'''
    debug_syntax(p)

# Empty production
def p_empty(p):
    '''empty : '''
    debug_syntax(p)

# Error rule for syntax errors
def p_error(p):
    raise SystemExit(f"{p.lineno}: Syntax Error (token: '{p.value}')")

# Build the parser
parser = yacc.yacc()
