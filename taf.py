import time
import sys
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

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
        AgregarCarro = addButton = browser.find_element_by_id("divFijo")
        if AgregarCarro:
            ActionChains(browser).move_by_offset(1120, 544).click().perform()
            AgregarCarro = addButton = browser.find_element_by_id("divFijo").click()
            buyButton = True
            #Breakexcept = True      

    except:
        #si esto se ejecuta el boton todavia no esta abierto
        time.sleep(0.5)
        browser.refresh()
        print("Todavia no esta disponible el boton de agregar a carrito")


browser.get("https://www.taf.com.mx/checkout/#/payment")

time.sleep(1)
pyautogui.click(1432, 527)

#Iniciar Sesion Paypal
time.sleep(10)
pyautogui.click(1000, 620)

#Pagar
print("Pagando")
time.sleep(8.5)
pyautogui.click(1000, 810)

