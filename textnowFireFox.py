# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import pyautogui as pa
import random
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager




#import ctypes para saber el tamaño de la pantalla
import ctypes


# Opciones de navegación
#options = Options()


#options.add_experimental_option("prefs", { \
 #   "profile.default_content_setting_values.notifications": 2
#})



driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Iniciarla en la pantalla 2

# Inicializamos el navegador
driver.get('https://accounts.google.com/')



#Escribir Email
mail = WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')))
mail.click()
time.sleep(3)
#mail.clear() 
#time.sleep(3)                                    
mail.send_keys('pedroxogomezxo@gmail.com', Keys.ENTER)

#wmix28889@gmail.com fernankikexo@gmail.com, pelusalola74@gmail.com pedroxogomezxo, arturololoxoxo, polopepe548, dianaroja298

time.sleep(10)

#Escribir Contrasenia
password = WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')))
password.click()
time.sleep(3)                                   
password.send_keys('092001Ss', Keys.ENTER)
#
time.sleep(5)




#Click en checkbox
#WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-6yig3r6f6xl1'][src^='https://www.google.com/recaptcha/api2/anchor?']")))

#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()




# Inicializamos el navegador
driver.get('https://textnow.com/signup')


time.sleep(5)
#Crear cuenta textnow
"""createAccount = WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
#                                      '/html/body/div/div')))
createAccount.click()"""

WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div/iframe')))\
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
pa.dragTo(650, 580, duration=30,button="left")

time.sleep(20)

# back to default web page frame

driver.quit()

