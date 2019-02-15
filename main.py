import pulp
 
## Objetivo del modelo ##
# pulp.LpMaximize = Maximizar
# pulp.LpMinimize = Minimizar
model = pulp.LpProblem("Maximizar Ganancia Bruta", pulp.LpMaximize)

## Naturaleza de variables ##
# Naturaleza Integer (Entero), Continuous (Continuos), Binary (Binarios)
# Limite inferior: lowBound (mayores o iguales a N)
# Limite superior: upBound (menores o iguales a N)
X1 = pulp.LpVariable('X1', lowBound=0, cat='Integer') 
X2 = pulp.LpVariable('X2', lowBound=0, cat='Integer') 

# Función objetivo.
model += 60 * X1 + 50 * X2

# Restricciones.
model += 2 * X1 + 4 * X2 <= 48
model += 3 * X1 + 2 * X2 <= 36

# Resolviendo el modelo.
model.solve()
pulp.LpStatus[model.status]

# Imprimiendo resultados.
print("maxz = 60x1 + 50x2")
print("restricción #1 - Tiempo disponible máquina A: 2x1 + 4x2 <= 48 ")
print("restricción #2 - Tiempo disponible máquina B: 3x1 + 2x2 <= 36 ")
print("\n====== RESULTADO ======")
print("Cantidad de unidades del producto 1 (x1) = {}".format(X1.varValue))
print("Cantidad de unidades del producto 2 (x2) = {}".format(X2.varValue))
print("Maxima ganancia bruta (z) = {}".format(pulp.value(model.objective)))