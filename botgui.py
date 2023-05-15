import time
import pyautogui as pa
import random
#import ctypes para saber el tamaño de la pantalla
import ctypes


def IniciarGmail(email, password):
    """Iniciar session gmail
    parameter: email address
    parameter: password password

    """
    
    #mover mouse
    
    #abrir navegador
    pa.click(600,1000)      
    

    #click en el buscador
    pa.moveTo(300,70,8)
    pa.click(300,70)

    #escribir link
    time.sleep(3)
    pa.typewrite("https://accounts.google.com/")
    pa.press("enter")

    #Escribir Correo
    time.sleep(8)
    #pa.click(600,550,3)
    pa.typewrite(email)
    pa.press("enter")


    #Escribir Password
    time.sleep(5)
    pa.typewrite(password)
    pa.press("enter")


    #pa.dragTo(650, 580, duration=40,button="left")
    #pa.mouseDown(650, 580,duration=30,button='left')

def IniciarTextnow():
  
    """Iniciar sesion en text now
        Luego de iniciar sesion e gmail ya el navegador tiene una sesion abierta
        y se puede loggear en textnow
    """
    #mover mouse
    
    #abrir navegador
    pa.click(600,1000)
    
    pa.moveTo(330,70,5)
    #click en el buscador
    pa.click(330,70)

    #escribir link
    time.sleep(3)
    pa.typewrite("https://textnow.com/signup")
    pa.press("enter")

    #Click en registrarse con google
    pa.moveTo(600,380,5)
    pa.click(600,380)
    #click en registrase segundo intento
    pa.moveTo(600,600,5)
    pa.click(600,600) 

    #Click para seleccionar cuenta
    pa.moveTo(600,600,8)
    pa.click(600,490)

    #click para confirmar
    pa.moveTo(600,600,8)
    pa.click(760,640)
    

    #Verficar que soy humano
    time.sleep(5)
    pa.moveTo(650,580,3)
    pa.mouseDown(button='left')
    time.sleep(15)
    pa.mouseUp(button='left')

    pa.mouseDown(button='left')
    time.sleep(15)
    pa.mouseUp(button='left') 
    #pa.dragTo(650, 580,duration=20,button='left')
    #pa.moveTo(600,490,4)
    time.sleep(20)

def CodeArea():
    #abrir navegador
    #pa.click(400,1000)   
    pa.click(600,1000)  

    #Click en registrarse con google
    time.sleep(5)
    pa.moveTo(550,380,5)
    pa.click(550,380)

    pa.typewrite("310")
    pa.press("enter")

    pa.moveTo(950,350,5)

def CerrarNavegador():
    time.sleep(5)

    with pa.hold('alt'):
        pa.press('f4')

    time.sleep(2)
   


if __name__ == '__main__':

    #IniciarGmail('arturololoxoxo','092001Ss') funciono
    #IniciarTextnow()
    #CerrarNavegador()


    #IniciarGmail('polopepe548','092001Ss') fallo por intentos
    #IniciarTextnow()
    #CerrarNavegador()
    #print("1 listo")

    #IniciarGmail('dianaroja298','092001Ss')
    #IniciarTextnow()
    #CerrarNavegador()
    #print("2 listo")  

    #IniciarGmail('wmix28889','092001Ss') funciono
    #IniciarTextnow()
    #CerrarNavegador()
    #print("3 listo")

    #IniciarGmail('fernankikexo','092001Ss') funciono
    #IniciarTextnow()
    #CerrarNavegador()
    #print("3 listo")

    #IniciarGmail('pedroxogomezxo','092001Ss') fallos por intentos
    #IniciarTextnow()

    #pelusalola74@gmail.com
    #  092001Ss"""

    #IniciarGmail('pelusalola74','092001Ss') 
    #IniciarTextnow()
    CodeArea()
    #CerrarNavegador()
    print("3 listo")