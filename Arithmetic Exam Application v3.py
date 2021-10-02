import random
posibilidades = ["+", "-", "*"]
correctas = 0
cuestionario = 0
while 1:
        operacion = f"{random.randint(2,9)} {random.choice(posibilidades)} {random.randint(2,9)}"
        print(operacion)
        
        operacion = operacion.split()

        if "+" in operacion:

            while 1:               
                try:
                    usuario = int(input())
                    respuesta = (int(operacion[0]) + int(operacion[2]))
                    if respuesta == usuario:
                        print("Right!")
                        correctas += 1
                        
                    else:
                        print("Wrong!")
                        
                    break
                        
                
                except:
                    print("Incorrect format.")    
                    
            
            
        elif "-" in operacion:

            while 1:
                try:
                    usuario = int(input())
                    respuesta = (int(operacion[0]) - int(operacion[2]))
                    if respuesta == usuario:
                        print("Right!")
                        correctas += 1
                    else:
                        print("Wrong!")
                    break
                except:
                    print("Incorrect format.")    
                    

                
            
            
        elif "*" in operacion:

            while 1:
                try:
                    usuario = int(input())
                    respuesta = (int(operacion[0]) * int(operacion[2]))
                    if respuesta == usuario:
                        print("Right!")
                        correctas += 1
                    else:
                        print("Wrong!")
                    break
                except:
                    print("Incorrect format.")   
                        

        cuestionario += 1
                        
        if cuestionario == 5:
            print(f"Your mark is {correctas}/5")
            break




    
        

