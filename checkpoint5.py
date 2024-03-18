# crear un bucle en python
var = range(1, 10)
for x in var:
    print(x)

# funcion suma

def suma(a, b, c):
    sum = a + b + c
    print(sum)
suma (1, 2, 3)

# funcion lambda

sum = lambda a, b, c:a + b + c
print (sum(1, 2, 3))

# determinar si un valor coincide o no con un valor de la lista

lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adam"]
nombre = "Enrique"
encontrado = False
for nom in lista_nombre:
    if nom == nombre:
        encontrado = True
        break
if encontrado:
    print(f"{nombre} esta en la lista")
else:
    print(f"{nombre} NO esta en la lista")
