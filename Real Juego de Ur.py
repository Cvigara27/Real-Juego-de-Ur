# -------------------- -----El Real Juego de Ur -------------------------------
# --------- Por Andreu Pomar, Albert Valado y Cristian Vigara -----------------


# ------- Variables y diccionarios ---------------------------------------

#Variables
turno=2
opcion_menu = 0
opcion_recorrido = 1
victoria=False

#Tuplas
salvos=(23,7,11)


#Librerías
import random

#Diccionarios
J1={"1":4,"2":4,"3":4,"4":4,"5":4,"6":4,"7":4}
J2={"A":20,"B":20,"C":20,"D":20,"E":20,"F":20,"G":20}

#Listas(Recorridos)
Recorrido1J1=[4,3,2,1,0,8,9,10,11,12,13,14,15,7,6,5]
Recorrido1J2=[20,19,18,17,16,8,9,10,11,12,13,14,15,23,22,21]
Recorrido2J1=[4,0,1,2,3,11,12,13,14,6,7,15,23,22,14,13,12,11,10,9,8,5]
Recorrido2J2=[20,16,17,18,19,11,12,13,14,22,23,15,7,6,14,13,12,11,10,9,8,21]

# ------- Funciones ------------------------------------------------------
def menu_principal ():
    global opcion_menu
    opcion_menu = 0
    while opcion_menu != 4 and opcion_menu != 1:
        print ("REAL JUEGO DE UR\n")
        print ("----------------\n")
        print ("1) Jugar")
        print ("2) Configuración")
        print ("3) Ayuda")
        print ("4) Salir")
        opcion_menu = int(input("Seleccione una opción:"))
    
        if opcion_menu == 1:
            limpiar_pantalla()
            bucle_juego(victoria)
        
        if opcion_menu == 2:
            configuracion_menu()
            opcion_menu = 0
            limpiar_pantalla()
        
        if opcion_menu == 3:
            ayuda_menu()
            opcion_menu = 0
            limpiar_pantalla()

# ------- Pequeña descripción del juego ----------------------------------
def ayuda_menu():
    limpiar_pantalla()
    print("-------------------------- REGLAS ---------------------------------")
    print("El real juego de Ur es un juego por turnos para dos jugadores,\n"
          "cada uno con siete fichas, y se usan cuatro dados piramidales que\n"
          "a efectos prácticos son dados de dos caras. Las fichas recorren un\n"
          "tablero según la puntuación obtenida en los dados, intentando llegar\n"
          "al extremo opuesto para salir y anotar un punto. El primer jugador\n"
          "en sacar todas sus fichas del tablero es el ganador. \n"
          "\n"
          "Existen algunas reglas adicionales:\n"
          "- Para salir hay que sacar el número exacto para llegar a la casilla final.\n"
          "- Cada casilla puede estar ocupada únicamente por una única ficha de\n"
          "  un solo jugador.\n"
          "- Un jugador puede devolver una ficha del rival a la posición de salida\n"
          "  si cae en su misma casilla, excepto si ocupa la casilla marcada como\n"
          "  salvo."
          "- El propio programa le indicará qué fichas puede mover en cada momento.\n"
          "\n")
    print("-------------------------- HISTORIA -------------------------------")
    print(" El real juego de Ur es uno de los juegos más antiguos que se conocen.\n"
          "Era jugado por la aristocracia de la ciudad sumeria de Ur, hace unos\n"
          "4500 años. El tablero original fue descubierto por el arqueólogo\n"
          "británico Sir Leonard Wolley en una tumba cerca de los antiguos\n"
          "márgenes del río Eufrates. Las reglas que aquí ofrecemos son una\n"
          "variación de las traducciones de tablillas de arcilla realizadas por\n"
          "Irving Finkel, especialista en escritura cuneiforme del Museo Británico.\n")
    input("Presione ENTER para continuar...")

