#Mónica Isabel López Flores y Deycy Mercedez López Peñate
import re
import tkinter as tk

palabras_reservadas = ["for", "do"]

def analizar(entrada):
    identificador = {}
    for token in palabras_reservadas:
        matches = re.findall(r"\b{}\b".format(token), entrada)
        for match in matches:
            identificador[match] = f"<Reservada {token}> Simbolo {token}"
            entrada = entrada.replace(match, "", 1)

    palabras = re.findall(r"\b\w+\b", entrada)
    for palabra in palabras:
        if palabra not in identificador:
            identificador[palabra] = f"<No definido> {palabra}"

    return identificador

def analizar_codigo():
    codigo = entrada_texto.get("1.0", tk.END)
    entrada = codigo.split("\n")
    token_totales = []
    for i, linea in enumerate(entrada):
        tokes_linea = analizar(linea)
        for token in tokes_linea.values():
            token_totales.append((i+1, token))

    resultado_texto.delete("1.0", tk.END)

    for numero_linea, token in token_totales:
        resultado_texto.insert(tk.END, f"Linea {numero_linea}\n{token}\n")

    numero_reservadas = len([token for numero_linea, token in token_totales if token.startswith("<Reservada")])
    resultado_texto.insert(tk.END, f"\nPalabra reservada: {numero_reservadas}\n")

    palabras_no_definidas = [token for numero_linea, token in token_totales if token.startswith("<No definido>")]
    if palabras_no_definidas:
        resultado_texto.insert(tk.END, "Palabras no definidas:\n")
        for palabra in palabras_no_definidas:
            resultado_texto.insert(tk.END, f"{palabra}\n")

def limpiar_codigo():
    entrada_texto.delete("1.0", tk.END)
    resultado_texto.delete("1.0", tk.END)

ventana = tk.Tk()
ventana.geometry("500x580")
ventana.title("Analizador Léxico")
ventana.config(bg="#12657f")

entrada_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=40)
entrada_texto.place(x=60, y=40)

boton_analizar = tk.Button(ventana, text="Analizar", font=("Arial", 12), bg="#121b29", fg="white", command=analizar_codigo)
boton_analizar.place(x=60, y=240)

boton_limpiar = tk.Button(ventana, text="Limpiar", font=("Arial", 12), bg="#121b29", fg="white", command=limpiar_codigo)
boton_limpiar.place(x=160, y=240)

resultado_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=40)
resultado_texto.place(x=60, y=300)

ventana.mainloop()