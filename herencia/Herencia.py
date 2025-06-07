class Animal:
    def __init__(self, nombre):
        self.nombre = nombre


    def hablar(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print (self .nombre, "dice: Guau!") 

class Gato(Animal):
    def hablar(self):
        print(self.nombre, "dice Miau!")

#Crear objetos
perro = Perro("Annie")
gato = Gato ("Mily")


perro.hablar()
gato.hablar()