# ------- Elegir que recorrido se hace -----------------------------------
def configuracion_menu():
    global opcion_recorrido
    limpiar_pantalla()
    print("El Real Juego de Ur ofrece dos recorridos diferentes. De manera " 
          "predeterminada está seleccionado el recorrido corto. ")
    print("1) Recorrido corto")
    print("2) Recorrido largo")
    opcion_recorrido=int(input("Seleccione el recorrido que prefiera: "))
    return opcion_recorrido

# ------- Todas las acciones que se hacen por turno ----------------------
def bucle_juego(victoria):
    global Recorrido1J1
    global Recorrido1J2
    global Recorrido2J1
    global Recorrido2J2
    while victoria == False:
        limpiar_pantalla()
        pintar_tablero()
        alternar_turno()
        resultado = tirar_dados()
        fichas_validas = comprobar_movimientos(turno,resultado)
        seleccion = elegir_ficha (turno, fichas_validas)
        mover_ficha (turno, resultado, seleccion, Recorrido1J1, Recorrido1J2, Recorrido2J1, Recorrido2J2)
        comprobar_victoria(turno,J1,J2)
    

# ------- Pinta el tablero -----------------------------------------------
def pintar_tablero():
    tablero=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    for k,v in J1.items():
        tablero[v] = k
    for k,v in J2.items():
        tablero[v] = k
    print("§═══§┌───┐╔═══╗┌───┐          ╔═══╗§───§")
    print("║ %s ║│ %s │║ %s ║│ %s │          ║ %s ║│ %s │" % (tablero[0],tablero[1],tablero[2],tablero[3],tablero[6],tablero[7]))
    print("§═══§└───┘╚═══╝└───┘          ╚═══╝§───§")
    print("┌───┐╔═══╗┌───┐§═══§┌───┐╔═══╗┌───┐╔═══╗")
    print("│ %s │║ %s ║│ %s │║ %s ║│ %s │║ %s ║│ %s │║ %s ║" % (tablero[8],tablero[9],tablero[10],tablero[11],tablero[12],tablero[13],tablero[14],tablero[15]))
    print("└───┘╚═══╝└───┘§═══§└───┘╚═══╝└───┘╚═══╝")
    print("§═══§┌───┐╔═══╗┌───┐          ╔═══╗§───§")
    print("║ %s ║│ %s │║ %s ║│ %s │          ║ %s ║│ %s │" % (tablero[16],tablero[17],tablero[18],tablero[19],tablero[22],tablero[23]))
    print("§═══§└───┘╚═══╝└───┘          ╚═══╝§───§")

# ------- Limpia la pantalla con muchos print en blanco ------------------
def limpiar_pantalla():
    print("\n"*100)

# ------- Cambia el turno ------------------------------------------------
def alternar_turno():
    global turno
    if turno ==1:
        turno = 2
    else:
        turno = 1
    print ("Es el turno del jugador %d" % (turno))
    return turno

# ------- Tira los dados ------------------------------------------------- 
def tirar_dados():
    d1 = random.randint (0,1)
    d2 = random.randint (0,1)
    d3 = random.randint (0,1)
    d4 = random.randint (0,1)
    resultado = d1+d2+d3+d4
    print ("¡Has sacado un %d! (%d, %d, %d, %d)" % (resultado, d1, d2, d3, d4))
    return resultado

# ------- Determina que fichas puede mover el jugar en cada turno --------
def comprobar_movimientos(turno,resultado):
    fichas_validasJ1=["1","2","3","4","5","6","7"]
    fichas_validasJ2=["A","B","C","D","E","F","G"]
    if turno == 1: # ----- Jugador 1
# -------  Elimina fichas que ya han anotado punto ------------------------
        for i in range (len (fichas_validasJ1)): 
            if J1[fichas_validasJ1[i]] == 5:
                fichas_validasJ1[i]=""

        while fichas_validasJ1.count("") > 0:
            fichas_validasJ1.remove("")
            
# ------- Elimina todas las fichas que estén en 0, menos la primera ------
        esperando = []
        for i in range (len(fichas_validasJ1)):
            if J1[fichas_validasJ1[i]] == 4:
                esperando.append(fichas_validasJ1[i])
                
        while len(esperando) > 1:
            fichas_validasJ1.remove(esperando.pop())

