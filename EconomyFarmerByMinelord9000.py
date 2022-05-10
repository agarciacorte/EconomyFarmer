import keyboard
import time


def escribirDepAll(prefix):
    espera = 0.2
    keyboard.write(prefix)
    time.sleep(espera)
    keyboard.write("d")
    time.sleep(espera)
    keyboard.write("e")
    time.sleep(espera)
    keyboard.write("p")
    time.sleep(espera)
    keyboard.write(" ")
    time.sleep(espera)
    keyboard.write("a")
    time.sleep(espera)
    keyboard.write("l")
    time.sleep(espera)
    keyboard.write("l")
    time.sleep(espera)

def escribirWork(prefix):
    espera = 0.2
    keyboard.write(prefix)
    time.sleep(espera)
    keyboard.write("w")
    time.sleep(espera)
    keyboard.write("o")
    time.sleep(espera)
    keyboard.write("r")
    time.sleep(espera)
    keyboard.write("k")

menu = True
print("\n")
print("           ╭━━━╮                   ╭━━━╮")
print("           ┃╭━━╯                   ┃╭━━╯")
print("           ┃╰━━┳━━┳━━┳━╮╭━━┳╮╭┳╮ ╭╮┃╰━━┳━━┳━┳╮╭┳━━┳━╮")
print("           ┃╭━━┫╭━┫╭╮┃╭╮┫╭╮┃╰╯┃┃ ┃┃┃╭━━┫╭╮┃╭┫╰╯┃┃━┫╭╯")
print("           ┃╰━━┫╰━┫╰╯┃┃┃┃╰╯┃┃┃┃╰━╯┃┃┃  ┃╭╮┃┃┃┃┃┃┃━┫┃")
print("           ╰━━━┻━━┻━━┻╯╰┻━━┻┻┻┻━╮╭╯╰╯  ╰╯╰┻╯╰┻┻┻━━┻╯")
print("                              ╭━╯┃")
print("                              ╰━━╯")
time.sleep(0.8)
print("\nBienvenido al generador de dinero afk para UnbelievaBoat Discord Bot")
time.sleep(0.5)
print("Created by: Minelord9000")

while(menu):
    print("\nCONFIGURACIÓN:")
    prefix = input("   Ingrese el prefix: ")
    print("      Prefix establecido en: [" + prefix + "]")
    time.sleep(0.8)
    cantidad = input("\n   Ingrese el número de repeticiones (deje en blanco para que nunca finalice): ")
    if cantidad.isdigit():
        print("      El programa se ejecutará " + cantidad + " veces\n")
        iteraciones = int(cantidad)
    else:
        print("      El programa se ejecutará infinitamente\n")
        iteraciones = 99999
    time.sleep(0.8)
    
    enfriamiento = input("   Ingrese el tiempo (en segundos) que dura el cooldown de work. (por default es de 30): ")
    if enfriamiento.isdigit():
        print("      Tiempo de cooldown establecido en " + enfriamiento + " segundos\n")
        cooldown = int(enfriamiento)
    else:
        print("      Tiempo de cooldown establecido en 30 segundos (default)\n")
        cooldown = 30
    time.sleep(0.8)

    confirmacion = input("   Desea continuar con la ejecución?\n      1.- Empezar la ejecución\n      2.- Regresar a la configuración\n   Ingrese [1] o [2]: ")
    if confirmacion == "1":
        menu = False
    else:
        pass
    time.sleep(1)

print('\nIMPORTANTE: El equipo no se puede usar durante la ejecución.')
time.sleep(2)

print('            Para detener el proceso pulse las teclas [Ctl] + [C].')
time.sleep(2)

print('            PREPARECE LA EJECUCIÓN COMENZARÁ EN ' + str(30 + cooldown) + ' segundos.')
time.sleep(2)

print('            Mantenga abierto el canal de economia y de un clic sobre el cuadro de enviar mensaje.\n            POSTERIORMENTE YA NO UTILICE EL EQUIPO.')
time.sleep(30)
print('            La ejecución comienza en breve.')
iteracionEspecial = 10
for i in range(iteraciones):
    time.sleep(cooldown + 0.5)

    if iteracionEspecial == i:
        iteracionEspecial += 10
        escribirDepAll(prefix)
        print ( '[' + str(i) + ']' + 'Guardando tu dinero...')
    else:
        escribirWork(prefix)
        print ( '[' + str(i) + ']' + 'Farmeando con work...')
        
    keyboard.send("enter")

escribirDepAll(prefix)
keyboard.send("enter")

fin = input("La ejecución ha finalizado. Precione [Enter] para cerrar...\n\n")
if fin == "":
    pass
else:
    pass
