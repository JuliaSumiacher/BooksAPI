# INTRODUCCIÓN
En este proyecto, desarrollamos una comunicación API Cliente-
Servidor utilizando un archivo JSON con una “lista de los mejores
100 libros” como base de datos. El objetivo fue crear un servidor
que almacenara y procesara datos de libros y un cliente que
realizara consultas y modificaciones a esos datos. Utilizamos un
entorno físico para el servidor, y un entorno virtual para el
cliente, trabajando en ambos casos sobre sistemas operativos
basados en Linux.

# DESCRIPCIÓN DEL ENTORNO DE TRABAJO DEL SERVIDOR
El servidor fue implementado sobre un entorno físico Ubuntu 22.04
Mate. Configuramos el entorno utilizando Python 3.8 y los módulos
fastapi, requests, y uvicorn. Nos encontramos con problemas
relacionados con la instalación de dependencias, que solucionamos
asegurándonos de tener instaladas las versiones correctas de las
bibliotecas necesarias.

# DESCRIPCIÓN DEL ENTORNO DE TRABAJO DEL CLIENTE
El cliente se desarrolló sobre un entorno virtual Ubuntu 22.04
LTA. Utilizamos Python 3.8 y el módulo requests para interactuar
con el servidor API. Uno de los problemas principales fue buscar
libros por autor, dado que siempre devolvía que el autor no fue
encontrado, incluso proporcionando autores que aparecían en el
catálogo.

# DESCRIPCIÓN DE LA BASE DE DATOS ELEGIDA
El archivo JSON seleccionado contiene información sobre 100 libros
y posee las siguientes propiedades:
• author: Nombre del autor (tipo ‘string’)
• country: País de origen del autor (tipo ‘string’)
• imageLink: Enlace a la imagen de la portada (tipo ‘string’)
• language: Idioma del libro (tipo ‘string’)
• link: Enlace a Wikipedia del libro (tipo ‘string’)
• pages: Número de páginas (tipo ‘integer’)
• title: Título del libro (tipo ‘string’)
• year: Año de publicación (tipo ‘integer’)

# PROCEDIMIENTO
Desarrollamos una API con varias rutas para manipular la base de
datos de libros. A continuación, se describen algunas de las
principales instrucciones para comunicarse con la API:

# • Obtener todos los libros
curl -X GET "http://localhost:8000/libros"
# • Buscar libros por autor
curl -X GET "http://localhost:8000/libros/autor/{autor}"
# • Buscar libros por año
curl -X GET "http://localhost:8000/libros/ano/{ano}"
# • Agregar un nuevo libro
curl -X POST "http://localhost:8000/libros" -H "Content-Type:
application/json" -d '{
"author": "Nuevo Autor",
"country": "Nuevo País",
"imageLink": "images/nueva-imagen.jpg",
"language": "Nuevo Idioma",
"link": "https://example.com/nuevo-libro",
"pages": 123,
"title": "Nuevo Título",
"year": 2021
}'
# • Modificar un libro existente
curl -X PUT "http://localhost:8000/libros/Nuevo%20Título" -H
"Content-Type: application/json" -d '{
"author": "Autor Modificado",
"country": "País Modificado",
"imageLink": "images/imagen-modificada.jpg",
"language": "Idioma Modificado",
"link": "https://example.com/libro-modificado",
"pages": 456,
"title": "Nuevo Título",
"year": 2022
}'
# • Eliminar un libro
curl -X DELETE "http://localhost:8000/libros/Nuevo%20Título"

# INSTRUCCIONES DE USO DEL CLIENTE
Para ejecutar y usar el cliente, primero asegúrese de que el
servidor API esté funcionando. Para levantar el servidor:
1. Instale pip y ‘uvicorn’:
sudo apt update
pip3 install uvicorn
2. Ejecute el servidor (asegúrese de navegar al directorio donde
se encuentra ‘servidor.py’):
uvicorn servidor:app --host 0.0.0.0 --port 8000 --reload
3. Permitir el puerto 8000 en el firewall:
sudo ufw allow 8000
sudo ufw enable

Siga estos pasos para configurar y ejecutar el cliente:
1. Instale Python y el módulo ‘requests’:
sudo apt update
sudo apt install python3-pip
pip3 install requests
2. Guarde el código del cliente en un archivo, por ejemplo,
cliente.py.
3. Ejecute el cliente utilizando Python:
python3 cliente.py

# PARA DESCARGAR EL .JSON
https://github.com/benoitvallon/100-best-books/blob/master/books.json
