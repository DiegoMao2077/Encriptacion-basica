from sys import stdin  # Módulo para leer entradas de texto plano de un archivo de extensión ".txt"
import hashlib         # Módulo de Python perteneciente a la librería estándar de Python implementado para cifrar datos                 

password=stdin.readline().strip()        # Entrada de texto
encrypto=str.encode(password)            # Se convierte el string en un byte string
h = hashlib.new("sha512")                # Se crea el objeto de clase hash
h.update(encrypto)                       # Se agregan las lineas del archivo al objeto hash
cad=str(h.hexdigest())                   # Convierte el hash en String
cad=cad[0:20]                            # Coge el primer caracter hasta la posición j-1 (19)
print(cad)                               # Se imprime el hash(String) en bytes (la entrada de texto queda encriptado)

