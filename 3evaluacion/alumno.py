class Alumno:
    
    def __init__(self, instituto, clase, edad, estatura, gafas, nombre):
        self.instituto = instituto
        self.clase = clase
        self.edad = int(edad)
        self.estatura = float(estatura)
        self.gafas = gafas
        self.nombre = nombre

    def __repr__(self):
        return f'Alumno {self.instituto}, {self.clase}, {self.edad}, {self.estatura}, {self.gafas}'

    def mayores_edad(self):
        print("Alumnos mayores de edad:")
        for alumno in alumnos:
            if alumno.edad >= 18:
                print(alumno)

    def filtro_instituto(self):
        selc_insti = input("¿Qué instituto quieres seleccionar?")
        print(f"Alumnos del instituto {selc_insti}:")
        for alumno in alumnos:
            if alumno.instituto == selc_insti:
                print(alumno)

    def con_gafas(self):
        return self.gafas


alumnos = [
    Alumno("Colegio A", "1A", 17, 1.65, False, "Pedro"),
    Alumno("Colegio B", "2B", 18, 1.70, True, "Juan"),
    Alumno("Colegio A", "3A", 19, 1.80, True, "María"),
    Alumno("Colegio C", "4A", 16, 1.75, False, "Ana"),
    Alumno("Colegio B", "5A", 17, 1.68, True, "Luis"),
    Alumno("Colegio A", "6A", 18, 1.72, False, "Elena"),
    Alumno("Colegio C", "7A", 17, 1.67, True, "Carlos"),
    Alumno("Colegio A", "8A", 16, 1.69, False, "Marta"),
    Alumno("Colegio B", "9A", 18, 1.71, True, "David"),
    Alumno("Colegio A", "10A", 17, 1.66, False, "Laura"),
    Alumno("Colegio B", "11A", 16, 1.68, True, "Sofía"),
    Alumno("Colegio C", "12A", 18, 1.70, False, "Diego"),
    Alumno("Colegio A", "13A", 17, 1.73, True, "Eva"),
    Alumno("Colegio B", "14A", 16, 1.67, False, "Pablo"),
    Alumno("Colegio C", "15A", 18, 1.72, True, "Carmen"),
    Alumno("Colegio A", "16A", 17, 1.69, False, "Alberto"),
    Alumno("Colegio B", "17A", 18, 1.70, True, "Lucía"),
    Alumno("Colegio C", "18A", 16, 1.68, False, "Antonio"),
    Alumno("Colegio A", "19A", 17, 1.71, True, "Isabel"),
    Alumno("Colegio B", "20A", 18, 1.73, False, "Ana")
]

while True:
    print("1 para filtrar por instituto")
    print("2 para mostrar mayores de edad")
    print("3 para mostrar alumnos con gafas")
    print("4 para salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        Alumno().filtro_instituto()
    elif opcion == "2":
        Alumno().mayores_edad()
    elif opcion == "3":
        print("Alumnos que usan gafas:")
        for alumno in alumnos:
            if alumno.con_gafas():
                print(alumno)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
