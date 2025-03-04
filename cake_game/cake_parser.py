from ply.yacc import yacc
from cake_lexer import lexer, tokens
from game_logic import inventario, tiene_objeto, ubicaciones, ubicacion_actual, mover_jugador

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