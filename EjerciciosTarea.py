#Ejercicios de Tarea pero con clases

import os
os.system('cls' if os.name == 'nt' else 'clear')

class EjerciciosTarea:
    def __init__ (self, Num1, Num2, Num3, Suma, Base, Altura, Area, Num):
        self.Num1 = Num1
        self.Num2 = Num2
        self.Num3 = Num3
        self.Suma = Suma
        self.Base = Base
        self.Altura = Altura
        self.Area = Area
        self.Num = Num

        def Ejercicio1(self):
            print("Hola mundo")

        def Ejercicio2(self):
            self.num1 = int(input("Ingrese el primer numero: "))
            self.num2 = int(input("Ingrese el segundo numero: "))
            self.Suma = self.num1 + self.num2
            print(f"La suma de {self.num1} y {self.num2} es: {self.Suma}")

        def Ejercicio3(self):
            self.Base = int(input("Ingrese la base del rectangulo: "))
            self.Altura = int(input("Ingrese la altura del rectangulo: "))
            self.Area = self.Base * self.Altura
            print(f"El area del rectangulo es: {self.Area}")

        def Ejercicio4(self):
            self.Num = int(input("Ingrese un numero: "))
            if self.Num > 0:
                print(f"{self.Num} es positivo")
            elif self.Num < 0:
                print(f"{self.Num} es negativo")
            else:
                print("El numero es cero")

        def Ejercicio5(self):
            self.Num = int(input("Ingrese un numero: "))
            if self.Num % 2 == 0:
                print(f"{self.Num} es un numero par")
            else:
                print(f"{self.Num} es un numero impar")
        
        def Ejercicio6(self):
            self.Num1 = int(input("Ingrese el primer numero: "))
            self.Num2 = int(input("Ingrese el segundo numero: "))
            self.Num3 = int(input("Ingrese el tercer numero: "))
            if self.Num1 > self.Num2 and self.Num1 > self.Num3:
                print(f"{self.Num1} es el mayor")  
            elif self.Num2 > self.Num1 and self.Num2 > self.Num3:
                print(f"{self.Num2} es el mayor")
            else:
                print(f"{self.Num3} es el mayor")

        def Ejercicio7(self):
            for i in range(1, 11):
                print("Numero:", i)
            
        def Ejercicio8(self):
            self.Num = int(input("Ingrese un numero: "))
            print(f"La tabla de multiplicar del {self.Num} es:")
            for i in range(1, 11):
                print(f"{self.Num} x {i} = {self.Num * i}")

        def Ejercicio9(self):
            self.Num = int(input("Ingrese un numero: "))
            self.Suma = 0
            for i in range(1, self.Num + 1):
                self.Suma += i
            print(f"La suma de los numeros del 1 al {self.Num} es: {self.Suma}")
        
        def Ejercicio10(self):
            self.Num = int(input("Por favor ingrese un numero entero positivo: "))
            for i in range(1, self.Num + 1):
                print("*" * i)
