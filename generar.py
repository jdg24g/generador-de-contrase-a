import random
import sqlite3
import string


def generar_contrasena_unica():
    letras = string.ascii_letters
    numeros = string.digits
    caracteres_validos = letras + numeros

    letra = random.choice(letras)
    numero = random.choice(numeros)
    restantes = [random.choice(caracteres_validos) for _ in range(6)]
    todos = list(letra + numero + "".join(restantes))
    random.shuffle(todos)
    return "".join(todos)


def guardar_contrasena():
    con = sqlite3.connect("base.db")
    cur = con.cursor()

    
    cur.execute("""CREATE TABLE IF NOT EXISTS contraseñas (contraseña TEXT UNIQUE)""")
    con.commit()

    
    while True:
        nueva = generar_contrasena_unica()
        cur.execute("SELECT 1 FROM contraseñas WHERE contraseña = ?", (nueva,))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO contraseñas (contraseña) VALUES (?)", (nueva,))
            con.commit()
            con.close()
            return nueva


def lista_de_contraseñas():
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM contraseñas")
    lista = cur.fetchall()
    con.close()
    return lista