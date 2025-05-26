#Ejercicios de clase pero usando las clases de Python

import os
os.system('cls' if os.name == 'nt' else 'clear')

class EjerciciosClase:
    def __init__(self,nombre, perro, gato, a, b Operacion, Total, Descuento, ISV, ValorCompra, Subtotal, TotalPagar, AnioActual, AnioNacimiento, Edad, TablaMultiplicar, Num, Diametro, Suma, Resta, Multiplicacion, Division, x, y, Potencia):
        self.nombre = nombre
        self.perro = perro
        self.gato = gato 
        self.a = a
        self.b = b
        self.Operacion = operacion
        self.Total = Total
        self.Descuento = Descuento
        self.ISV = ISV
        self.ValorCompra = ValorCompra
        self.Subtotal = Subtotal
        self.TotalPagar = TotalPagar
        self.AnioCtual = AnioActual
        self.AnioNacimiento = AnioNacimiento
        self.Edad = Edad
        self.TablaMultiplicar = TablaMultiplicarMultiplicar
        self.Num =Num
        self.Diametro = Diametro
        self.Suma = Suma
        self.Resta = Resta
        self.Multiplicacion = Multiplicacion
        self.Division = Division
        self.x = x
        self.y = y
        self.Potencia = Potencia 

        def Condicionales (self):
            self.a = int(input("Ingrese un numero: "))
            if self.a % 2 == 0:
                print(f"{self.a} es un numero par")
            else:
                print(f"{self.a} es un numero impar")

        def Ejercicio1(self):
            self.Total = 0
            self.Descuento = 0
            self.ISV = 0.15

            self.ValorCompra = float(input("Ingrese el valor de la compra: "))
            if self.ValorCompra > 1000:
                self.Descuento = 0.25
            else:
                self.Descuento = 0
            self.Total = self.ValorCompra - (self.ValorCompra * self.Descuento)
            self.Total = self.Total + (self.Total * self.ISV)
            print(f"El total a pagara es: {self.Total}")

        def Ejercicio2(self):
            self.AnioActual = 2025
            self.AnioNacimiento = float(input("Ingrese su año de nacimiento: "))
            self.Edad = self.AnioActual - self.AnioNacimiento

            print(f"Su edad es: {self.Edad} anios")

            if self.Edad >= 21:
                print("Usted es mayor de edad")
            else:
                print("Usted es menor de edad por tener menos de 21 anios")

            if self.Edad >= 18:
                print("Ya puedes ir a votar")
            else:
                print("Aun no puedes ir a votar")

        def Ejercicio3(self):
            self.TablaMultiplicar = int(input("Ingrese el numero de la tabla de multiplicar que desea ver: "))
            print(f"Tabla de multiplicar del {self.TablaMultiplicar}")
            for i in range(1, 11):
                print(f"{self.TablaMultiplicar} x {i} = {self.TablaMultiplicar * i}")

        