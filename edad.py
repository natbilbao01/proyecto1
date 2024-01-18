nombre =input("ingrese su numero de cedula: ")
edad = int(input("ingrese por favor su edad:"))
if edad >=18:
    print(f"{nombre},Eres mayor de edad")
else:
    print(f"{nombre},Eres menor de edad")
