##########################################################
##########################################################
###              LEXER IMPLEMENTATION                 ####
###               cake delivery game                  ####
##########################################################
##########################################################

from ply.lex import lex
from ply.yacc import yacc

# GENERAL TOKENS
tokens = ('RECOGER', 'SALIR', 'DE', 'LLEVAR',
          'AVANZAR', 'ESQUIVAR', 'GOLPEAR', 'CON',
          'ENTREGAR', 'GAME_OBJECT', 'WHITESPACE')

# BASIC COMMANDS
# There's no associated action for these tokens.
# Longer commands should be specified first, since
# they are intended to be tokenized first. This is
# maximal munch! :D
t_ESQUIVAR = r'ESQUIVAR'
t_ENTREGAR = r'ENTREGAR'
t_RECOGER = r'RECOGER'
t_GOLPEAR = r'GOLPEAR'
t_AVANZAR = r'AVANZAR'
t_LLEVAR = r'LLEVAR'
t_SALIR = r'SALIR'
t_CON = r'CON'
t_DE = r'DE'


# OBJECT TOKEN
# The action here is to save the value of the object identifier.
def t_GAME_OBJECT(t):
    r'[a-z]+'
    t.value = str(t.value)
    return t


# NEWLINE COUNTER
# Counting newlines, however this is not necessary.
# Since we are testing online one line per command.
# Uncomment it, if full testing program is required.
# def t_ignore_newline(t):
#    r'[\n]+'
#    t.lexer.lineno += t.value.count('\n')


# WHITESPACE HANDLER
# Consumes any kind of whitespace
t_WHITESPACE = r'[\f\r\v\u0020\t]+'


# Error handler for illegal characters
# Unrecognized characters fall here.
# Observe that we don't have upper case letters; we've defined
# that the objects should always be named with lower case letters.
def t_error(t):
    print(f'Illegal character found {t.value[0]!r}')
    t.lexer.skip(1)


# There's no need, I think, for EOF handling. However, it could be
# included if necessary.

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

result = result[:-1]  # delete end of line whitespace
lexer.input(result)  # fully tokenize input

# Save and print all tokens
token_list = []
i = 0
for tokens in lexer:
    i += 1
    token_list.append(tokens)
    print(f'{i}', tokens)