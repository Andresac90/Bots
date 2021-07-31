import time
import sys
import pyautogui
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#Ingresar URL
print("Ingresa la URL del articulo para usar el bot")
URL = input()

#Inicializar webdriver
option = Options()

#Profile en Chrome
#option.add_argument(r"--user-data-dir=C:\Users\aceve\AppData\Local\Google\Chrome\User Data") #Andres
#option.add_argument(r'--profile-directory=Default') #Andres
option.add_argument(r"--user-data-dir=C:\Users\bolan\AppData\Local\Google\Chrome\User Data") #David
option.add_argument(r'--profile-directory=Profile 4') #David

#Quitar flag en Chrome
option.add_experimental_option("detach", True)
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')

#Direccion en memoria de Chromedriver
#browser = webdriver.Chrome(r'C:\Users\aceve\OneDrive\Documents\ProjectDavid\chromedriver', options=option) #Andres
browser = webdriver.Chrome(r'C:\Users\bolan\OneDrive\Documentos\chromedriver.exe', options=option) #David

#Ir al URL Seleccionado
browser.get("{}".format(URL))

#Comenzar Algoritmo
print("Iniciando bot")
buyButton = False
        
#Checar disponibilidad y agregar al carrito
while not buyButton:
    try:
        #Si esto se ejecuta el boton esta abierto
        AgregarCarro = addButton = browser.find_element_by_class_name("btn--full")
        if AgregarCarro:
            browser.find_element_by_class_name("btn--full").click()
            buyButton = True
            #Breakexcept = True      

    except:
        #si esto se ejecuta el boton todavia no esta abierto
        time.sleep(1)
        browser.refresh()
        print("Todavia no esta disponible el boton de agregar a carrito")

#Checkout
browser.find_element_by_name("checkout").click()
time.sleep(1.5)
#Ir a Paypal
browser.find_element_by_id('continue_button').click()

#Iniciar Sesion Paypal
#time.sleep(2)
pyautogui.click(1000, 620)

#Pagar
print("Pagando")
time.sleep(7)
pyautogui.click(1000, 910)
