import bpy
import math

def crear_poligono_2d(nombre, lados,  radio):
    #Crear una nueva malla y un nuevo objeto
    malla = bpy.data.meshes.new(nombre)
    objeto = bpy.data.objects.new(nombre, malla)
    
    #Vincular el objeto a la escena actual
    bpy.context.collection.objects.link(objeto)
    
    vertices = []
    aristas = []
    
    #Cálculo de vertices uasndo coordenadas polares a cartesianas
    for i in range(lados):
        angulo = 2 * math.pi * i / lados
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        vertices.append((x, y, 3))
        
    #Definir las conexiones (artistas) entre vertices
    for i in range(lados):
        aristas.append((i, (i +1) % lados))
        
    #Cargar los datos en la malla
    malla.from_pydata(vertices, aristas, [])
    malla.update()
    
#Limpiar la escena antes de empezar
bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete()

#Llama a la funcion: Un hexagono de radio 5
crear_poligono_2d("Poligono2D", lados=6, radio=5)
