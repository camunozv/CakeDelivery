from ply.yacc import yacc
from cake_lexer import lexer, tokens, t_DIRECCION
from game_logic import (
    inventario,
    tiene_objeto,
    ubicaciones,
    ubicacion_actual,
    mover_jugador,
    recoger_objeto,
    entregar_objeto,
    get_ubicacion_actual
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
    global ubicacion_actual
    objeto = p[2]
    persona = p[4]

    if tiene_objeto(objeto):
        if ubicacion_actual == "princesa":  # Verifica que estás en la habitación correcta
            if persona == "princesa":
                entregar_objeto(objeto)  # Pasa el objeto correctamente
                print(f"Comando ENTREGAR: Entregaste {objeto} a {persona}.")
            else:
                print(f"Error: No está {persona} aquí.")
        else:
            print(f"Error: Debes estar en la habitación de la princesa para entregarle el postre. Estas en {ubicacion_actual}")
    else:
        print(f"Error: No tienes {objeto} en tu inventario.")



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
