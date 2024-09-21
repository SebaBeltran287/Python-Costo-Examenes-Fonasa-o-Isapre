import math
import os
os.system("cls")
total=0
print("1. Fonasa")
print("2. Isapre")
opcion=input("Ingrese su opcion: ")
examen1=input("Hemograma $1500 (si/no): ")
if examen1=="si":
    total=total+1500
examen2=input("Orina Completa $1750 (si/no): ")
if examen2=="si":
    total=total+1750
examen3=input("E.C.G. $1850 (si/no): ")
if examen3=="si":
    total=total+1850
examen4=input("Perfil Lipídico $1250 (si/no): ")
if examen4=="si":
    total=total+1250
print(f"El total es {total}")
if opcion=="1":
    total=total*0.9
    print(f"El total con descuento es: {total}")
