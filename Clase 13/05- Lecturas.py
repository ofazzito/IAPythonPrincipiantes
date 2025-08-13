# Modos de apertura de archivos
# 'r' - lectura (por defecto)     

# abrir un archivo para leerlo completo (read)
# with open('mi_archivo.txt', 'r') as f:
#     contenido = f.read()        # Lee todo
#     print(contenido)           # Imprime el contenido completo
    
# abrir un archivo para leerlo línea por línea (readlines)
# with open('mi_archivo.txt', 'r', encoding='utf-8') as f:
#     lineas = f.readlines()  # Devuelve una lista de líneas

#     for linea in lineas:
#         # Procesar cada línea
#         # quiero imprimir la linea que empiece con una letra "E"
#         if  linea.startswith("E"):
#             print(linea.strip()) # strip() elimina espacios en blanco y saltos de línea

# abrir un archivo para leer una línea a la vez (readline)
with open('mi_archivo.txt', 'r', encoding='utf-8') as f:
    contador = 0
    while True:
        linea = f.readline()
        contador += 1
        if not linea:
            break
        print(f"Linea {contador}: {linea.strip()}")  # Imprime cada línea con su número
