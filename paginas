import requests
from bs4 import BeautifulSoup
import os

url_pagina = 'https://www.wallpaperflare.com/justice-logo-metallica-album-covers-heavy-metal-thrash-metal-wallpaper-spoki'

try:
    respuesta = requests.get(url_pagina)
    respuesta.raise_for_status()  

    soup = BeautifulSoup(respuesta.text, 'html.parser')

    # Encuentra todos los elementos img en el HTML
    imagenes = soup.find_all('img')

    # Carpeta donde quieres guardar las imágenes
    carpeta_destino = "imagenes_descargadas"
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    for i, img in enumerate(imagenes):  
        # Intenta extraer la URL de la imagen de diferentes atributos
        src = img.get('src') or img.get('data-src')
        if not src:
            # Si no se encuentra una URL de imagen, continúa con la siguiente
            continue
        # Asume que las URLs que no comienzan con http son relativas
        if not src.startswith('http'):
            src = f"{url_pagina}/{src}"
        
        # Obtén la imagen
        try:
            img_respuesta = requests.get(src)
            img_respuesta.raise_for_status()

            # Define un nombre de archivo basado en el índice de la imagen
            nombre_archivo = os.path.join(carpeta_destino, f'imagen_{i}.jpg')

            # Guarda la imagen
            with open(nombre_archivo, 'wb') as f:
                for chunk in img_respuesta.iter_content(1000):
                    f.write(chunk)
            print(f"Descargada {src} en {nombre_archivo}")
        except requests.exceptions.RequestException as e:
            print(f"No se pudo descargar {src}: {e}")
except requests.exceptions.RequestException as exc:
    print('Hubo un problema al obtener la página: %s' % (exc))
