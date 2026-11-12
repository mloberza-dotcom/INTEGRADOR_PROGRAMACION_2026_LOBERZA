import Menu
import Gestion_stock

def main():
    Gestion_stock.inicializacion()
    
    while True:
        opcion = Menu.mostrar_menu()
        
        if opcion == 1:
            print("CARGAR STOCK")
            Gestion_stock.cargar()
            
        elif opcion == 2:
            print("MOSTRAR TOTAL DEL STOCK")
            Gestion_stock.mostrar()
            
        elif opcion == 3:
            print("CONTAR PRODUCTOS")
            cat = input("De que categoria queres contar los productos (enlatados, frutas, panaderia, congelados)? ").lower()
            if cat in Gestion_stock.stockcant:
                Gestion_stock.contar(Gestion_stock.stockcant[cat])
            else:
                print("Categoria no valida.")
                
        elif opcion == 4:
            print("Saliendo del sistema.")
            break
        else:
            print("Opcion invalida 1.Cargar Stock\n2.Mostrar total del stock\n3.Contar productos 4.Salir")

if __name__ == "__main__":
    main()