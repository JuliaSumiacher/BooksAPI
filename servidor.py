from fastapi import FastAPI, HTTPException
import uvicorn
import json

app = FastAPI()

# Cargamos los datos del archivo JSON en una variable global
with open('books.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Ruta para obtener todos los libros
@app.get('/libros')
def obtener_libros():
    return data

# Ruta para buscar libros por autor
@app.get('/libros/autor/{autor}')
def buscar_libros_por_autor(autor: str):
    libros = [libro for libro in data if libro['author'].lower() == autor.lower()]
    if not libros:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return libros

# Ruta para buscar libros por año
@app.get('/libros/ano/{ano}')
def buscar_libros_por_ano(ano: int):
    libros = [libro for libro in data if libro['year'] == ano]
    if not libros:
        raise HTTPException(status_code=404, detail="Año no encontrado")
    return libros

# Ruta para agregar un nuevo libro
@app.post('/libros')
def agregar_libro(libro: dict):
    data.append(libro)
    with open('books.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)
    return {"mensaje": "Libro agregado correctamente"}

# Ruta para modificar un libro existente
@app.put('/libros/{titulo}')
def modificar_libro(titulo: str, libro_actualizado: dict):
    for libro in data:
        if libro['title'].lower() == titulo.lower():
            libro.update(libro_actualizado)
            with open('books.json', 'w', encoding='utf-8') as file:
                json.dump(data, file)
            return {"mensaje": "Libro actualizado correctamente"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")

# Ruta para eliminar un libro
@app.delete('/libros/{titulo}')
def eliminar_libro(titulo: str):
    for libro in data:
        if libro['title'].lower() == titulo.lower():
            data.remove(libro)
            with open('books.json', 'w', encoding='utf-8') as file:
                json.dump(data, file)
            return {"mensaje": "Libro eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")

# Punto de entrada para ejecutar el servidor
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
