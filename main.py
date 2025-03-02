from ply.lex import lex
from ply.yacc import yacc

# --- Lexer

tokens = ('RECOGER', 'SALIR', 'DE', 'LLEVAR', 
          'AVANZAR', 'ESQUIVAR', 'GOLPEAR', 'CON', 
          'ENTREGAR', 'OBJECT_KEYWORD', 'WHITESPACE')

# Ignored characters
t_WHITESPACE = r'\s+'

# Token matching rules are written as regexs
t_RECOGER = r'RECOGER'
t_SALIR = r'SALIR'
t_DE = r'DE'
t_LLEVAR = r'LLEVAR'
t_AVANZAR = r'AVANZAR'
t_ESQUIVAR = r'ESQUIVAR'
t_GOLPEAR = r'GOLPEAR'
t_CON = r'CON'
t_ENTREGAR = r'ENTREGAR'
t_OBJECT_KEYWORD = r'[a-z]+' 

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored token with an action associated with it


# Error handler for illegal characters
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()

# Loop for data reading
result = ''
new_input = ''
while True:
    new_input = str(input('Enter Command > '))
    if not new_input:
        break
    result += new_input + ' '

result = result[:-1] 
lexer.input(result)

#
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
    #print('Token: ', tok, ' Type: ', type(tok))
    #print('Lineno: ', tok.lineno, ' Lexpos: ', tok.lexpos)

# LexToken(LPAREN,'(',1,0) The last number in the tuple represents the index in which 
# the character appears. The second one represents the line where it appears.
