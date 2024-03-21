import re

class Persona:
    def __init__(self, nombre, edad, dni):
        if re.match(r'^[a-zA-Z]{2,}$', nombre):
            self.nombre = nombre
        if re.match(r'^\d+$', str(edad)) and int(edad) > 0:
            self.edad = int(edad)
        if re.match(r'^\d{8}[a-zA-Z]$', dni):
            self.dni = dni

    def __repr__(self):
        return f'{self.nombre},{self.edad},{self.dni}'

    def mostrar(personas):
        for persona in personas:
            print(persona)
    
    def mayorEdad(self):
        edades = [persona.edad for persona in personas]
        edades_ordenadas = sorted(edades)
        for edad in edades_ordenadas:
            for persona in personas:
                if persona.edad == edad:
                    print(persona)
           
persona1 = Persona ('Nerea',21,'41898712N')
persona2 = Persona ('Victor',19,'42398724D')
persona3 = Persona ('Maxi',20,'41894412M')
persona4 = Persona ('Arty',18,'46665524T')
persona5 = Persona ('Ivan',35,'41898664I')

personas = [persona1,persona2,persona3,persona4,persona5]

#personas.append(persona1)
#personas.append(persona2)
#personas.append(persona3)
#personas.append(persona4)
#personas.append(persona5)

print("Personas: ")
Persona.mostrar(personas)

print("\nPersonas ordenadas por edad (de menor a mayor):")
Persona.mayorEdad(personas)