from ply.yacc import yacc
from cake_lexer import lexer, tokens, t_DIRECCION
from game_logic import (
    inventario,
    tiene_objeto,
    ubicaciones,
    ubicacion_actual,
    mover_jugador,
    recoger_objeto,
)


# --- REGLAS DEL PARSER ---
def p_comando_recoger(p):
    """comando : RECOGER OBJETO"""
    objeto = p[2]
    recoger_objeto(objeto)


def p_comando_avanzar(p):
    """comando : AVANZAR DIRECCION"""
    direccion = p[2]
    mover_jugador(direccion)


def p_comando_llevar(p):
    """comando : LLEVAR OBJETO"""
    objeto = p[2]
    recoger_objeto(objeto)
    print(f"Comando LLEVAR: Llevaste un {objeto}")



def p_comando_golpear(p):
    """comando : GOLPEAR CON HERRAMIENTA"""
    herramienta = p[3]
    if herramienta == "espada" and not tiene_objeto("espada"):
        print("Error: No tienes una espada.")
    else:
        print(f"Comando GOLPEAR: Golpeaste con {herramienta}")


def p_comando_entregar(p):
    """comando : ENTREGAR OBJETO A OBJETO"""
    print(f"Comando ENTREGAR: Entregaste {p[2]} a {p[4]}")


def p_comando_salir(p):
    """comando : SALIR"""
    print("Comando SALIR: Saliendo del juego...")
    exit()


# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: comando incompleto")


parser = yacc()
