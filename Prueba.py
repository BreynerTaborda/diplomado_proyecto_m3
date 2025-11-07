"""

"""
import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

base_url = "https://www.fincaraiz.com.co/arriendo/casas-y-apartamentos/medellin/antioquia/pagina{}?&ordenListado=3" 

info_list = []

for page in range(1, 2):
    try:
        response = requests.get(base_url.format(page), headers=headers)
        response.raise_for_status()  # Lanza un error para códigos de estado 4xx/5xx, para cuando no existen las paginas.
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
        inmubeles = soup.select("div.listingBoxCard")
    except requests.RequestException as e:
        print(f"Error al acceder a la página {page}: {e}")
        continue #Continua con la siguiente iteracion

    # Lista para almacenar la información
    for inmueble in inmubeles:
        try:
            #Precio del inmueble
            precio = inmueble.find("p", class_="main-price").get_text(strip=True)
            print(precio)
            # Tipo de inmueble acompañado de la ciudad
            tipo_inmueble = inmueble.find("a", class_="lc-data").find_all("div")[0].find("strong").get_text(strip=False)
            print(tipo_inmueble)
            #Cantidad habitaciones
            numero_habitaciones = inmueble.find("div", class_="lc-typologyTag").find_all("span", class_="lc-typologyTag__item")[0].get_text()
            print(numero_habitaciones)
            #Numero baños
            numero_banos = inmueble.find("div", class_="lc-typologyTag").find_all("span", class_="lc-typologyTag__item")[1].get_text()
            print(numero_banos)
            #Metros cuadrados
            metros_cuadrados = inmueble.find("div", class_="lc-typologyTag").find_all("span", class_="lc-typologyTag__item")[2].get_text()
            print(metros_cuadrados)
            #Barrio/Ubicación
            barrio_ubicacion = inmueble.find("h2", class_="lc-title").get_text()
            print(barrio_ubicacion)
            """info_list.append({
                "precio": precio, 
                "tipo_inmueble": tipo_inmueble,
                "numero_habitaciones": numero_habitaciones, 
            })  """
            exit()
        except Exception as e:
            print(f"Error al procesar un producto en la página {page}: {e}")
            continue #Continua con el siguiente producto
    
    #Delay de 1 segundo
    sleep_time = random.uniform(1, 3)
    time.sleep(sleep_time)  # Delay aleatorio entre 1 y 3 segundos
    print(f"Página {page} procesada con una pausa de {sleep_time:.2f} segundos.")

print(info_list)