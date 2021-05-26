import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#si
#variables input
print("Ingresa la URL del articulo para usar el bot")
URL = input()
print("Selecciona metodo de pago escribiendo: P o T (Paypal o tarjeta)")
Metodo = input()
if Metodo == "P":
    print("Ingresa tu correo electronico de paypal")
    Paypalcorreo = input()
    print ("Ingresa tu contrasena de paypal")
    Paypalcontra = input()
elif Metodo == "T":
    print ("Ingresa el nombre del titular de la tarjeta (Nombre)")
    TarjetaNombre = input()
    print ("Ingresa el nombre del titular de la tarjeta (Apellido)")
    TarjetaApellido = input()
    print("Ingresa el numero de tu tarjeta")
    TarjetaId = input()
    print ("Ingresa la fecha de caducidad (Mes)")
    Tarjetames = input()
    print ("Ingresa la fecha de caducidad (Ano)")
    Tarjetaano = input()
    print ("Ingresa los tres digitos de tu tarjeta")
    TarjetaCVV = input()
else:
    print("No ingresaste T o P")
    time.sleep(0.5)
    print("Cerrando el programa")
    sys.exit()

#Cuenta de la pagina
Cuenta = "acevedopico@hotmail.com"
Password = "Agapa90190"
LoginPagina = False

#Web URL
option = webdriver.ChromeOptions()

#Quitar flag en Chrome
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')

#Direccion en memoria de Chromedriver
browser = webdriver.Chrome(r'C:\Users\bolan\OneDrive\Documentos\chromedriver.exe', options=option)

#Entrar al URL
if URL:
    browser.get("{}".format(URL))
else:
    print("No se ingreso URL, cerrando el programa")
    sys.exit()

#Iniciar sesion
print("Inicia sesion e ingresa a la pagina del articulo, ingresa SI para activar el BOT, NO para salir del programa")
Sesion = input()

#Algoritmo
if Sesion == "SI":
    buyButton = False

    if not LoginPagina:
        
    #Checar disponibilidad y agregar al carrito
        while not buyButton:
            try:
                #Si esto se ejecuta es que todavia no esta abierto el boton
                Carritodisp = addButton = browser.find_element_by_class_name("btn-disabled")

                #El boton de compra no esta listo
                print("Todavia no esta disponible el boton de agregar a carrito")

                #Refreshear pagina
                time.sleep(1)
                browser.refresh()
    
            except:
                Carritodisp = addButton = browser.find_element_by_class_name("btn--full").click()
                print("El boton de agregar al carrito fue presionado")
                buyButton = True
    
        #Finalizar compra
        #time.sleep(1)
        #Close = addButton = browser.find_element_by_class_name("privy-x").click()
        FinalizarCompra = addButton = browser.find_element_by_class_name("cart__checkout").click()
        Envio = addButton = browser.find_element_by_class_name("btn").click()
        ContinuarPago = addButton = browser.find_element_by_class_name("btn").click()
        if (Metodo == "P"):
            Paypal = addButton = browser.find_element_by_id('checkout_payment_gateway_9942630443').click()
        elif (Metodo == "T"):
            Tarjeta = addButton = browser.find_element_by_id('checkout_payment_gateway_18405425195').click()
        else:
            print("Metodo de pago seleccionado incorrecto")
            time.sleep(1)
            print("Saliendo del programa")
            browser.quit()
            sys.exit()
        Final = addButton = browser.find_element_by_id('continue_button').click()

        #Llenar datos de pago
        if (Metodo == "P"):
            #Llenar datos login
            UserP = addButton = browser.find_element_by_id('email')
            UserP.clear()
            UserP.send_keys(Paypalcorreo)
            ContraP = addButton = browser.find_element_by_id('password')
            ContraP.clear()
            ContraP.send_keys(Paypalcorreo)
            LoginPaypal = addButton = browser.find_element_by_id('btnLogin').click()
        elif (Metodo == "T"):
            #Llenar datos tarjeta
            time.sleep(1.2)
            IdTar = addButton = browser.find_element_by_id('credit-card-inline')
            IdTar.send_keys(TarjetaId)
            NombreTar = addButton = browser.find_element_by_id('first-name')
            NombreTar.send_keys(TarjetaNombre)
            ApellidoTar = addButton = browser.find_element_by_id('last-name')
            ApellidoTar.send_keys(TarjetaApellido)
            ComprarTar = addButton = browser.find_element_by_id('continueButton').click()
        else:
            print("Error en datos de pago ingresados")
            time.sleep(0.5)
            print("Ingresalos manualmente, o reinicia el programa")
        
else:
    print("Saliendo del programa")
    browser.quit()
    sys.exit()