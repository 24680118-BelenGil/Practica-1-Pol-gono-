# Practica-1-Pol-gono-2D
## Planteamiento 
Crear un polígono 2D en Blender usando Scripting, donde se pueda editar el numero de lados y el radio de el polígono.
## Desarrollo
Abrimos Blender, habilitamos el área de Scripting y comenzamos a escribir en el área de texto.

1.Importamos las siguinetes librerias.
```python 
import bpy
import math
```
* **import bpy:** Es la mas importante, ya que de esta libreria depende que Blender entienda el código de python.
* **import math:** Libreria de python que permite usar las funciones de seno, coseno y pi.

2.Creamos la siguinete función.
```python 
def crear_poligono_2d(nombre, lados,  radio):
```
Definira el nombre, No.lados y el radio de el polígono.

3.Creación de objetos.
```python 
malla = bpy.data.meshes.new(nombre)
objeto = bpy.data.objects.new(nombre, malla)
bpy.context.collection.objects.link(objeto)
```
* **malla:** Usamos el comando "meshes" para crear la estrcutura básica de la figura.
* **objeto:** Usamos "objects" para crear el contenedor de la malla y ligaos la malla a este.
Finalmente vinculamos el objeto alplano de Blender

4.Listas.
```python 
vertices = []
aristas = []
```
Creamos dos listas, "vertices" guardara las coordenas (x, y, z) para crear una linea y "aristas" se encargara de unir las lineas.

5.Primer ciclo for.
```python 
for i in range(lados):
        angulo = 2 * math.pi * i / lados
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        vertices.append((x, y, 3))
```
Calculamos las vertices pasnado las coordenadas polares a cartesianas, este bucle se repite segun los lados del polígono.
* **angulo:** define donde poner cada punto.
* **x/y :** convierte el ángulo polar a plano cartesiano.
Finalmente se guarda el punto calculado.

6.Segundo ciclo for.
```python 
for i in range(lados):
        aristas.append((i, (i +1) % lados))
```
Definimos las uniones de cada vertice guardado.

7.Carga, Limpieza y Ejecución.
```python 
    malla.from_pydata(vertices, aristas, [])
    malla.update()
    
bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete()

crear_poligono_2d("Poligono2D", lados=6, radio=5)
```
* **malla. :** Se cargan los datos calculados en vertices y aristas en la malla, [] se usa para señalar que en "z" no hay valores, ya que es una figura 2D. Tambien calcula como se vera la figura. 
* **Limpieza:** Se usa "select" para seleccionar todo objeto creado anteriormente y con "delete" los elimina. 
*  **Ejecución:** Llamamos la funcion anteriormente creada y definimos el nombre del poligono, el número de lados y el radio de la figura.
## Resultado
Finalmente, segun lo definido en el código, obtenemos un hexagono de radio 5 y 3 unidades de distancia en el eje Z.
[Da click aquí para ver el código](./poligono_blender.py)

<img width="903" height="550" alt="Captura de pantalla 2026-02-08 162823" src="https://github.com/user-attachments/assets/27497032-cc0f-460b-b1e2-99fca3429dc0" />


