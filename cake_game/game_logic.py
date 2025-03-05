# --- INVENTARIO ---
inventario = set()

n_bosque = 2; cont_bosque = 0
n_salida = 2; cont_salida = 0


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
        "descripcion": "Llegaste a la panadería del pueblo y recibes tu encomienda. Debes llevarle un postre entre: galletas, torta de arándano, o helado a la princesa Maria José. ¿Qué deseas hacer?",
        "conexiones": {
            "sur": "bosque",  # Desde la panadería, al sur está el bosque
        },
        "objetos": {
            "galletas",
            "torta de arándano",
            "helado"
        }, # Objetos disponibles en esta ubicación
    },
    "bosque":{
        "descripcion": "Estas ahora en el bosque tenebroso. Puedes avanzar en la dirección al castillo parac completar tu misión ¿Hacia donde deseas avanzar?",
        "conexiones": {
            "norte": "",
            "sur": "",
            "este": "",
            "oeste": ""
        },
        "objetos": set(),
    },
    "ogro": {
        "descripcion": "",
        "conexiones": {},
        "objetos": set(),
    },
    "salida": {
        "descripcion": "¡Has salido vivo del bosque! Felicidades, eres muy valiente. El castillo de la princesa está cerca, sigue avanzando.",
        "conexiones": {},
        "objetos": set(),
    },
    "princesa": {
        "descripcion": "Llegaste a la habitación de la princesa, ¿Qué dese",
        "conexiones": {},
        "objetos": set(),
    }

}

ubicacion_actual = "castillo"  # Ubicación inicial del jugador
postres = {"galletas", "torta de arándano", "helado"}

def get_ubicacion_actual():
    return ubicacion_actual

# --- FUNCIONES DEL JUEGO ---
def mover_jugador(direccion):
    global ubicacion_actual, cont_bosque
    ubicacion = ubicaciones[ubicacion_actual]

    if ubicacion_actual == "bosque":
        cont_bosque += 1  # Incrementar el contador cada vez que avanza en el bosque
        print(f"Comando AVANZAR: Sigues avanzando en el bosque... ({cont_bosque}/{n_bosque})")
        ubicacion["descripcion"] = "Sigues en el bosque tenebroso. ¿Hacia donde deseas avanzar?"

        if cont_bosque >= n_bosque:
            ubicacion_actual = "ogro"
            cont_bosque = 0
        return 
    
    if ubicacion_actual == "salida":
        cont_salida += 1  # Incrementar el contador cada vez que avanza en la salida del bosque
        print(f"Comando AVANZAR: Te sigues acercando al castillo de la princesa... ({cont_salida}/{n_salida})")
        ubicacion["descripcion"] = "Sigues en el camino. ¿Hacia donde deseas avanzar?"

        if cont_salida >= n_salida:
            ubicacion_actual = "princesa"
            cont_salida = 0
        return 

    if direccion in ubicacion["conexiones"]:
        nueva_ubicacion = ubicacion["conexiones"][direccion]
        ubicacion_actual = nueva_ubicacion
        print(f"Comando AVANZAR: Te moviste al {direccion}.")
        #mostrar_ubicacion_actual()
        if nueva_ubicacion == "princesa":
            actualizar_descripcion_princesa()
    else:
        print(f"Error: No puedes avanzar al {direccion} desde aquí.")

def mostrar_ubicacion_actual():
    ubicacion = ubicaciones[ubicacion_actual]
    print(ubicacion["descripcion"])


def actualizar_descripcion_panaderia():
    ubicacion = ubicaciones["panaderia"]
    objetos_restantes = ubicacion["objetos"]
    global postres

    # Verifica si el jugador ya tiene un postre en su inventario
    if any(tiene_objeto(postre) for postre in postres):
        ubicacion["descripcion"] = "Ya tienes un postre para la princesa. ¡Llévaselo antes de que se enfríe!"
    else:
        ubicacion["descripcion"] = (
            f"Llegaste a la panadería del pueblo y recibes tu encomienda. Debes llevarle un postre entre: {', '.join(objetos_restantes)} a la princesa Maria José. ¿Qué deseas hacer? \n {inventario}"
        )

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

def actualizar_descripcion_princesa():
    ubicacion = ubicaciones["princesa"]

    global postres
    postre_en_inventario = next((postre for postre in postres if tiene_objeto(postre)), None)

    if postre_en_inventario:
        ubicacion["descripcion"] = f"¡Has al castillo de la princesa llegado! ¿Deseas entregar el {postre_en_inventario}?"
    else:
        ubicacion["descripcion"] = "¡Felicidades! Has completado tu viaje. La princesa está contenta…"


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
        elif ubicacion_actual == "panaderia":
            actualizar_descripcion_panaderia()
    else:
        print(f"Error: No hay {objeto} en esta ubicación.")

def entregar_objeto(objeto, persona):
    global ubicacion_actual

    if tiene_objeto(objeto):  # Verifica que efectivamente tienes el objeto
        if ubicacion_actual == "princesa":  # Verifica que estás en la habitación correcta
            if persona == "princesa":
                inventario.remove(objeto)  # Elimina el objeto del inventario
                print(f"Comando ENTREGAR: Entregaste {objeto} a {persona}.")
                actualizar_descripcion_princesa()
            else:
                print(f"Error: No está {persona} aquí.")
        else:
            print(f"Error: Debes estar en la habitación de la princesa para entregarle el postre. Estas en {ubicacion_actual}")
    else:
        print("Error: No tienes ese objeto en tu inventario.")