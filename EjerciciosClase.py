#Ejercicios de clase pero usando las clases de Python

import os
os.system('cls' if os.name == 'nt' else 'clear')

class EjerciciosClase:
     def __init__(self, nombre, perro, gato, a, b, operacion, Total, Descuento, ISV, ValorCompra, Subtotal, TotalPagar, AnioActual, AnioNacimiento, Edad, TablaMultiplicar, Num, Diametro, Suma, Resta, Multiplicacion, Division, x, y, Potencia):
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
        self.TablaMultiplicar = TablaMultiplicar
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

        def Ejercicio4(self):
            self.i = 1
            self.Num = int(input("Por favor ingrese un numero de la tabla de multiplicar que desee ver: "))
            print(f"Tabla de multiplicar del {self.Num}")
            while self.i <= 10:
                print(f"{self.Num} x {self.i} = {self.Num * self.i}")
                self.i += 1
        
        def EjercicioCicloFor(Self):
            for i in range(1, 11):
                print(i)

        def EjercicioTablaDel5(self):
            print("Tabla del 5")
            for i in range(1, 11):
                print(f"5 x {i} = {5 * i}")

        def EjercicioCicloWhile(self):
            self.i = 1
            while self.i <= 10:
                print(self.i)
                self.i += 1
        
        def HolaMundo(self):
            print("Hola Mundo")
        
        def OperacionesAritmeticas(self):
            a = 10
            b = 5

            Suma = a + b
            print(f"{a} + {b} = {Suma}")

            Resta = a - b
            print(f"{a} - {b} = {Resta}")

            Multiplicacion = a * b
            print(f"{a} * {b} = {Multiplicacion}")

            Div = a / b
            print(f"{a} / {b} = {Div}")

            x = int(input("x: "))
            y = int(input("y: "))

            # Potencia
            Potencia = x ** y
            print(f"{x} ^ {y} = {Potencia}")

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} esta comiendo")

    def correr(self):
        print(f"{self.nombre} esta corriendo")

class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} gua gua gua")



        