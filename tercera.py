import re
import tkinter as tk
from tkinter import scrolledtext

palabras_reservadas = r'\b(programa|int|read|end|print)\b'
cadena = r'\".*?\"'
id = r'\b[a-zA-Z]+(?=\s*\()'
variables = r'\b(int|float|boolean|string)\s+([a-zA-Z_, ]+)\b'
punto_coma = r';'
parentesis_apertura = r'\('
parentesis_cierre = r'\)'
parentesis_dobles_apertura = r'\(\('
parentesis_dobles_cierre = r'\)\)'
llave_apertura = r'\{'
llave_cierre = r'\}'

# Agregamos los nuevos patrones
simbolos = {
    '=': r'=',
    '+': r'\+',
    '-': r'-',
    '*': r'\*',
    '/': r'\/',
    '(': r'\(',
    ')': r'\)',
    '{': r'\{',
    '}': r'\}',
    ':': r':',
    ';': r';',
}


def analizar():
    # Obtiene el texto del widget txt_input
    texto = txt_input.get("1.0", "end-1c")
    txt_output.delete("1.0", tk.END)  # Limpia el cuadro de salida

    reservadas = re.findall(palabras_reservadas, texto)
    cadenas = re.findall(cadena, texto)
    ids = re.findall(id, texto)
    vars = re.findall(variables, texto)
    punto_coma_encontrado = re.findall(punto_coma, texto)
    parentesis_apertura_encontrados = re.findall(parentesis_apertura, texto)
    parentesis_cierre_encontrados = re.findall(parentesis_cierre, texto)
    parentesis_dobles_apertura_encontrados = re.findall(
        parentesis_dobles_apertura, texto)
    parentesis_dobles_cierre_encontrados = re.findall(
        parentesis_dobles_cierre, texto)
    llave_apertura_encontradas = re.findall(llave_apertura, texto)
    llave_cierre_encontradas = re.findall(llave_cierre, texto)

    ids = [i for i in ids if i not in reservadas]

    reservadas = list(set(reservadas))

    vars = [i[1] for i in vars]

    simbolos_encontrados = set()
    for simbolo, patron in simbolos.items():
        encontrado = re.findall(patron, texto)
        if encontrado:
            simbolos_encontrados.add(simbolo)

    output = f"""Palabras reservadas encontradas: {reservadas}
Cadenas encontradas: {cadenas}
IDs encontradas: {ids, vars}
Símbolos encontrados: {', '.join(simbolos_encontrados)}

Número de ';' encontrados: {len(punto_coma_encontrado)}
Paréntesis de apertura encontrados: {len(parentesis_apertura_encontrados)}
Paréntesis de cierre encontrados: {len(parentesis_cierre_encontrados)}
Llaves de apertura encontradas: {len(llave_apertura_encontradas)}
Llaves de cierre encontradas: {len(llave_cierre_encontradas)}"""

    if parentesis_dobles_apertura_encontrados or parentesis_dobles_cierre_encontrados:
        output += "\nLa sintaxis de los paréntesis dobles no es reconocida."

    txt_output.insert(tk.END, output)


root = tk.Tk()
root.geometry('700x500')  # Tamaño de la ventana

txt_input = scrolledtext.ScrolledText(root, width=60, height=10)
txt_input.pack()

btn = tk.Button(root, text="Analizar texto", command=analizar)
btn.pack()

txt_output = scrolledtext.ScrolledText(root, width=80, height=10)
txt_output.pack()

root.mainloop()
