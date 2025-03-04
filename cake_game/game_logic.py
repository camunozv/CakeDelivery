# --- INVENTARIO ---
inventario = set()

def tiene_objeto(objeto):
    return objeto in inventario

# --- ESTADOS DEL JUEGO ---
ubicaciones = {
    'castillo': {
        'descripcion': 'Despiertas, tienes una entrega pendiente, ponte tu armadura y lleva tu espada. En tu habitación están los siguientes objetos: Yelmo, pechera, botas y espada. ¿Qué deseas hacer?',
        'conexiones': ['panaderia']
    },
    'sala': {
        'descripcion': 'Estás en la sala. Hay un sofá y una puerta que lleva al jardín.',
        'conexiones': []
    },
    'jardín': {
        'descripcion': 'Estás en el jardín. Hay flores y un camino que lleva a la calle.',
        'conexiones': []
    }
}

ubicacion_actual = 'castillo'  # Ubicación inicial del jugador

# --- FUNCIONES DEL JUEGO ---
def mover_jugador(direccion):
    global ubicacion_actual
    ubicacion = ubicaciones[ubicacion_actual]

    if direccion in ubicacion['conexiones']:
        ubicacion_actual = direccion
        print(f"Comando AVANZAR: Te moviste al {direccion}.")
        print(ubicaciones[ubicacion_actual]['descripcion'])
    else:
        print(f"Error: No puedes avanzar al {direccion} desde aquí.")

def mostrar_ubicacion_actual():
    print(ubicaciones[ubicacion_actual]['descripcion'])