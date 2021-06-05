import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#Ingresar URL
print("Ingresa la URL del articulo para usar el bot")
URL = input()

#Inicializar webdriver
option = Options()

#Profile en Chrome
option.add_argument(r"--user-data-dir=C:\Users\aceve\AppData\Local\Google\Chrome\User Data") #Andres
option.add_argument(r'--profile-directory=Default') #Andres
#option.add_argument(r"--user-data-dir=C:\Users\aceve\AppData\Local\Google\Chrome\User Data") #David
#option.add_argument(r'--profile-directory=Default') #David

#Quitar flag en Chrome
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')

#Direccion en memoria de Chromedriver
browser = webdriver.Chrome(r'C:\Users\aceve\OneDrive\Documents\ProjectDavid\chromedriver', options=option) #Andres
#browser = webdriver.Chrome(r'C:\Users\bolan\OneDrive\Documentos\chromedriver.exe', options=option) #David

#/////////////////////////CODIGOUSOEMERGENCIAINICIO/////////////////////////

#Entrar al URL
#if URL:
  #  browser.get("https://www.lustmexico.com/account/login?return_url=%2Faccount")

#No se ingreso un url
#else:
    #print("No se ingreso URL, cerrando el programa")
   # sys.exit()

#Variables
#Ingresar metodo de pago
# print("Selecciona metodo de pago escribiendo: P o T (Paypal o tarjeta)")
# Metodo = input()

# #Datos en Paypal
# if Metodo == "P":
#     #Correo en Paypal
#     Paypalcorreo = "acevedopico@hotmail.com"

#     #Contraseña en Paypal
#     Paypalcontra = "Agapa90190"

# #Datos en Tarjeta
# elif Metodo == "T":
#     #Nombre del titular en la tarjeta
#     TarjetaNombre = "Mario Andres"
    
#     #Apellido del titular en la tarjeta
#     TarjetaApellido = "Acevedo Pico"

#     #Numero de la tarjeta (16 digitos)
#     TarjetaId = "4561237894561234"

#     #Mes de caducidad de la tarjeta
#     Tarjetames = "02"

#     #Año de caducidad de la tarjeta
#     Tarjetaano = "2025"

#     #Tres digitos de tarjeta
#     TarjetaCVV = "123"

# #No se selecciono metodo de pago
# else:
#     print("No ingresaste T o P")
#     time.sleep(0.5)
#     print("Cerrando el programa")
#     sys.exit()

#///////////////////Hasta aqui tienes que llenar datos///////////////////

#Login
# print("Inicia Sesion en la pagina")
# print("Presiona enter cuando estes logeado")
# input()

#/////////////////////////CODIGOUSOEMERGENCIAEND/////////////////////////

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
#browser.find_element_by_class_name("cart__checkout").click()

#Comando Javascript
browser.get("https://www.lustmexico.com/26365824/checkouts/1f9980146c0114fca9f170ca93d95bd3?previous_step=shipping_method&step=payment_method")

# if (Metodo == "P"):
#     browser.find_element_by_id('checkout_payment_gateway_9942630443').click()
# elif (Metodo == "T"):
#     browser.find_element_by_id('checkout_payment_gateway_18405425195').click()
# else:
#     print("Metodo de pago seleccionado incorrecto")
#     time.sleep(1)
#     print("Saliendo del programa")
#     browser.quit()
#     sys.exit()

#Ir a Paypal
browser.find_element_by_id('continue_button').click()

#Pagar Paypal
time.sleep(10)
print("Pagando")
botonp = addButton = browser.find_element_by_id("payment-submit-btn")

#Pagar con dos opciones

#Paypal
#if (Metodo == "P"): 

#Tarjeta
# elif (Metodo == "T"):
#     #Llenar datos tarjeta
#     time.sleep(1.2)
#     IdTar = addButton = browser.find_element_by_id('credit-card-inline')
#     IdTar.send_keys(TarjetaId)
#     NombreTar = addButton = browser.find_element_by_id('first-name')
#     NombreTar.send_keys(TarjetaNombre)
#     ApellidoTar = addButton = browser.find_element_by_id('last-name')
#     ApellidoTar.send_keys(TarjetaApellido)
#     ComprarTar = addButton = browser.find_element_by_id('continueButton').click()
# else:
#     print("Error en datos de pago ingresados")
#     time.sleep(0.5)
#     print("Ingresalos manualmente, o reinicia el programa")