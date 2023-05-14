from datetime import datetime
#Clase Cliente
class Cliente():
    def __init__(self, id, nombre, apellido, fecha_registro, saldo, contacto=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_registro = datetime.strptime(fecha_registro, '%d-%m-%Y')
        self.__saldo = saldo
        self.contacto = contacto



    # Método getter para obtener el saldo
    def obtener_saldo(self):
        return self.__saldo

    # Método setter para actualizar el saldo
    def actualizar_saldo(self, monto):
        self.__saldo += monto

    # Método para agregar saldo
    def agregar_saldo(self):
        monto = float(input("Ingrese nuevo monto: "))
        self.actualizar_saldo(monto)

    # Método para mostrar saldo
    def mostrar_saldo(self):
        print(f"Tu saldo actual es de: {self.obtener_saldo()}")


        
        
#------------------------------------------------------------------------------------------------------------------------------------------------------   


#Clase Pruducto
class Producto():
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, descuento=None):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.impuesto = 1.19
        self.descuento = descuento
        self.valor_final = self.valor_neto * self.impuesto




#------------------------------------------------------------------------------------------------------------------------------------------------------------

class Validacion(Producto, Cliente):
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, valor_final, descuento, id, nombre_cliente, apellido_cliente, fecha_registro, saldo, contacto=None):
        Producto.__init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, valor_final, descuento)
        Cliente.__init__(self, id, nombre_cliente, apellido_cliente, fecha_registro, saldo, contacto)
        
    def validar_saldo(self, cliente, producto):
        if cliente.obtener_saldo() < producto.valor_final:
            print("No cuenta con saldo suficiente")
        elif cliente.obtener_saldo() >= producto.valor_final:
            pass
           
    def validar_stock(self, producto):
        if producto.stock < 1:
            print("Lo sentimos no hay stock suficiente")

#-----------------------------------------------------------------------------------------------------------------------------------------------------
    
#Clase Vendedor   
class Vendedor(Validacion):
    def __init__(self, run, nombre, apellido, seccion, contacto = None):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0
        self.contacto = contacto

    # Metodo para vender, se descuenta 1 del stock del producto, se calcula la comision y se suma al atributo comision del vendedor, 
    # Y descuenta el valor final del producto (valorneto+impuesto) del saldo del producto, llamando al metodo actualizar_saldo(ya que saldo
    # esta encapsulado). 
    def vender(self, producto, cliente):
        self.validar_stock(producto)
        self.validar_saldo(cliente, producto)
        if producto.stock > 0:
            producto.stock -= 1
            comision = producto.valor_neto * 0.005
            self.__comision += comision
            cliente.actualizar_saldo(-producto.valor_final)
            print("Estimado cliente su saldo despues de esta compra es: ")
            cliente.mostrar_saldo()
        else:
            print("Lo sentimos, este producto no se encuentra disponible en este momento")

    def obtener_comision(self):
        return self.__comision
    
    
#-----------------------------------------------------------------------------------------------------------------------------------------------

#Clase Proveedor
class Proveedor():
    def __init__(self, rut, nombre_legal, razon_social, pais, tipo_persona, contacto=None):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona
        self.contacto = contacto



    def enviar_productos(self, producto):
        if producto.stock == 0:
            producto.stock + 50
            print("Se ha actualizado el stock de productos")
        




#------------------------------------------------------------------------------------------------------------------------

#instanciamos 5 clientes
cliente1 = Cliente("c001","Camila", "Fuentes", "25-5-2021", 100)
cliente2 = Cliente("c002", "Ana", "Pereira", "1-2-2019", 0)
cliente3 = Cliente("c003", "Diego", "Perez", "2-6-2015", 0)
cliente4 = Cliente("c004", "Tamara", "Torres", "15-11-2022", 0)
cliente5 = Cliente("c005", "Alondra", "Mendez", "8-10-2019", 0)


#instanciamos 5 proveedores
proveedor1 = Proveedor('12345678-9', 'Proveedor 1 Ltda.', 'Proveedor 1 Ltda.', 'Chile', 'persona jurídica','juan@proveedor1.cl')
proveedor2 = Proveedor('98765432-1', 'Proveedor 2 SpA', 'Proveedor 2 SpA', 'Chile', 'persona jurídica','maria@proveedor2.cl')
proveedor3 = Proveedor('11111111-1', 'Juan Perez', 'Juan Perez', 'Colombia', 'persona natural')
proveedor4 = Proveedor('22222222-2', 'María Gonzalez', 'María Gonzalez', 'Colombia', 'persona natural')
proveedor5 = Proveedor('33333333-3', 'Proveedor 5 Inc.', 'Proveedor 5 Inc.', 'Estados Unidos', 'persona jurídica','john@proveedor5.com')


#Instanciamos vendedor
vendedor1 = Vendedor(135695258, "Pedro", "Moreno", "Electronica")

#(self, sku, nombre, categoria, proveedor, stock, valor_neto, descuento=None):
#Instanciamos producto
producto1 = Producto("P001", "Refigerador", "Linea Blanca", proveedor1, 1, 50)


#----------------------------------------------------------------------------------------------------------------------------------------------



vendedor1.vender(producto1, cliente1)
proveedor1.enviar_productos(producto1)
