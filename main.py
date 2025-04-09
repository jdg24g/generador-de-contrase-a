import customtkinter
import pyperclip

from generar import guardar_contrasena, lista_de_contraseñas

app = customtkinter.CTk()
app.title("🔐 GENERADOR DE CONTRASEÑAS")
app.geometry("400x400")
app.resizable(False, False)


resultado = customtkinter.CTkEntry(app, width=300, justify="center")
resultado.grid(row=0, column=0, padx=20, pady=20)


def button_callback():
    nueva = guardar_contrasena()
    resultado.configure(state="normal")
    resultado.delete(0, "end")
    resultado.insert(0, nueva)
    resultado.configure(state="readonly")


def copiar():
    pyperclip.copy(resultado.get())


def mostrar_contrasenas():
    lista = lista_de_contraseñas()

    ventana = customtkinter.CTkToplevel(app)
    ventana.title("Lista de Contraseñas Guardadas")
    ventana.geometry("400x400")

    text_box = customtkinter.CTkTextbox(ventana, width=350, height=350)
    text_box.pack(padx=20, pady=20)

    if not lista:
        text_box.insert("0.0", "No hay contraseñas guardadas.")
    else:
        for i, contrasena in enumerate(lista, 1):
            text_box.insert("end", f"{i}. {contrasena[0]}\n")

    text_box.configure(state="disabled")


boton_generar = customtkinter.CTkButton(
    app, text="Generar Contraseña", command=button_callback
)
boton_generar.grid(row=1, column=0, pady=10)

boton_copiar = customtkinter.CTkButton(app, text="Copiar", command=copiar)
boton_copiar.grid(row=2, column=0, pady=10)

boton_ver = customtkinter.CTkButton(
    app, text="Ver Contraseñas", command=mostrar_contrasenas
)
boton_ver.grid(row=3, column=0, pady=10)

app.grid_columnconfigure(0, weight=1)
app.mainloop()