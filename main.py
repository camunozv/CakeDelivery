##########################################################
##########################################################
###              LEXER IMPLEMENTATION                 ####
###               cake delivery game                  ####
##########################################################
##########################################################

from ply.lex import lex
from ply.yacc import yacc

tokens = ('RECOGER', 'SALIR', 'DE', 'LLEVAR', 
          'AVANZAR', 'ESQUIVAR', 'GOLPEAR', 'CON', 
          'ENTREGAR', 'OBJECT_KEYWORD', 'WHITESPACE')


# BASIC COMMANDS
# There's no associated action for these tokens.
t_RECOGER = r'RECOGER'
t_SALIR = r'SALIR'
t_DE = r'DE'
t_LLEVAR = r'LLEVAR'
t_AVANZAR = r'AVANZAR'
t_ESQUIVAR = r'ESQUIVAR'
t_GOLPEAR = r'GOLPEAR'
t_CON = r'CON'
t_ENTREGAR = r'ENTREGAR'

# OBJECT TOKEN
# The action here is to save the value of the object identifier.
def t_OBJECT_KEYWORD(t):
    r'[a-z]+' 
    t.value = str(t.value)
    return t

# NEWLINE COUNTER
# Counting newlines, however this is not necessary.
def t_ignore_newline(t):
    r'[\n]+'
    t.lexer.lineno += t.value.count('\n')

# WHITESPACE HANDLER
# Consumes any kind of whitespace
t_WHITESPACE = r'[\f\r\v\u0020\t]+'
    
# Error handler for illegal characters
# Unrecognized characters fall here.
# Observe that we don't have upper case letters; we've defined
# that the objects should always be in lower case.
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

# Tokenizer loop
token_list = []
while True:
    tokens = lexer.token()
    if not tokens: 
        break      # No more input
    token_list.append(tokens)

i = 0
for tokens in token_list:
    i += 1
    print(f'{i}', tokens)
# LexToken(LPAREN,'(',1,0) The last number in the tuple represents the index in which 
# the character appears. The second one represents the line where it appears.
