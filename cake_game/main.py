from cake_parser import parser
from game_logic import mostrar_ubicacion_actual


# --- LOOP PRINCIPAL ---
while True:
    try:
        mostrar_ubicacion_actual()# Mostrar la ubicación actual después de cada comando.
        comando = input('Enter Command > ')
        if not comando:
            break

        # Pasar el comando al parser (el lexer se usa internamente)
        parser.parse(comando)
    except EOFError:
        break