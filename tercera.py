import re

palabras_reservadas = r'\b(programa|int|read|end|print)\b'
cadena = r'\".*?\"'
id = r'\b[a-zA-Z]+(?=\s*\()'
variables = r'\b(int|float|boolean|string)\s+([a-zA-Z_, ]+)\b'
punto_coma = r';'
parentesis_apertura = r'\('
parentesis_cierre = r'\)'
parentesis_dobles_apertura = r'\(\('
parentesis_dobles_cierre = r'\)\)'

texto = """
programa suma(){
int a,b,c;
read a;
read b;
c=a+b;
print("La suma es");
end
}
"""

reservadas = re.findall(palabras_reservadas, texto)
cadenas = re.findall(cadena, texto)
ids = re.findall(id, texto)
vars = re.findall(variables, texto)
punto_coma_encontrado = re.findall(punto_coma, texto)
parentesis_apertura_encontrados = re.findall(parentesis_apertura, texto)
parentesis_cierre_encontrados = re.findall(parentesis_cierre, texto)
parentesis_dobles_apertura_encontrados = re.findall(parentesis_dobles_apertura, texto)
parentesis_dobles_cierre_encontrados = re.findall(parentesis_dobles_cierre, texto)

if parentesis_dobles_apertura_encontrados or parentesis_dobles_cierre_encontrados:
    print("La sintaxis de los paréntesis dobles no es reconocida.")

ids = [i for i in ids if i not in reservadas]

reservadas = list(set(reservadas))

vars = [i[1] for i in vars]

print("Palabras reservadas encontradas: ", reservadas)
print("Cadenas encontradas: ", cadenas)
print("IDs encontradas: ", ids)
print("Variables encontradas: ", vars)
print("Número de ';' encontrados: ", len(punto_coma_encontrado))
print("Paréntesis de apertura encontrados: ", len(parentesis_apertura_encontrados))
print("Paréntesis de cierre encontrados: ", len(parentesis_cierre_encontrados))
