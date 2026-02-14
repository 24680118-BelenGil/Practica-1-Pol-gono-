import bpy
import math

#Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

#Parámetros de la figura
radio = 3
angulo_actual = 0
paso_angular = 60 #Cada 60 grados para obtener 6 circulos alrededor

#1.Circulo Central
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0, 0, 0), vertices=64)

#...INICIO DEL PATRÓN REPETITIVO
while angulo_actual <360:

    angulo_actual += paso_angular
    
    x3 = radio * math.cos(math.radians(angulo_actual))
    y3 = radio * math.sin(math.radians(angulo_actual))
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x3, y3, 0), vertices=64)
