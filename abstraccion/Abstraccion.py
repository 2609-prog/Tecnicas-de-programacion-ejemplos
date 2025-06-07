class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

# Usamos la clase
calc = Calculadora(10, 5)
print("Suma:", calc.sumar())
print("Resta:", calc.restar())
