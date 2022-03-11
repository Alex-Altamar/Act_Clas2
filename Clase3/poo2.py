def main():
    class Persona():
        def __init__(self):
            self.nombre = input("Ingrese el nombre:  ")
            self.apellido = input("Ingrese el apellido:  ")
            self.direccion = input("Ingrese la direccion:  ")
            self.telefono = input("Ingrese el telefono:  ")

        def mostrarPersona(self):
            print(f"Mi nombre: {self.nombre} {self.apellido} ")
            


    class Empleado(Persona):
        def __init__(self):
            super().__init__()

            self.__sueldo = float(input("Ingrese el sueldo: "))
            self.alimentacion = 120000
            self.transporte = 80000
            self.pension = 0.04
            self.salud = 0.0375
            self.deducido = (self.pension*self.__sueldo) + (self.salud*self.__sueldo)
            
            if self.__sueldo < 2000000 :
                self.devengado = (self.__sueldo + self.transporte + self.alimentacion) - self.deducido
            else:
                self.devengado = self.__sueldo - self.deducido


        def mostrarEmpleado(self):
            super().mostrarPersona()
            print(f"Sueldo: {self.__sueldo}")
            print(f"Transporte: {self.transporte}")
            print(f"Alimentacion: {self.alimentacion}")
            print(f"Pension: {self.pension}")
            print(f"Salud: {self.salud}")

        def totalDevengado(self):
        
            print(f"Total devengado: {self.devengado}")
            print(f"Total deducido: {self.deducido}")

    empleado1 = Empleado()

    #empleado1.__sueldo = 4000000

    empleado1.mostrarEmpleado()
    empleado1.totalDevengado()

if __name__ == "__main__":
    main()
