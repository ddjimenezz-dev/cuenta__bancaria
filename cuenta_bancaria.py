class CuentaBancaria:
 
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.tipo = "ahorros"
 
    def depositar(self, monto):
        self.saldo = self.saldo + monto
        print("Deposito realizado. Saldo actual: " + str(self.saldo))
 
    def retirar(self, monto):
        if monto > self.saldo:
            print("No hay suficiente saldo.")
        else:
            self.saldo = self.saldo - monto
            print("Retiro realizado. Saldo actual: " + str(self.saldo))
 
    def mostrar_info(self):
        print("Titular: " + self.titular)
        print("Numero de cuenta: " + self.numero)
        print("Saldo: " + str(self.saldo))
        print("Tipo de cuenta: " + self.tipo)
 
 
# Crear dos objetos
cuenta1 = CuentaBancaria("Ana Garcia", "001-2231", 1500)
cuenta2 = CuentaBancaria("Carlos Lopez", "002-7745", 800)
 
# Usar los objetos
print("--- Cuenta 1 ---")
cuenta1.mostrar_info()
cuenta1.depositar(200)
cuenta1.retirar(100)
 
print("")
print("--- Cuenta 2 ---")
cuenta2.mostrar_info()
