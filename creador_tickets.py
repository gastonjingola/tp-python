import sys, os, random, subprocess

if not os.path.exists('tickets'):
    os.makedirs('tickets')
def limpiar_pantalla():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run([comando], shell=True)

while True:
    print('=' * 40) 
    print("hola, bienvenido al sistema de tickets")
    print('=' * 40)  
    print('elegi una opcion')
    print("1 - Alta ticket")
    print("2 - Leer ticket")
    print("3 - Salir")
    
    opcion = input("Seleccione: ")

    if opcion == '1':
        while True:
            print("ingrese los datos para ingresar un nuevo ticket")
            while True:
                nombre = input("ingresa tu nombre: ")
                if nombre.strip() != "":
                        break
                print("no tenes nombre? ingresalo no lo dejes vacio porfa.")
            while True:
                sector = input("ingresa tu sector: ")
                if sector.strip() != "":
                        break
                print("pone el sector no lo dejes vacio porfa.")
            while True:
                asunto = input("ingresa asunto?: ")
                if asunto.strip() != "":
                        break
                print("y tu asunto??? ingresalo no lo dejes vacio porfa.")
            while True:
                mensaje = input("ingresa un mensaje: ")
                if mensaje.strip() != "":
                        break
                print("cual es tu mensaje??? no puede estar vacío completalo porfa.")
            numero_random = random.randrange(1000, 9999)
            ruta = f"tickets/{numero_random}.txt"
            with open(ruta, 'w', encoding='UTF-8') as archivo:
                archivo.write(f"Nombre: {nombre}\nSector: {sector}\nAsunto: {asunto}\nMensaje: {mensaje}\nN°: {numero_random}")
            print('=' * 70)
            print("se genero el siguiente ticket")
            print('=' * 70)
            print(f"su nombre: {nombre}")
            print(f"sector: {sector}")
            print(f"asunto: {asunto}")
            print(f"mensaje: {mensaje}")
            print("mas vale que te acuerdes el numero de ticket")
            print(f"Nºticket {numero_random}")
            otro_ticket = input("queres generar otro ticket? (s/n): ")
            if otro_ticket.lower() == "s" :
                    continue
            else :
                    break   
        
    elif opcion == '2':
        intentos_fallidos = 0
        while True:
            print("Elegiste Leer ticket")
            num_ticket = input("cual es el numero de su ticket?: ")
            if not num_ticket.isdigit():
                intentos_fallidos += 1
                if intentos_fallidos >= 3:
                     print("LEE LO QUE TE PIDO NENE, SOLO INGRESA NUMEROS, SI? gracias.")
                else:
                    print("Error, pone solo numeros.")
                continue
            intentos_fallidos = 0
            ruta = f"tickets/{num_ticket}.txt"
            if  os.path.isfile(ruta):
                with open(ruta, 'r', encoding='UTF-8') as archivo:
                    print('=' * 70)
                    print (f"su ticket con el numero {num_ticket} es el siguiente")
                    print('=' * 70)
                    print(archivo.read())
            else :
                print("el numero de ticket no es correcto, verificalo porfa")
            leer_otro = input("queres leer otro ticket? (s/n): ")
            if leer_otro.lower() == "s" :
                    continue
            else :
                    break   
        
    elif opcion == '3':
        salir = input("estas segurisimo de salir del programa? si es asi presiona cualquier tecla, en caso contrario presiona la tecla n: ")
        if salir.lower() == "n" :
                    continue
        else : 
            print("Saliendo del programa...")
            sys.exit()        
    else:
        print("Opción incorrecta. Por favor, intente de nuevo.")

