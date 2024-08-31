import requests  # Importamos la biblioteca requests para hacer solicitudes HTTP

# Definimos la URL del servidor.
server_url = 'http://<ip_del_servidor>:8000'  

# Función para obtener todos los libros
def obtener_libros():
    response = requests.get(f'{server_url}/libros')  # Hacemos una solicitud GET al endpoint '/libros'
    print(response.json())  # Imprimimos la respuesta JSON

# Función para buscar libros por autor
def buscar_libros_por_autor(autor):
    response = requests.get(f'{server_url}/libros/autor/{autor}')  # Hacemos una solicitud GET al endpoint '/libros/autor/{autor}'
    print(response.json())  # Imprimimos la respuesta JSON

# Función para buscar libros por año
def buscar_libros_por_ano(ano):
    response = requests.get(f'{server_url}/libros/ano/{ano}')  # Hacemos una solicitud GET al endpoint '/libros/ano/{ano}'
    print(response.json())  # Imprimimos la respuesta JSON

# Función para agregar un nuevo libro
def agregar_libro(libro):
    response = requests.post(f'{server_url}/libros', json=libro)  # Hacemos una solicitud POST al endpoint '/libros' con el nuevo libro en formato JSON
    print(response.json())  # Imprimimos la respuesta JSON

# Función para modificar un libro existente
def modificar_libro(titulo, libro_actualizado):
    response = requests.put(f'{server_url}/libros/{titulo}', json=libro_actualizado)  # Hacemos una solicitud PUT al endpoint '/libros/{titulo}' con los datos actualizados del libro en formato JSON
    print(response.json())  # Imprimimos la respuesta JSON

# Función para eliminar un libro
def eliminar_libro(titulo):
    response = requests.delete(f'{server_url}/libros/{titulo}')  # Hacemos una solicitud DELETE al endpoint '/libros/{titulo}'
    print(response.json())  # Imprimimos la respuesta JSON

# Bloque principal de ejecución
if __name__ == "__main__":
    # Llamamos a las funciones definidas anteriormente para probar el funcionamiento del servidor
    obtener_libros()
    buscar_libros_por_autor("Gabriel Garcia Marquez")
    buscar_libros_por_ano(1985)
    
    # Definimos un nuevo libro para agregar
    nuevo_libro = {
        "author": "Nuevo Autor",
        "country": "Nuevo País",
        "imageLink": "nueva-imagen.jpg",
        "language": "Nuevo Idioma",
        "link": "https://nuevo-enlace.com",
        "pages": 123,
        "title": "Nuevo Título",
        "year": 2021
    }
    agregar_libro(nuevo_libro)  # Agregamos el nuevo libro
    
    # Definimos los datos actualizados del libro
    libro_actualizado = {
        "author": "Autor Actualizado",
        "country": "País Actualizado",
        "imageLink": "imagen-actualizada.jpg",
        "language": "Idioma Actualizado",
        "link": "https://enlace-actualizado.com",
        "pages": 456,
        "title": "Título Actualizado",
        "year": 2022
    }
    modificar_libro("Nuevo Título", libro_actualizado)  # Modificamos el libro existente
    
    eliminar_libro("Título Actualizado")  # Eliminamos el libro actualizado


# Ejemplo de uso de las funciones del cliente
print(obtener_libros())  # Imprimimos todos los libros
print(buscar_libros_por_autor('Gabriel Garcia Marquez'))  # Imprimimos los libros de un autor específico
print(buscar_libros_por_ano(1985))  # Imprimimos los libros de un año específico
nuevo_libro = {
    "author": "Nuevo Autor",
    "country": "Nuevo País",
    "imageLink": "link",
    "language": "Nuevo Idioma",
    "link": "link",
    "pages": 123,
    "title": "Nuevo Título",
    "year": 2024
}
print(agregar_libro(nuevo_libro))  # Agregamos un nuevo libro y mostramos la respuesta
print(modificar_libro("Nuevo Título", {"pages": 456}))  # Modificamos un libro existente y mostramos la respuesta
print(eliminar_libro("Nuevo Título"))  # Eliminamos un libro existente y mostramos la respuesta
