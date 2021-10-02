import random
posibilidades = ["+", "-", "*"]
operacion = f"{random.randint(2,9)} {random.choice(posibilidades)} {random.randint(2,9)}"
print(operacion)

usuario = int(input())

operacion = operacion.split()

if "+" in operacion:
    respuesta = (int(operacion[0]) + int(operacion[2]))
    if respuesta == usuario:
        print("Right!")
    else:
        print("Wrong!")
    
elif "-" in operacion:
    respuesta = (int(operacion[0]) - int(operacion[2]))
    if respuesta == usuario:
        print("Right!")
    else:
        print("Wrong!")
    
    
elif "*" in operacion:
    respuesta = (int(operacion[0]) * int(operacion[2]))
    if respuesta == usuario:
        print("Right!")
    else:
        print("Wrong!")
    

