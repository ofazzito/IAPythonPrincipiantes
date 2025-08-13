# Crear un archivo y escribir en él
nombre_archivo = 'mi_archivo.txt'

# Abrir el archivo en modo escritura (w)
archivo = open(nombre_archivo, 'w', encoding='utf-8')

# Escribir contenido en el archivo
archivo.write('Hola, este es un archivo de prueba.\n')
archivo.write('Este es un segundo renglón.\n')  
archivo.write('\tTodo simple y sencillo desde Python.\n')
archivo.write('No soy un niño\n')

# Cerrar el archivo
archivo.close()

# Confirmación de creación del archivo
print(f'Se ha creado el archivo {nombre_archivo} con éxito.')


