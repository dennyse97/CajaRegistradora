#class compras
lista_articulos =list()

def compras():
    print("Agrega tus productos")
    productos=input("Ingrese el producto:")
    precio =float(input("Ingrese el precio: "))
    lista_articulos.append(productos.capitalize())
    print ()
    print("Producto Agregado")
    print()

def total_Compras():
    sumadecostos = 0
    sumadecostos = sumadecostos+precio
     
def tickets():
    print("Lista de Productos Comprados")
    for productos in lista_articulos:
        print (productos)
        print(sumadecostos)

while True:
    print()
    try:
        print ("Opciones")
        print()
        print(" 1. Agregar Productos ")
        print(" 2. Generar ticket ")
        print("3. Apagar")

        opcion =int(input("Que desea hacer: "))
    except ValueError:
        print("Opcion Invalida")
    else:
        if opcion == 1:
            compras()
        elif opcion ==2:
            tickets()
        else:
            break
print("Gracias por visitarnos")
