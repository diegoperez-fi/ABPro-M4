from datetime import datetime

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



#--------------------------------------------------------------

class Producto:
    def __init__(self, sku, nombre, valor_neto):
        self.sku = sku
        self.nombre = nombre
        self.valor_neto = valor_neto
        

#--------------------------------------------------------------


class Bodega(Producto):
    def __init__(self,  sku, nombre, valor_neto, stock_b):
        super().__init__(sku, nombre, valor_neto)
        self.stock_b = stock_b
        self.valor_mayorista = valor_neto - (valor_neto * 0.3)



#---------------------------------------------------------------

class Sucursal(Producto):
    def __init__(self,  sku, nombre, valor_neto, stock_s):
        super().__init__(sku, nombre, valor_neto)
        self.stock_s = stock_s
        

    def ajustar_stock(self):
        if self.stock_s < 50:
            self.stock_s += 300
            for producto in productos_bodega:
                if producto.sku == self.sku:
                    producto.stock_b -= 300
                    print(f"El nuevo Stock en bodega del producto {producto.nombre} es de {producto.stock_b} unidades")
                    print(f"El nuevo Stock en sucursal del producto {producto.nombre} es de {self.stock_s}")
                    break

#--------------------------------------------------------------------
class OrdenCompra:
    def __init__(self, id_ordencompra, producto, despacho):
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.despacho = despacho
        self.valor_despacho = 5000 if despacho else 0

    def calcular_total_final(self):
        valor_neto = self.producto.valor_neto
        impuesto = valor_neto * 0.19
        valor_total = valor_neto + impuesto + self.valor_despacho

        print("Detalle de la orden de compra:")
        print(f"Valor neto: {valor_neto} CLP")
        print(f"Impuesto: {impuesto} CLP")
        print(f"Despacho: {'Sí, costo despacho: 5000' if self.despacho else 'No'}")
        print(f"Valor total: {valor_total} CLP")

        return valor_total

#-------------------------------------------------------------------  
class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, contacto = None):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0
        self.contacto = contacto

   
    def vender(self, orden_compra, cliente):
        producto = orden_compra.producto

        if producto.stock_s > 0:
            valor_total = orden_compra.calcular_total_final()

            if cliente.obtener_saldo() >= int(valor_total):
                producto.stock_s -= 1
                comision = producto.valor_neto * 0.005
                self.__comision += comision
                cliente.actualizar_saldo(-valor_total)

                print("Venta realizada exitosamente.")
                print(f"Nuevo saldo del cliente: {cliente.obtener_saldo()} CLP")
                print(f"Nuevo stock del producto en sucursal: {producto.stock_s} unidades")
            else:
                print("El cliente no tiene saldo suficiente para realizar la compra.")
        else:
            print("El producto no está disponible en stock en la sucursal.")


    def obtener_comision(self):
        return self.__comision
    



#------------------------------------------------------------------------

#Clientes
#instanciamos 5 clientes
cliente1 = Cliente("c001","Camila", "Fuentes", "25-5-2021", 20000)
cliente2 = Cliente("c002", "Ana", "Pereira", "1-2-2019", 15000)


#Productos Bodega
zapatillas = Bodega('A111', 'zapatillas', 5000, 500)
poleras = Bodega('A112', 'polera', 3000, 600)
zapatos = Bodega('A113', 'zapatos', 15000, 600)

productos_bodega = [zapatillas, zapatos, poleras]


#Productos sucursal
zapatillas_sucursal = Sucursal('A111', 'zapatillas', 5000, 60)
poleras_sucursal = Sucursal('A112', 'polera', 3000, 51)
zapatos_sucursal = Sucursal('A113', 'zapatos', 15000, 40)

productos_sucursal = [zapatillas_sucursal, zapatos_sucursal, poleras_sucursal]

#Instanciamos vendedor
vendedor1 = Vendedor(135695258, "Pedro", "Moreno", "Electronica")


#Instancia para verificar el stock de productos en sucursal
for producto in productos_sucursal:
    producto.ajustar_stock()


#Instancia de orden de compra
orden_compra = OrdenCompra(1, zapatillas_sucursal, True)



#Instanciamos la venta desde la clase vendedor
vendedor1.vender(orden_compra, cliente1)

#Comprobamos que se haga la comision del vendedor por el producto vendido
print(f"Comisión del vendedor: {vendedor1.obtener_comision()} CLP")
