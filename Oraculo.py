import time
from datetime import datetime

#Este programa es un oraculo que da consejos de a cuedo a especificaciones dadas por el usuario
salir = " "

 

nombre = input(str("Bienvenido al Oraculo de la fortuna por favor ingrese su nombre -> ")) 

edad = input(f"Hola {nombre}, por favor ingresa tu edad -> ")
numEdad = int(edad)

while salir != "1":

 Pregunta = input("Ingresa sobre que quieres que te aconseje el oraculo -> ")

 print("mmmmm... Muy bien estoy viendo tu futuro....")

#demora X cantidad de segundos en mostrar un mensaje
 time.sleep(1)

 print("....")
 time.sleep(2)

 print(f"....calma, {nombre} .....")


 time.sleep(3)

 #indexado con valor negativo
 caracter = nombre[-1]
 #obtener el valor  entero que representa el Unicode del carácter proporcionado
 valorCaracter = ord(caracter)

 #Obtener segundo actual para agregarle a la variable y que vaya cambiando segun el digito.
 hora_actual = datetime.now().time()
 #obtener el segundo
 segundo = hora_actual.second

 #Suma de la edad mas el valor de unicode.
 suerte = numEdad + valorCaracter + segundo
 print(f"{nombre}, tu numero de la suerte es {suerte}")


 #Obtener el ultimo digito, transformandolo en cadena
 ultimoDigito = str(suerte)[-1]

 #Ciclo para entregar respuestas a la pregunta en base al ultimo numero del "numero de la suerte", ya que asi esta incluido el 0.
 match ultimoDigito:
  case '1':
   print(" Consejo para tu situacion: El camino hacia la claridad comienza con la introspección.")
  case '2':
   print("Consejo para tu situacion: Las respuestas se revelan cuando el corazón y la mente están en armonía.")
  case '3':
   print("Consejo para tu situacion:  A veces, la verdadera sabiduría está en aceptar lo desconocido.")
  case '4':
   print("Consejo para tu situacion: La paciencia es la llave que abre las puertas del entendimiento.")
  case '5':
   print(" Consejo para tu situacion:  Tu destino está entrelazado con las decisiones que tomas en el presente.")
  case '6':
   print("Consejo para tu situacion:  La sabiduría se encuentra en escuchar a tu intuición con atención.")
  case '7':
   print("Consejo para tu situacion:  Recuerda que el cambio es la única constante en la vida.")
  case '8':
   print("Consejo para tu situacion:  Explora nuevas perspectivas para descubrir respuestas inesperadas.")
  case '9':
   print("Consejo para tu situacion:  Aprovecha las lecciones del pasado para iluminar tu camino futuro.")
  case '0':
   print("Consejo para tu situacion:  Confía en el proceso y permite que el tiempo revele su magia")
   





 salir = input("¿Quieres terminar el oraculo (1) o continuar(2)? -> ")

print("Gracias, nos vemos pronto (Si el Dios de la programacion lo permite).")

