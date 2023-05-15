# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui as pa
import random
#import ctypes para saber el tamaño de la pantalla
import ctypes


def iniciar():
    # Opciones de navegación
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    #options.add_argument("--incognito")


    options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2
    })

    driver_path = 'C:\\Users\\Administrador\\Downloads\\chromedriver.exe'

    driver = webdriver.Chrome(driver_path, chrome_options=options)
    # Delete the cookies  
    driver.delete_all_cookies()

    # Iniciarla en la pantalla 2
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    return driver



def gmail(driver, email, passworrd):
    # Inicializamos el navegador
    driver.get('https://accounts.google.com/')


    # Wait
    driver.implicitly_wait(5)
    #Escribir Email
    mail = WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')))
    mail.click()
    time.sleep(3)
    #mail.clear() 
    #time.sleep(3)                                    
    mail.send_keys(email, Keys.ENTER)

    #wmix28889@gmail.com fernankikexo@gmail.com, pelusalola74@gmail.com pedroxogomezxo, arturololoxoxo, polopepe548, dianaroja298

    time.sleep(10)

    #Escribir Contrasenia
    password = WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')))
    password.click()
    time.sleep(3)                                   
    password.send_keys(passworrd, Keys.ENTER)
    #
    time.sleep(5)
    return driver



    #Click en checkbox
    #WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-6yig3r6f6xl1'][src^='https://www.google.com/recaptcha/api2/anchor?']")))

    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()



def textnow(driver):
    # Inicializamos el navegador
    driver.get('https://textnow.com/signup')


    time.sleep(5)
    #Crear cuenta textnow
    """createAccount = WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
    #                                      '/html/body/div/div')))
    createAccount.click()"""

   # WebDriverWait(driver, 5)\
    #        .until(EC.element_to_be_clickable((By.XPATH,
     #                                       '/html/body/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div/iframe')))\
      #      .click()

    WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.ID,
                                            'google-auth-btn')))\
            .click()

    
    
    time.sleep(2)
    #mover mouse
    pa.moveTo(600,550,3)
    pa.click()      
    time.sleep(2)

    pa.moveTo(760,660,3)
    pa.doubleClick()

    time.sleep(10)

    pa.moveTo(650,580,3)
    #pa.dragTo(650, 580, duration=40,button="left")
    pa.mouseDown(650, 580,duration=30,button='left')

    time.sleep(60)

    # back to default web page frame

    driver.quit()

textnow(gmail(iniciar(),'arturololoxoxo@gmail.com','092001Ss'))
textnow(gmail(iniciar(),'pedroxogomezxo@gmail.com','092001Ss'))

 #wmix28889@gmail.com fernankikexo@gmail.com, pelusalola74@gmail.com pedroxogomezxo, arturololoxoxo, polopepe548, dianaroja298
#  092001Ss.