# ------- Eliminar fichas que vayan a pisar fichas del mismo jugador -----
        if opcion_recorrido==1:
            eliminar=[]
            for i in fichas_validasJ1:
                for x in fichas_validasJ1:
                    if (Recorrido1J1.index(J1[i])+resultado)!=15:
                        if (Recorrido1J1.index(J1[i])+resultado)==Recorrido1J1.index(J1[x]):
                            eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ1.remove(i)
        
        if opcion_recorrido==2:
            eliminar=[]
            for i in fichas_validasJ1:
                for x in fichas_validasJ1:
                    if (Recorrido2J1.index(J1[i])+resultado)!=21:
                        if (Recorrido2J1.index(J1[i])+resultado)==Recorrido2J1.index(J1[x]):
                            eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ1.remove(i)

# ------- Eliminar fichas que vayan a pisar enemigo en salvo -------------
        if opcion_recorrido==1:
            eliminar=[]
            for i in fichas_validasJ1:
                for x in fichas_validasJ2:
                    if (Recorrido1J1.index(J1[i])+resultado)==Recorrido1J2.index(J2[x]) and Recorrido1J2.index(J2[x])==8:
                        eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ1.remove(i)

        if opcion_recorrido==2:
            eliminar=[]
            for i in fichas_validasJ1:
                posicion=Recorrido2J1.index(J1[i])+resultado
                valor=Recorrido2J1[posicion]
                for x in fichas_validasJ2:
                    if valor == J2[x] and J2[x] in salvos:
                        eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ1.remove(i)

# ------- Eliminar fichas que vayan a salirse del tablero ----------------
        if opcion_recorrido==1:
            eliminar=[]
            for i in fichas_validasJ1:
                if (Recorrido1J1.index(J1[i])+resultado)>(len(Recorrido1J1)-1):
                    eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ1.remove(i)
        
        if opcion_recorrido==2:
            eliminar=[]
            for i in fichas_validasJ1:
                if (Recorrido2J1.index(J1[i])+resultado)>(len(Recorrido2J1)-1):
                    eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ1.remove(i)

        return fichas_validasJ1

    if turno == 2: # ----- Jugador 2
# ------- Elimina fichas que ya han anotado punto ------------------------
        for i in range (len (fichas_validasJ2)): 
            if J2[fichas_validasJ2[i]] == 21:
                fichas_validasJ2[i]=""

        while fichas_validasJ2.count("") > 0:
            fichas_validasJ2.remove("")
            
# ------- Elimina todas las fichas que estén en 0, menos la primera ------
        esperando = []
        for i in range (len(fichas_validasJ2)):
            if J2[fichas_validasJ2[i]] == 20:
                esperando.append(fichas_validasJ2[i])
                
        while len(esperando) > 1:
            fichas_validasJ2.remove(esperando.pop())

# ------- Eliminar las fichas que vayan a pisar fichas del mismo jugador -
        if opcion_recorrido==1:
            eliminar=[]
            for i in fichas_validasJ2:
                for x in fichas_validasJ2:
                    if (Recorrido1J2.index(J2[i])+resultado)!=15:
                        if (Recorrido1J2.index(J2[i])+resultado)==Recorrido1J2.index(J2[x]):
                            eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ2.remove(i)
        
        if opcion_recorrido==2:
            eliminar=[]
            for i in fichas_validasJ2:
                for x in fichas_validasJ2:
                    if (Recorrido2J2.index(J2[i])+resultado)!=21:
                        if (Recorrido2J2.index(J2[i])+resultado)==Recorrido2J2.index(J2[x]):
                            eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ2.remove(i)

# ------- Eliminar fichas que vayan a pisar enemigo en salvo -------------
        if opcion_recorrido==1:
            eliminar=[]
            for i in fichas_validasJ2:
                for x in fichas_validasJ1:
                    if (Recorrido1J2.index(J2[i])+resultado)==Recorrido1J1.index(J1[x]) and Recorrido1J1.index(J1[x])==8:
                        eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ2.remove(i)

        if opcion_recorrido==2:
            eliminar=[]
            for i in fichas_validasJ2:
                posicion=Recorrido2J2.index(J2[i])+resultado
                valor=Recorrido2J2[posicion]
                for x in fichas_validasJ1:
                    if valor == J1[x] and J1[x] in salvos:
                        eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ2.remove(i)

