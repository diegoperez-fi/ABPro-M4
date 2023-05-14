from datetime import datetime

#Clase Cliente
class Cliente():
    def __init__(self, id, nombre, apellido, fecha_registro, saldo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_registro = datetime.strptime(fecha_registro, '%d-%m-%Y')
        self.__saldo = saldo



    # Método getter para obtener el saldo
    def obtener_saldo(self):
        return self.__saldo

    # Método setter para actualizar el saldo
    def actualizar_saldo(self, monto):
        self.__saldo += monto

    # Método para agregar saldo
    def agregar_saldo(self):
        monto = int(input("Ingrese nuevo monto: "))
        self.actualizar_saldo(monto)

    # Método para mostrar saldo
    def mostrar_saldo(self):
        print(f"Tu saldo actual es de: {self.obtener_saldo()}")

   


#Clase Pruducto
class Producto():
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = 1.19


#Clase Vendedor   
class Vendedor():
    def __init__(self, run, nombre, apellido, seccion):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0


#instanciamos 5 clientes
cliente1 = Cliente("c001","Camila", "Fuentes", "25-5-2021", 2000)
cliente2 = Cliente("c002", "Ana", "Pereira", "1-2-2019", 0)
cliente3 = Cliente("c003", "Diego", "Perez", "2-6-2015", 0)
cliente4 = Cliente("c004", "Tamara", "Torres", "15-11-2022", 0)
cliente5 = Cliente("c005", "Alondra", "Mendez", "8-10-2019", 0)


#Llamamos a los metodos agregar saldo y luego mostrar saldo de la clase cliente
cliente1.agregar_saldo()
cliente1.mostrar_saldo()



#instanciamos 5 productos
producto1 = Producto("P001", "Refigerador", "Linea Blanca", "Mademsa", 250, 400000)
producto2 = Producto("P002", "Televisor", "Electrodomesticos", "LG", 300, 250000)
producto3 = Producto("P003", "Celular", "Telefonia", "Motorola", 30, 100000)
producto4 = Producto("P004", "Batidora", "Linea Blanca", "Thomas", 50, 28000)
producto5 = Producto("P005", "PS5", "Entretenimiento", "Sony", 10, 700000)


#instanciamos 5 vendedores
vendedor1 = Vendedor(135695258, "Pedro", "Moreno", "Electronica")
vendedor2 = Vendedor(154243836, "Michel", "Lara", "Linea Blanca")
vendedor3 = Vendedor(136526960, "Andrea", "Perez", "Linea Blanca")
vendedor4 = Vendedor(197741779, "Cristobal", "Meza", "Telefonia")
vendedor5 = Vendedor(209095541, "Camila", "Chapa", "Entretenimiento")

