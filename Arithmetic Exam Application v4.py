import random
posibilidades = ["+", "-", "*"]
correctas = 0
cuestionario = 0
while 1:
        level = (input("Which level do you want? Enter a number: \n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n"))
        if level == "1":
                level_description = "simple operations with numbers 2-9" 
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
                            save = input(f"Your mark is {correctas}/5. Would you like to save the result? Enter yes or no.")
                            break
                break

        elif level == "2":
                level_description = "integral squares of 11-29"
                número = random.randint(11,29)
                while 1:
                        print(número)                       

                        try:
                            usuario = int(input())
                            if usuario == número * número:
                                print("Right!")
                                correctas += 1
                                
                            else:
                                print("Wrong!")

                            cuestionario += 1                  
                            if cuestionario == 5:
                                    save = input(f"Your mark is {correctas}/5. Would you like to save the result? Enter yes or no.")
                                    break
                                    
                        
                        except:
                            print("Wrong format! Try again.")
                break
                                                                

        else:
                print("Incorrect format.")


if save in ["yes", "YES", "y", "Yes"]:
        name = input("What is your name?")
        archivo = open("results.txt","a")
        archivo.write(f"{name}: {correctas}/5 in level {level} ({level_description}).\n")
        print(f"The results are saved in \"results.txt\".")
        archivo.close()


        

