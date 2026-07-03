import secrets, string, sys

diccionario = {
  'letras': string.ascii_letters,
  'numeros': string.digits,
  'caracteres': string.punctuation
}

while True:
    print('=' * 70)
    print("bienvenido al mejor generador de contraseña de caseros")
    print('=' * 70)
    print('vas a tener que elegir el tipo de contraseña que queres')
    print("»1. - generar la contraseña solo de letras")
    print("»2. - generar la contraseña solo de numeros")
    print("»3. - generar la contraseña con letras y numeros")
    print("»4. - generar la contraseña con letras , numeros y caracteres")
    print("»0. - salir")
    
    opcion = input("entonces , que tipo de contraseña queres?: ")
    if opcion == "0":
        print("saliendo del mejor generador de contraseña de caseros,vuelva prontos")
        break
    elif opcion in ["1", "2", "3", "4"]:
      while True:
        largo = input("ingresa la longitud que vas a querer para la contraseña: ")
        if not largo.isdigit() or largo == "0":
            print("tenes que ingresar un número entero y que sea mayor a 0.")
            otra_opcion = input("te equivocaste y queres elegir otra opcion del menu? (s/n): ")
            if otra_opcion.lower() == "s":
                    break
            else:
                    continue
        largo = int(largo)
        break
      if type(largo) is str:
          continue
      if opcion == "1":
        caracteres_permitidos = diccionario['letras']
      elif opcion == "2":
        caracteres_permitidos = diccionario['numeros']
      elif opcion == "3":
        caracteres_permitidos = diccionario['letras'] + diccionario['numeros']
      elif opcion == "4":
        caracteres_permitidos = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']
      largo_password = largo
      password = ''

      for _ in range(largo_password):
        password += secrets.choice(caracteres_permitidos)
      print('=' * 70)
      print(f"la contraseña generada es: {password}")     
      print('=' * 70)
      break
    else:
      print("opcion no valida, lee e ingresa un numero valido.")

