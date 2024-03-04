import time
from datetime import datetime

def oraculo(nombre, numEdad):
    caracter = nombre[-1] 
    valorCaracter = ord(caracter)
    hora_actual = datetime.now().time()
    segundo = hora_actual.second
    suerte = numEdad + valorCaracter + segundo
    ultimoDigito = str(suerte)[-1]
    return ultimoDigito

salir = " "

while salir != "1":
    nombre = input(str("Bienvenido al Oráculo de la fortuna, por favor ingrese su nombre -> "))
    edad = input(f"Hola {nombre}, por favor ingresa tu edad -> ")
    numEdad = int(edad)

    pregunta = input("Ingresa sobre qué quieres que te aconseje el oráculo -> ")

    print("mmmmm... Muy bien estoy viendo tu futuro....")

    # Demora X cantidad de segundos en mostrar un mensaje
    time.sleep(1)
    print("....")
    time.sleep(2)
    print(f"....calma, {nombre} .....")
    time.sleep(3)

    # Obtener el último dígito, transformándolo en cadena
    ultimoDigito = oraculo(nombre, numEdad)

    print(f"{nombre}, tu número de la suerte es {ultimoDigito}")

    # Ciclo para entregar respuestas a la pregunta en base al último número del "numero de la suerte"
    # ya que así está incluido el 0.
    match ultimoDigito:
        case '1':
            print("Consejo para tu situación: El camino hacia la claridad comienza con la introspección.")
        case '2':
            print("Consejo para tu situación: Las respuestas se revelan cuando el corazón y la mente están en armonía.")
        case '3':
            print("Consejo para tu situación: A veces, la verdadera sabiduría está en aceptar lo desconocido.")
        case '4':
            print("Consejo para tu situación: La paciencia es la llave que abre las puertas del entendimiento.")
        case '5':
            print("Consejo para tu situación: Tu destino está entrelazado con las decisiones que tomas en el presente.")
        case '6':
            print("Consejo para tu situación: La sabiduría se encuentra en escuchar a tu intuición con atención.")
        case '7':
            print("Consejo para tu situación: Recuerda que el cambio es la única constante en la vida.")
        case '8':
            print("Consejo para tu situación: Explora nuevas perspectivas para descubrir respuestas inesperadas.")
        case '9':
            print("Consejo para tu situación: Aprovecha las lecciones del pasado para iluminar tu camino futuro.")
        case '0':
            print("Consejo para tu situación: Confía en el proceso y permite que el tiempo revele su magia")

    salir = input("¿Quieres terminar el oráculo (1) o continuar(2)? -> ")

print("Gracias, nos vemos pronto (Si el Dios de la programación lo permite).")
