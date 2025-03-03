##########################################################
##########################################################
###              LEXER+PARSER IMPLEMENTATION          ####
###               cake delivery game                  ####
##########################################################
##########################################################

from ply.lex import lex
from ply.yacc import yacc

# --- INVENTARIO ---
# Variable global para almacenar los objetos recogidos
inventario = set()

# Función para verificar si un objeto está en el inventario
def tiene_objeto(objeto):
    return objeto in inventario

# -- Lexer --
tokens = (
    'RECOGER', 'SALIR', 'DE', 'LLEVAR', 'AVANZAR', 'ESQUIVAR', 'GOLPEAR', 'CON',
    'ENTREGAR', 'OBJETO', 'WHITESPACE', 'DIRECCION', 'A', 'HERRAMIENTA'
)

# WHITESPACE HANDLER
# Consumes any kind of whitespaceRE
t_ignore = '[\f\r\v\u0020\t]+'

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
t_A = r'A'


# OBJECT TOKEN
# The action here is to save the value of the object identifier.
def t_OBJETO(t):
    r'[a-z]+'
    t.value = str(t.value)
    return t

# Direcciones válidas
def t_DIRECCION(t):
    r'norte|sur|este|oeste'
    return t

# Herramientas/armas para golpear
def t_HERRAMIENTA(t):
    r'cabeza|pie|puño|espada'  # La espada ahora es una herramienta/arma
    return t


# NEWLINE COUNTER
# Counting newlines, however this is not necessary.
# Since we are testing online one line per command.
# Uncomment it, if full testing program is required.
# def t_ignore_newline(t):
#    r'[\n]+'
#    t.lexer.lineno += t.value.count('\n')






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

## --- PARSER ---

#Reglas del parser
def p_comando_recoger(p):
    '''comando : RECOGER OBJETO'''
    objeto = p[2]
    if objeto == 'espada':
        inventario.add(objeto)
        print(f"Comando RECOGER: Recogiste {objeto}")
    else:
        print(f"Comando RECOGER: No puedes recoger {objeto}")
    
def p_comando_avanzar(p):
    '''comando : AVANZAR DIRECCION'''
    print(f"Comando AVANZAR: Avanzaste hacia el {p[2]}")
    
def p_comando_llevar(p):
    '''comando : LLEVAR OBJETO'''
    objeto = p[2]
    if objeto == 'postre1':
        inventario.add(objeto)
    print(f"Comando LLEVAR: Llevaste un {p[2]}")
    
def p_comando_golpear(p):
    '''comando : GOLPEAR CON HERRAMIENTA'''
    herramienta = p[3]
    if herramienta == 'espada' and not tiene_objeto('espada'):
        print("Error: No tienes una espada.")
    else:
        print(f"Comando GOLPEAR: Golpeaste con {herramienta}")
        
def p_comando_entregar(p):
    '''comando : ENTREGAR OBJETO A OBJETO'''
    print(f"Comando ENTREGAR: Entregaste {p[2]} a {p[4]}")

# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: comando incompleto")

parser = yacc()

# --- LOOP PRINCIPAL ---
while True:
    try:
        comando = input('Enter Command > ')
        if not comando:
            break

        # Pasar el comando al parser (el lexer se usa internamente)
        parser.parse(comando)
    except EOFError:
        break