# ------- Eliminar fichas que vayan a salirse del tablero ----------------
        if opcion_recorrido==1:
            eliminar=[]
            for i in fichas_validasJ2:
                if (Recorrido1J2.index(J2[i])+resultado)>(len(Recorrido1J2)-1):
                    eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ2.remove(i)
        
        if opcion_recorrido==2:
            eliminar=[]
            for i in fichas_validasJ2:
                if (Recorrido2J2.index(J2[i])+resultado)>(len(Recorrido2J2)-1):
                    eliminar.append(i)
                
            for i in eliminar:
                fichas_validasJ2.remove(i)

        return fichas_validasJ2

# ------- Despues de comprobar las fichas se selecciona una --------------    
def elegir_ficha(turno,fichas_validas):
    if len(fichas_validas)==0:
        print("No puedes mover ninguna ficha.")
        input("Presione ENTER para continuar")
        seleccion = False
        return seleccion
    else:
        for i in fichas_validas:
            print(i)
        if turno==1:
            seleccion=input("¿Qué ficha quieres mover? ")
            while seleccion not in fichas_validas:
                seleccion=input("¡Esa ficha no es válida! ¿Qué ficha quieres mover? ")
            return seleccion          
        else:
            seleccion=input("¿Qué ficha quieres mover? ")
            while seleccion not in fichas_validas:
                seleccion=input("¡Esa ficha no es válida! ¿Qué ficha quieres mover? ")
                seleccion=seleccion.upper()
            return seleccion

# ------- Mueve una ficha/Pisa una ficha ---------------------------------    
def mover_ficha(turno,resultado,seleccion,Recorrido1J1,Recorrido1J2,Recorrido2J1,Recorrido2J2):
    if seleccion!=False: #Selección será False si la función comprobar_movimientos() no encuentra ninguna ficha válida
        if turno == 1: # ----- Jugador 1
# ------- Elimina ficha enemiga si se puede ------------------------------
            if opcion_recorrido==1:
                posicion=Recorrido1J1.index(J1[seleccion])+resultado
                valor=Recorrido1J1[posicion]
                J1[seleccion]=valor
                for i in J2.keys():
                    if J1[seleccion]==J2[i]:
                        J2[i]=20
                
            if opcion_recorrido==2:
                posicion=Recorrido2J1.index(J1[seleccion])+resultado
                valor=Recorrido2J1[posicion]
                J1[seleccion]=valor
                for i in J2.keys():
                    if J1[seleccion]==J2[i]:
                        J2[i]=20
                
        if turno == 2: # ----- Jugador 2
# ------- Elimina ficha enemiga si se puede ------------------------------
            if opcion_recorrido==1:
                posicion=Recorrido1J2.index(J2[seleccion])+resultado
                valor=Recorrido1J2[posicion]
                J2[seleccion]=valor
                for i in J1.keys():
                    if J2[seleccion]==J1[i]:
                        J1[i]=4
                
            if opcion_recorrido==2:
                posicion=Recorrido2J2.index(J2[seleccion])+resultado
                valor=Recorrido2J2[posicion]
                J2[seleccion]=valor
                for i in J1.keys():
                    if J2[seleccion]==J1[i]:
                        J1[i]=4
                                        
# ------- Comprueba si todas las fichas estan en la meta -----------------
def comprobar_victoria (turno, J1, J2):
    victoria=True
    if turno == 1:
        for i in J1.values():
            if i != 5:
                victoria=False
    else:
        for i in J2.values(): 
            if i != 21:
                victoria=False
    if victoria == True:
        limpiar_pantalla()
        print ("¡Enhorabuena! Ha ganado el jugador %d" % (turno))
        input("Pulsa ENTER para volver al menú.")
        

# ------------- Programa Principal ---------------------------------------
menu_principal()