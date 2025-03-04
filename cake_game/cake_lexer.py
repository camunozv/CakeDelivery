from ply.lex import lex

# This file is just for saving the lexer when we are done.
# Copy it pleas from main.py

# --- TOKENS ---
tokens = (
    "RECOGER",
    "SALIR",
    "DE",
    "LLEVAR",
    "AVANZAR",
    "ESQUIVAR",
    "GOLPEAR",
    "CON",
    "ENTREGAR",
    "OBJETO",
    "DIRECCION",
    "A",
    "HERRAMIENTA",
)

# WHITESPACE HANDLER
# Consumes any kind of whitespaceRE
t_ignore = "[\f\r\v\u0020\t]+"


# Reglas del lexer
t_ESQUIVAR = r"ESQUIVAR"
t_ENTREGAR = r"ENTREGAR"
t_RECOGER = r"RECOGER"
t_GOLPEAR = r"GOLPEAR"
t_AVANZAR = r"AVANZAR"
t_LLEVAR = r"LLEVAR"
t_SALIR = r"SALIR"
t_CON = r"CON"
t_DE = r"DE"
t_A = r"A"


def t_DIRECCION(t):
    r"norte|sur|este|oeste"
    return t


def t_OBJETO(t):
    r"[a-z]+"
    return t


def t_error(t):
    print(f"Carácter ilegal: {t.value[0]!r}")
    t.lexer.skip(1)


# Construir el lexer
lexer = lex()


# Prueba de tokenización (opcional, para verificar)
def tokenizar(entrada):
    lexer.input(entrada)
    tokens = []
    for token in lexer:
        tokens.append(token)
    return tokens
