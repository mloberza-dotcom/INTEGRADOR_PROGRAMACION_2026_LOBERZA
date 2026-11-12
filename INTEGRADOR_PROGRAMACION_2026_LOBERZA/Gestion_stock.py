stockprod={
    "enlatados": [],
    "frutas": [],
    "panaderia": [],
    "congelados": []}


stockcant={
    "enlatados": [],
    "frutas": [],
    "panaderia": [],
    "congelados": []}


def inicializacion ():
    for categoria in stockprod:
        stockprod[categoria]=[]
    for categoria in stockcant:
        stockcant[categoria]=[]

def cargar ():
    while True:
        categoria=input("De que categoria es tu producto??\n").lower()
        if categoria in stockcant:
            print("categoria aceptada")
            break
        else:
            print("la categoria tiene que ser panaderia, frutas, enlatados o congelados")

    nombre=input("Que producto queres cargar??\n")
    cantidad=int(input("Cuantos queres cargar??\n"))
    stockprod[categoria].append(nombre)
    stockcant[categoria].append(cantidad)

def mostrar():
    while True:
            categoria=input("Que categoria queres ver??\n").lower()
            if categoria in stockcant:
                print("Categoria aceptada")
                break
            else:
                print("la categoria tiene que ser panaderia, frutas, enlatados o congelados")

    print(f"Categoria: {categoria}")
    for i in range (len(stockprod[categoria])):
        print(f"Productos: {stockprod[categoria][i]} Cantidades:{stockcant[categoria][i]}")

def contar(lista):
    cantprod=len(lista)
    cantprods=sum(lista)
    print(f"La cantidad de productos que hay son {cantprod}\n en total son: {cantprods} disponibles en el almacen")
