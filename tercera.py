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
simbolo_igual = r'='
simbolo_mas = r'\+'
simbolo_menos = r'-'
simbolo_multiplicacion = r'\*'
simbolo_division = r'\/'

def analizar():
    texto = txt_input.get("1.0", "end-1c")  # Obtiene el texto del widget txt_input

    reservadas = re.findall(palabras_reservadas, texto)
    cadenas = re.findall(cadena, texto)
    ids = re.findall(id, texto)
    vars = re.findall(variables, texto)
    punto_coma_encontrado = re.findall(punto_coma, texto)
    parentesis_apertura_encontrados = re.findall(parentesis_apertura, texto)
    parentesis_cierre_encontrados = re.findall(parentesis_cierre, texto)
    parentesis_dobles_apertura_encontrados = re.findall(parentesis_dobles_apertura, texto)
    parentesis_dobles_cierre_encontrados = re.findall(parentesis_dobles_cierre, texto)
    llave_apertura_encontradas = re.findall(llave_apertura, texto)
    llave_cierre_encontradas = re.findall(llave_cierre, texto)

    # Buscamos los nuevos simbolos
    simbolo_igual_encontrado = re.findall(simbolo_igual, texto)
    simbolo_mas_encontrado = re.findall(simbolo_mas, texto)
    simbolo_menos_encontrado = re.findall(simbolo_menos, texto)
    simbolo_multiplicacion_encontrado = re.findall(simbolo_multiplicacion, texto)
    simbolo_division_encontrado = re.findall(simbolo_division, texto)

    ids = [i for i in ids if i not in reservadas]

    reservadas = list(set(reservadas))

    vars = [i[1] for i in vars]

    output = f"""Palabras reservadas encontradas: {reservadas}
Cadenas encontradas: {cadenas}
IDs encontradas: {ids}
Variables encontradas: {vars}
Número de ';' encontrados: {len(punto_coma_encontrado)}
Paréntesis de apertura encontrados: {len(parentesis_apertura_encontrados)}
Paréntesis de cierre encontrados: {len(parentesis_cierre_encontrados)}
Llaves de apertura encontradas: {len(llave_apertura_encontradas)}
Llaves de cierre encontradas: {len(llave_cierre_encontradas)}
Símbolo '=' encontrados: {len(simbolo_igual_encontrado)}
Símbolo '+' encontrados: {len(simbolo_mas_encontrado)}
Símbolo '-' encontrados: {len(simbolo_menos_encontrado)}
Símbolo '*' encontrados: {len(simbolo_multiplicacion_encontrado)}
Símbolo '/' encontrados: {len(simbolo_division_encontrado)}"""

    if parentesis_dobles_apertura_encontrados or parentesis_dobles_cierre_encontrados:
        output += "\nLa sintaxis de los paréntesis dobles no es reconocida."

    txt_output.insert(tk.END, output)  # Imprime el resultado en el widget txt_output

root = tk.Tk()
root.geometry('700x500')  # Tamaño de la ventana

txt_input = scrolledtext.ScrolledText(root, width=60, height=10)
txt_input.pack()

btn = tk.Button(root, text="Analizar texto", command=analizar)
btn.pack()

txt_output = scrolledtext.ScrolledText(root, width=80, height=10)
txt_output.pack()

root.mainloop()

