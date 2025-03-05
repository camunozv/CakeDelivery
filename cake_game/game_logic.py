# --- INVENTARIO ---
inventario = set()

n_bosque = 2; cont_bosque = 0
n_salida = 2; cont_salida = 0


def tiene_objeto(objeto):
    return objeto in inventario


# --- ESTADOS DEL JUEGO ---
ubicaciones = {
    "castillo": {
        "descripcion": "Despiertas, tienes una entrega pendiente, ponte tu armadura y lleva tu espada. En tu habitación están los siguientes objetos: yelmo, pechera, botas y espada. ¿Qué deseas hacer?",
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
        "descripcion": "Llegaste a la panadería del pueblo y recibes tu encomienda. Debes llevarle un postre entre: galletas, torta de fresa, o helado a la princesa Maria José. ¿Qué deseas hacer?",
        "conexiones": {
            "oeste": "bosque",  # Desde la panadería, al sur está el bosque
        },
        "objetos": {
            "galletas",
            "torta de arándano",
            "helado"
        }, # Objetos disponibles en esta ubicación
    },
    "bosque":{
        "descripcion": "Estas ahora en el bosque tenebroso. Puedes avanzar en la dirección al castillo para completar tu misión ¿Hacia donde deseas avanzar?",
        "conexiones": {
            "norte": "",
            "sur": "",
            "este": "",
            "oeste": ""
        },
        "objetos": set(),
    },
    "ogro": {
        "descripcion": 'En mitad del bosque, te encuentras un ogro horripilante! "No te dejaré pasar!" ',
        "conexiones": {
            "este": "salida"
        },
        "objetos": set(),
    },
    "salida": {
        "descripcion": "¡Has salido vivo del bosque! Felicidades, eres muy valiente. El castillo de la princesa está cerca, sigue avanzando.",
        "conexiones": {},
        "objetos": set(),
    },
    "princesa": {
        "descripcion": "",
        "conexiones": {},
        "objetos": set(),
    }

}

ubicacion_actual = "castillo"  # Ubicación inicial del jugador
postres = {"galletas", "torta de fresa", "helado"}


# --- FUNCIONES DEL JUEGO ---
def mover_jugador(direccion):
    global ubicacion_actual, cont_bosque, cont_salida
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
            actualizar_descripcion_princesa()
        return 

    if direccion in ubicacion["conexiones"]:
        nueva_ubicacion = ubicacion["conexiones"][direccion]
        ubicacion_actual = nueva_ubicacion
        print(f"Comando AVANZAR: Te moviste al {direccion}.")
    else:
        if ubicacion_actual == "ogro":
             print(f"El ogro te tapa el camino!")
        else: 
            print(f"No puedes avanzar al {direccion} desde aquí.")

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
        ubicacion["descripcion"] = f"¡Has llegado al castillo de la princesa! ¿Deseas entregar el {postre_en_inventario}?"
    else:
        print("Llegaste a tiempo! Pero dejaste el postre en la panadería. La princesa se enoja contigo y te quita tu rol de caballero panadero!")
        exit()  # Salir del juego


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

def golpear_ogro(herramienta):
    global ubicacion_actual

    if ubicacion_actual != "ogro":
        print("No hay un ogro aquí.")
        return

    if herramienta == "puño":
        print("Intentaste golpear al ogro con tu puño, pero no fue suficiente. ¡El ogro te ha derrotado!")
        print("¡Has fallado en tu misión!")
        exit()  # Terminar el juego
    elif herramienta == "patada":
        if tiene_objeto("botas"):
            print("Golpeaste al ogro con una patada. ¡El ogro está aturdido! Puedes avanzar.")
            ubicacion_actual = "salida"  # Mover al jugador a la salida
        else:
            print("Intentaste dar una patada al ogro, pero no tienes botas puestas. ¡El ogro te ha derrotado!")
            print("¡Has fallado en tu misión!")
            exit()  # Terminar el juego
    elif herramienta == "espada":
        if tiene_objeto("espada"):
            print("Golpeaste al ogro con la espada. ¡El ogro está aturdido! Puedes avanzar.")
            ubicacion_actual = "salida"  # Mover al jugador a la salida
        else:
            print("Intentaste golpear al ogro con la espada, pero no la dejaste en casa! ¡El ogro te ha derrotado!")
            print("¡Has fallado en tu misión!")
            exit()  # Terminar el juego
    else:
        print(f"Intentaste golpear al ogro con {herramienta}, pero no es una herramienta válida. ¡El ogro te ha derrotado!")
        print("¡Has fallado en tu misión!")
        exit()  # Terminar el juego

def entregar_objeto(objeto, persona):
    global ubicacion_actual

    if tiene_objeto(objeto):  # Verifica que efectivamente tienes el objeto
        if ubicacion_actual == "princesa":  # Verifica que estás en la habitación correcta
            if persona == "princesa":
                inventario.remove(objeto)  # Elimina el objeto del inventario
                print(f"Comando ENTREGAR: Entregaste {objeto} a {persona}.")
                print("¡Felicidades! Has completado tu misión. La princesa está feliz y te nombra el mejor caballero panadero del reino.")
                exit()  # Terminar el juego con un mensaje celebratorio
            else:
                print(f"Error: No está {persona} aquí.")
        else:
            print(f"Debes estar en la habitación de la princesa para entregarle el postre. Estas en {ubicacion_actual}")
    else:
        print("No tienes ese objeto en tu inventario.")
        

def mostrar_ayuda():
    ubicacion = ubicaciones[ubicacion_actual]
    mensaje = "Acciones disponibles:\n"

    # Mostrar objetos disponibles para recoger
    if ubicacion["objetos"]:
        mensaje += f"- Puedes RECOGER los siguientes objetos: {', '.join(ubicacion['objetos'])}.\n"

    # Mostrar direcciones disponibles para moverse
    if ubicacion["conexiones"]:
        mensaje += f"- Puedes AVANZAR en las siguientes direcciones: {', '.join(ubicacion['conexiones'].keys())}.\n"

    # Mostrar comandos generales
    mensaje += "- Comandos generales: RECOGER [objeto], AVANZAR [dirección], ENTREGAR [objeto] A [persona], AYUDA, SALIR.\n"

    # Mensaje especial para la panadería
    if ubicacion_actual == "panaderia":
        mensaje += "- Recuerda que debes llevar un postre a la princesa.\n"

    # Mensaje especial para el bosque
    if ubicacion_actual == "bosque":
        mensaje += "- Debes avanzar varias veces para salir del bosque.\n"

    # Mensaje especial para el ogro
    if ubicacion_actual == "ogro":
        mensaje += "- Puedes GOLPEAR CON: puño, patada (necesitas botas) o espada (necesitas espada).\n"

    # Mensaje especial para la princesa
    if ubicacion_actual == "princesa":
        mensaje += "- Puedes ENTREGAR el (postre) A la (princesa).\n"

    print(mensaje)