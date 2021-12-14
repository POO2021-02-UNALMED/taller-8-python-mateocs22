from futbolista import Futbolista
from deportista import Deportista
from persona import Persona

if __name__ == "__main__":

   
    futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
    ok = False
    if (futbolista.__str__() == "Mi nombre es Juan Pablo soy profesional en el deporte Futbol Tengo 30 años de edad y llevo 12 años en el deporte"):
        ok = True
    
    print(futbolista.__str__())