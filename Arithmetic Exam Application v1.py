operacion = input()

operacion = operacion.split()

if "+" in operacion:
    print(int(operacion[0]) + int(operacion[2]))
    
elif "-" in operacion:
    print(int(operacion[0]) - int(operacion[2]))
    
elif "*" in operacion:
    print(int(operacion[0]) * int(operacion[2]))

