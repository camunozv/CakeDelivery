from cake_parser import parser
from game_logic import mostrar_ubicacion_actual


# --- LOOP PRINCIPAL ---
print("Bienvenido a Cake Game! En este juego interpretas a un caballero panadero durante uno de sus días de trabajo. ¿Que pasará hoy?")
while True:
    try:
        mostrar_ubicacion_actual()  # Mostrar la ubicación actual después de cada comando.
        comando = input("\nEnter Command > ")
        if not comando:
            break

        # Pasar el comando al parser (el lexer se usa internamente)
        parser.parse(comando)
    except EOFError:
        break
