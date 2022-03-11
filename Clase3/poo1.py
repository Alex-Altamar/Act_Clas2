def main():
    class Persona():
        nombre = "Alex"
        apellido = "altamar"
        direccion = "km 1"
        telefono = "3043810635"

        def mostrarPersona(self):
            print(f"Mi nombre: {self.nombre} {self.apellido} ")
    
    persona1 = Persona() #crear una instancia de la clase 
    persona1.mostrarPersona()

    persona2 = Persona()
    persona2.nombre = "Doris"
    persona2.apellido = "Altamar"
    persona2.direccion = "km 2"
    persona2.telefono = "3145942776"

    persona2.mostrarPersona()

if __name__ == "__main__":
    main()