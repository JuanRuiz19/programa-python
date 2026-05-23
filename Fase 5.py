# Programa: Ingenieria Electronica
# Autor: Juan Carlos Ruiz Vallejo
# Curso: Fundamentos de Programacion


# MÓDULO: Función de clasificación de compromiso

def clasificar_compromiso(duracion, clics):
    """
    Clasifica el nivel de compromiso de una sesión.
    
    Parámetros:
        duracion (int): Duración de la sesión en segundos
        clics    (int): Número de eventos de clics
    
    Retorna:
        str: "Alto", "Medio" o "Bajo"
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"



# DATOS INICIALES: Matriz de sesiones
# Formato: [ID Cliente, Duración (seg), Clics]

sesiones = [
    [1001, 250, 12],   # Duración alta y clics altos  -> Alto
    [1002, 45,  1],    # Duración baja y clics bajos  -> Bajo
    [1003, 120, 6],    # Duración media y clics medios -> Medio
    [1004, 200, 3],    # Duración alta pero clics bajos -> Medio
    [1005, 30,  10],   # Duración baja -> Bajo
    [1006, 190, 9],    # Duración alta y clics altos  -> Alto
    [1007, 90,  2],    # Clics bajos -> Bajo
]



# GENERACIÓN DEL INFORME

print("=" * 45)
print("   INFORME DE NIVEL DE COMPROMISO")
print("=" * 45)
print(f"{'ID Cliente':<15} {'Duración (s)':<15} {'Clics':<10} {'Clasificación'}")
print("-" * 45)

conteo_alto  = 0
conteo_medio = 0
conteo_bajo  = 0

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion   = sesion[1]
    clics      = sesion[2]
    
    clasificacion = clasificar_compromiso(duracion, clics)
    
    print(f"{id_cliente:<15} {duracion:<15} {clics:<10} {clasificacion}")
    
    if clasificacion == "Alto":
        conteo_alto += 1
    elif clasificacion == "Medio":
        conteo_medio += 1
    else:
        conteo_bajo += 1

print("=" * 45)
print("\nRESUMEN GENERAL:")
print(f"  Sesiones de compromiso Alto  : {conteo_alto}")
print(f"  Sesiones de compromiso Medio : {conteo_medio}")
print(f"  Sesiones de compromiso Bajo  : {conteo_bajo}")
print(f"  Total de sesiones analizadas : {len(sesiones)}")
print("=" * 45)
