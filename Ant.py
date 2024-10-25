import numpy as np

num_hormigas = 5
num_ciudades = 5
evaporacion_feromonas = 0.1
alfa = 1  
beta = 2  
iteraciones = 30

distancias = np.array([
    [0, 2, 9, 10, 7],
    [2, 0, 6, 5, 11],
    [9, 6, 0, 8, 3],
    [10, 5, 8, 0, 8],
    [7, 11, 3, 8, 0]
])

feromonas = np.ones((num_ciudades, num_ciudades))*0.1

# Función de visibilidad (1/distancia)
visibilidad = 1 / (distancias + np.diag([np.inf]*num_ciudades))  

def elegir_siguiente_ciudad(feromonas, visibilidad, ciudad_actual, visitadas):
    probabilidades = []
    for i in range(num_ciudades):
        if i not in visitadas:
            # Fórmula de probabilidad: (feromonas^alfa) * (visibilidad^beta)
            prob = (feromonas[ciudad_actual][i] ** alfa) * (visibilidad[ciudad_actual][i] ** beta)
            probabilidades.append((i, prob))
    
    suma_probabilidades = sum([p[1] for p in probabilidades])
    probabilidades_normalizadas = [(p[0], p[1] / suma_probabilidades) for p in probabilidades]
    
    r = np.random.random()
    acumulado = 0
    for ciudad, prob in probabilidades_normalizadas:
        acumulado += prob
        if r <= acumulado:
            return ciudad

def actualizar_feromonas(caminos, longitudes_caminos):
    # Evaporar las feromonas
    global feromonas
    feromonas = (1 - evaporacion_feromonas) * feromonas
    
    for i, camino in enumerate(caminos):
        for j in range(num_ciudades - 1):
            feromonas[camino[j]][camino[j+1]] += 1 / longitudes_caminos[i]

def calcular_longitud_camino(camino):
    longitud = 0
    for i in range(len(camino) - 1):
        longitud += distancias[camino[i]][camino[i + 1]]
    return longitud


mejor_camino = None
mejor_longitud = float('inf')

for iteracion in range(iteraciones):
    caminos = []
    longitudes_caminos = []
    
    for hormiga in range(num_hormigas):
        ciudad_inicial = np.random.randint(num_ciudades)
        camino = [ciudad_inicial]
        
        while len(camino) < num_ciudades:
            ciudad_actual = camino[-1]
            siguiente_ciudad = elegir_siguiente_ciudad(feromonas, visibilidad, ciudad_actual, camino)
            camino.append(siguiente_ciudad)

        camino.append(camino[0])
        caminos.append(camino)
        longitudes_caminos.append(calcular_longitud_camino(camino))
    
    actualizar_feromonas(caminos, longitudes_caminos)
    
    min_longitud = min(longitudes_caminos)
    if min_longitud < mejor_longitud:
        mejor_longitud = min_longitud
        mejor_camino = caminos[longitudes_caminos.index(min_longitud)]
    
    print(f"Iteración {iteracion + 1}: Mejor longitud = {mejor_longitud}")

print(f"Mejor camino encontrado: {mejor_camino}")
print(f"Longitud del mejor camino: {mejor_longitud}")