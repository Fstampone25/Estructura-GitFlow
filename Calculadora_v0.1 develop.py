

numero1 = int(input("ingrese el primer numero: "))

numero2 = int(input("ingrese el segundo numero: "))

operacion = input("elegi la operacion + o -: ")

if operacion == "+":
    resultado = numero1 + numero2
    print("resultado: ", resultado)

elif operacion == "-":
    resultado = numero1 - numero2
    print("resultado: ", resultado)

else:
    print("operacion no valida")
