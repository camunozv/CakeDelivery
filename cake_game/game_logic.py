# --- INVENTARIO ---
inventario = set()


def tiene_objeto(objeto):
    return objeto in inventario


# --- ESTADOS DEL JUEGO ---
ubicaciones = {
    "castillo": {
        "descripcion": "Despiertas, tienes una entrega pendiente, ponte tu armadura y lleva tu espada. En tu habitación están los siguientes objetos: Yelmo, pechera, botas y espada. ¿Qué deseas hacer?",
        "conexiones": {
            "norte": "panaderia"  # Desde el castillo, al norte está la panadería
        },
        "objetos": {
            "yelmo",
            "pechera",
            "botas",
            "espada",
        },  # Objetos disponibles en esta ubicación
    },
    "panaderia": {
        "descripcion": "Estás en la panadería. Hay un pastel sobre la mesa.",
        "conexiones": {
            "sur": "castillo"  # Desde la panadería, al sur está el castillo
        },
        "objetos": set(),  # No hay objetos en esta ubicación
    },
}

ubicacion_actual = "castillo"  # Ubicación inicial del jugador


# --- FUNCIONES DEL JUEGO ---
def mover_jugador(direccion):
    global ubicacion_actual
    ubicacion = ubicaciones[ubicacion_actual]

    if direccion in ubicacion["conexiones"]:
        nueva_ubicacion = ubicacion["conexiones"][direccion]
        ubicacion_actual = nueva_ubicacion
        print(f"Comando AVANZAR: Te moviste al {direccion}.")
        mostrar_ubicacion_actual()
    else:
        print(f"Error: No puedes avanzar al {direccion} desde aquí.")


def mostrar_ubicacion_actual():
    ubicacion = ubicaciones[ubicacion_actual]
    print(ubicacion["descripcion"])


def actualizar_descripcion_castillo():
    ubicacion = ubicaciones["castillo"]
    objetos_restantes = ubicacion["objetos"]

    if not objetos_restantes:
        # Si no quedan objetos, mostrar la nueva descripción
        ubicacion["descripcion"] = (
            "Ya te alistaste! Dirígete a la panadería antes de que se te haga tarde."
        )
    else:
        # Si quedan objetos, mostrar la lista de objetos restantes
        if "espada" in objetos_restantes:
            descripcion = "Despiertas, tienes una entrega pendiente, ponte tu armadura y lleva tu espada. En tu habitación están los siguientes objetos: "
        else:
            descripcion = "Despiertas, tienes una entrega pendiente, ponte tu armadura. En tu habitación están los siguientes objetos: "

        descripcion += ", ".join(objetos_restantes) + ". ¿Qué deseas hacer?"
        ubicacion["descripcion"] = descripcion


def recoger_objeto(objeto):
    global ubicacion_actual
    ubicacion = ubicaciones[ubicacion_actual]

    if objeto in ubicacion["objetos"]:
        inventario.add(objeto)
        ubicacion["objetos"].remove(objeto)  # Eliminar el objeto de la ubicación
        print(f"Comando RECOGER: Recogiste {objeto}.")

        # Actualizar la descripción de la ubicación
        if ubicacion_actual == "castillo":
            actualizar_descripcion_castillo()
    else:
        print(f"Error: No hay {objeto} en esta ubicación.")
