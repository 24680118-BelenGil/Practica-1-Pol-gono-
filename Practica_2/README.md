# Preactica 2. Flor de vida 🏵️
## Planteamiento
Contruye una Flor de vida con un circulo base de radio 3 y centro en las coordenadas (0,0,0) y *n* canctidad de circulo perifericos, estos deben crearse usan el ciclo "while", que deben estar ubicados exactamente sobre el perímetro del circulo base.

## Desarrollo
Abrimos el area de **Scripting**, creamos un nuevo Text y lo guardamos.

**1.Librerias**

Importamos las siguientes librerias:
```python 
import bpy
import math
```
* **import bpy:** Es la libreria mas importante, con ella Blender entiende el codigo en python.
* **import math:** La necesitaremos para usar las funciones trigonometricas *(seno/coseno)* y convertir las coordenada polares a coordenadas cartianas, así obtendremos una flor en 2D.
  
**2.Preparación de escena**

Antes de crear la flor, necesitamos preparar el escenario seleccionando y elimanado todo objeto que este presente en el, para ello creamos los siguientes métodos:
```python 
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
```
* El primer método selecciona todo objento que se encuentre en el plano y con el siguiente elimina lo seleccionado.
  
**3.Parámetros/Variables**

Una vez preparada la escena, definimos las variable a utilizar.
```python 
radio = 3
angulo_actual = 0
paso_angular = 60 
```
* **radio:** Define la medida del radio de la circunferencia.
* **angulo_actual:** Se inicializa en 0 y define donde inicia y termina un circulo, las cordenadas *X,Y* donde se va ha dibujar, además, de limitar el angulo donde se dibujaran los circulos.
* **paso_angular:** Defiene cada cuantos angulos se de dibujar un circulo, siendo sl limite el *angulo_actual* 

**4.Circulo base**

Con las variables definidas creamos el circulo base, dfiniendo en el interior del método sus caracteristicas, la medida de su radio, su localización en el plano cartesiano y las vertices que nos permitiran visualizar el circulo en el plano.
```python 
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0, 0, 0), vertices=64)
```

**5.Ciclo "While"**

Finalmente, uasmos el ciclo "While" para crear los circulos perifericos e iniciar el patron repetitivo que seguira siempre y cuando el **angulo_actual** se menor a **360°**, una vez cumplida la condicion el ciclo se dentendra.
```python 
while angulo_actual <360:

    angulo_actual += paso_angular
    
    x3 = radio * math.cos(math.radians(angulo_actual))
    y3 = radio * math.sin(math.radians(angulo_actual))
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x3, y3, 0), vertices=64)
```
* **angulo_actual += paso_angular:** Suma por cada ciclo el valos de *paso_angular* a *angulo_acual* para compararlo con 360.
* **X/Y:** Convierte los angulos a radianes, de esta forma la computadora podra enterder los angulos, y dara la coordenadas *X/Y* exactas del circulo, para finalmemte  multiplcar por *radio* y obtener el centro de los circulos en el perimetro del circulo base.
* **bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x3, y3, 0), vertices=64):** Es el encargado de crear el circulo segun los parametros definidos. 

## Resultado
¡¡LISTO!! Ahora puedes crear tu flor de vida 🏵️, cambia las variables para visulizar diferente resultdos.😊

[Da click aquí para ver el código](./Flor_de_vida.py) 

<img width="1048" height="641" alt="Captura de pantalla 2026-02-14 112707" src="https://github.com/user-attachments/assets/3ee1223c-61e0-4242-bd51-8c9e4e74042a" />

En esta imagen el valor de **paso_ angular** es de 60.

<img width="1048" height="648" alt="Captura de pantalla 2026-02-14 112745" src="https://github.com/user-attachments/assets/3d51beb9-301b-485d-aea5-6a2334dc4de1" />

Aquí es de 10.

