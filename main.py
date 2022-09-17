import random
import time

#-- Text colors var  --#

BK = '\033[30m' 
RD = '\033[31m'
GRN = '\033[32m'
YLL = '\033[33m'
BL = '\033[34m'
MGTA = '\033[35m'  # Informational TextD
CYN = '\033[36m'
RST = '\033[39m'

#----------------------Restart var i+user----------#

iniciandoTrivia = True
intentos = 0

#------- Welcome message ------#

nombreUsuario = input("Ingresa tu nombre: ")
print(
    MGTA + '\n', f"Hola! {nombreUsuario}\U0001F600, vas a participar en un trivia de programación, leé con atención las preguntas encuentra la respuesta correcta, si halla la pregunta SECRETA , suma puntos extras, comienza con 0 puntos estás listo!",
    '\n' + RST)

#---------------Restart Game-----------------#
while iniciandoTrivia == True:
    intentos += 1
    puntaje = 0
    print(nombreUsuario,f"\nIntento número: {intentos}", '\n')

    #----------------init count ---------------#
    for numeroCarga in range(5, 0, -1):
        print("Iniciando en: ", numeroCarga)
        time.sleep(2)

    #------------Starting trivia1------------#

    print(CYN +
          "\n1. Determine el resultado de la siguiente instrucción Python" +
          RST)
    print(CYN + ">>> print (-1+2)", '\n' + RST)

    print(CYN + "a) Cero" + RST)
    print(CYN + "b) -1" + RST)
    print(CYN + "c) 1" + RST)
    print(CYN + "d) 2", '\n' + RST)

    #---------------alternatives and questions1------------------#
    lista_puntaje1 = [] #list 
  
    puntaje = random.randint(0, 5)
    respuesta_1 = input(CYN + "Ingrese una opción\U0001F600 a, b, c, d:  " + RST).lower()
    while respuesta_1 not in ("a", "b", "c", "d", "x"):
        respuesta_1 = input(
            "Elige las siguientes opciones a, b, c, d: ").lower()

    if respuesta_1 == "x":
      
        puntaje += puntaje 
        lista_puntaje1.append(puntaje)
        print(CYN + f"{nombreUsuario} tienes puntos extras! \U0001F643",
              '\n' + RST)

    elif respuesta_1 == "a":
        puntaje = -3
        lista_puntaje1.append(puntaje) 
        print(CYN + "Respuesta incorrecta \U0001F611", '\n' + RST)

    elif respuesta_1 == "b":
        puntaje = -3
        lista_puntaje1.append(puntaje)
        print(CYN + "Respuesta incorrecta \U0001F611", '\n' + RST)

    elif respuesta_1 == "d":
        puntaje = -3
        lista_puntaje1.append(puntaje)
        print(CYN + "Respuesta incorrecta \U0001F611", '\n' + RST)

    else:
        puntaje += puntaje
        lista_puntaje1.append(puntaje)
        print(CYN + "Respuesta correcta! \U0001F37B", '\n' + RST)

        #------------Starting trivia2------------#

    print(RD + "2. La salida de la siguiente instrucción Python es:" + RST)
    print(RD + "print(1+ 2 + 3 + 4 + 5 * 2)", '\n' + RST)

    print(RD + "a) 30" + RST)
    print(RD + "b) 25" + RST)
    print(RD + "c) 20" + RST)
    print(RD + "d) 15", '\n' + RST)

    #---------------alternatives and questions2------------------#

    lista_puntaje2 = [] #list 
  
    puntaje = random.randint(0, 5)
    respuesta_2 = input(RD + "Ingrese una opción\U0001F600 a, b, c, d:  " + RST).lower()

    while respuesta_2 not in ("a", "b", "c", "d", "v"):
        respuesta_2 = input(
            "Opción incorrecta vuelve a ingresar a, b, c, d: ").lower()

    if respuesta_2 == "v":
        puntaje += puntaje
        lista_puntaje2.append(puntaje)
        print(
            RD +
            f"{nombreUsuario} esto es secreto tienes puntos extras! \U0001F643",
            '\n' + RST)

    elif respuesta_2 == "a":
        puntaje = -3
        lista_puntaje2.append(puntaje)
        print(RD + "Respuesta incorrecta \U0001F611", '\n' + RST)

    elif respuesta_2 == "b":
        puntaje = -3
        lista_puntaje2.append(puntaje)
        print(RD + "Respuesta incorrecta \U0001F611", '\n' + RST)

    elif respuesta_2 == "d":
        puntaje = -3
        lista_puntaje2.append(puntaje)
        print(RD + "Respuesta incorrecta \U0001F611", '\n' + RST)

    else:
        puntaje += puntaje
        lista_puntaje2.append(puntaje)
        print(RD + "Respuesta correcta! \U0001F37B", '\n' + RST)

        #------------Starting trivia3------------#

    print(
        YLL +
        "3. ¿Cuál es el resultado que se obtiene al ejecutar esta instrucción Python?"
        + RST)
    print(YLL + ">>> print(1+ 2 + 3 + (4 + 5) * 2)", '\n' + RST)

    print(YLL + "a) 26" + RST)
    print(YLL + "b) 28" + RST)
    print(YLL + "c) 28" + RST)
    print(YLL + "d) 24", '\n' + RST)

    #---------------alternatives and questions3------------------#

    lista_puntaje3 = [] #list 
  
    puntaje = random.randint(0, 5)
    respuesta_3 = input(YLL + "Ingrese una opción\U0001F600 a, b, c, d:  " +
                        RST).lower()

    while respuesta_3 not in ("a", "b", "c", "d", "h"):
        respuesta_3 = input(
            "Opción incorrecta vuelve a ingresar a, b, c, d: ").lower()

    if respuesta_3 == "h":
        puntaje += puntaje
        lista_puntaje3.append(puntaje)
        print(
            YLL +
            f"{nombreUsuario} esto es secreto tienes puntos extras! \U0001F643",
            '\n' + RST)

    elif respuesta_3 == "a":
        puntaje = -3
        lista_puntaje3.append(puntaje)
        print(YLL + "Respuesta incorrecta \U0001F611", '\n' + RST)

    elif respuesta_3 == "b":
        puntaje = -3
        puntaje -= puntaje-5
        print(YLL + "Respuesta incorrecta \U0001F611", '\n' + RST)

    elif respuesta_3 == "c":
        puntaje = -3
        lista_puntaje3.append(puntaje)
        print(YLL + "Respuesta incorrecta \U0001F611", '\n' + RST)
    else:
        puntaje += puntaje
        lista_puntaje3.append(puntaje)
        print(YLL + "Respuesta correcta! \U0001F37B", '\n' + RST)

        #------------Starting trivia4------------#
    
    print(
        GRN +
        "4. ¿Cuál es el resultado que se obtiene al ejecutar esta instrucción Python?"
        + RST)
    print(GRN + ">>> print(17 % 3)", '\n' + RST)

    print(GRN + "a) 5" + RST)
    print(GRN + "b) 3" + RST)
    print(GRN + "c) 2" + RST)
    print(GRN + "d) 1", '\n' + RST)

    #---------------alternatives and questions4------------------#
    lista_puntaje4 = [] #list 
  
    puntaje = random.randint(0, 5)
    respuesta_4 = input(GRN + "Ingrese una opción\U0001F600 a, b, c, d:  " +
                        RST).lower()

    while respuesta_4 not in ("a", "b", "c", "d", "l"):
        respuesta_4 = input("Opción incorrecta vuelve a ingresar a, b, c, d: ")

    if respuesta_4 == "l":
      puntaje += puntaje
      lista_puntaje4.append(puntaje)
      print(
            GRN +
            f"{nombreUsuario} esto es secreto tienes puntos extras! \U0001F643",
            '\n' + RST)

    elif respuesta_4 == "a":
        puntaje = -3
        lista_puntaje4.append(puntaje)
        print(GRN + "Respuesta incorrecta \U0001F611", '\n' + RST)

    elif respuesta_4 == "b":
        puntaje = -3
        lista_puntaje4.append(puntaje)
        print(GRN + "Respuesta incorrecta \U0001F611", '\n' + RST)

    elif respuesta_4 == "d":
        puntaje = -3
        lista_puntaje4.append(puntaje)
        print(GRN + "Respuesta incorrecta \U0001F611", '\n' + RST)
      
    else:
        puntaje += puntaje
        lista_puntaje4.append(puntaje)
        print(GRN + "Respuesta correcta! \U0001F37B", '\n' + RST)

        #------------Starting trivia5------------#

    print(BK + "5. Determine el resultado de la siguiente instrucción Python" +
          RST)
    print(BK + ">>> print((8+6+5)%(2**2))", '\n' + RST)

    print(BK + "a) 6" + RST)
    print(BK + "b) 5" + RST)
    print(BK + "c) 4" + RST)
    print(BK + "d) 3", '\n' + RST)

    #---------------alternatives and questions5------------------#
    lista_puntaje5 = [] #list 
    puntaje = random.randint(0, 5)
    respuesta_5 = input(BK + "Ingrese una opción\U0001F600 a, b, c, d:  " +
                        RST).lower()

    while respuesta_5 not in ("a", "b", "c", "d", "w"):
        respuesta_5 = input("Opción incorrecta vuelve a ingresar a, b, c, d: ")

    if respuesta_5 == "w":
      puntaje += puntaje
      lista_puntaje5.append(puntaje)
      print(
            BK +
            f"{nombreUsuario} esto es secreto tienes puntos extras! \U0001F643",
            '\n' + RST)

    elif respuesta_5 == "a":
        puntaje = -3
        lista_puntaje5.append(puntaje)
        print(BK + "Respuesta incorrecta \U0001F611", '\n' + RST)

    elif respuesta_5 == "b":
        puntaje = -3
        lista_puntaje5.append(puntaje)
        print(BK + "Respuesta incorrecta \U0001F611", '\n' + RST)

    elif respuesta_5 == "c":
        puntaje = -3
        lista_puntaje5.append(puntaje)
        print(BK + "Respuesta incorrecta \U0001F611", '\n' + RST)
    else:
        puntaje += puntaje
        lista_puntaje5.append(puntaje)
        print(BK + "Respuesta correcta! \U0001F37B", '\n' + RST)

        #-------------goodbye message--------------------#
    print("pregunta 1 obtuviste un puntaje de: ",lista_puntaje1[0])
    print("pregunta 2 obtuviste un puntaje de: ",lista_puntaje2[0])
    print("pregunta 3 obtuviste un puntaje de: ",lista_puntaje3[0])
    print("pregunta 4 obtuviste un puntaje de: ",lista_puntaje4[0])
    print("pregunta 5 obtuviste un puntaje de: ",lista_puntaje5[0])
  
    print(f"intentos: {intentos} has obtenido un puntaje final: ",sum(lista_puntaje1 + lista_puntaje2 + lista_puntaje3 + lista_puntaje4 + lista_puntaje5))
  
  
    print("\n¿Desea continuar?")

  
    repetir_trivia = input(
        "Ingresa, 'si' para repetir o cualquier tecla para salir: ").lower()

    if repetir_trivia != "si":
        print(
            CYN +
            f"\nEspero {nombreUsuario} que lo hayas pasado genial!\U0001F37B\U0001F37B\U0001F37B"
            + RST)

        iniciandoTrivia = False
