print("*****************************")
print("Comparación entre dos valores")
print("*****************************\n")

numero_uno=int(input("Ingrese el primer valor: "))
numero_dos=int(input("Ingrese el segundo valor: "))
print("Los números comparados son: " + str(numero_uno) + " y " + str(numero_dos))

print("Los operadores que se cumplen son: ")

if numero_uno < numero_dos:
    print("Es menor que..")

if numero_uno > numero_dos:
    print("Es mayor que..")

if numero_uno == numero_dos:
    print("Es igual a..")

if numero_uno >= numero_dos:
    print("Es mayor igual a..")

if numero_uno <= numero_dos:
    print("Es menor igual a..")
               
if numero_uno != numero_dos:
    print("Es diferente a..")
