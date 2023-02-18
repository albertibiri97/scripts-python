#Importamos las librerías necesarias, algunas se tienen que instalar con pip
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import sys
import csv
import os

#Si no tiene el argumento del enlace de youtube mostrará un error y saldrá

if len(sys.argv) < 2:
    print ('Debes indicar la url del canal')
    sys.exit()

#Declaro la clave de google developer
DEVELOPER_KEY = "AIzaSbSjj3FbVAfVUEvYPTKNjo"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Paso el argumento (enlace) para que solo coja el id del canal con split
cadena= sys.argv[1]
channel_id = cadena.split("/")[-1]

# funcion que devuelve la lista de videos del canal. youtube es un argumento que indica a la api la aplicación sobre la que trabajar
#**kwargs es un diccionario de elementos típicos sobre los que trabajar con youtube
#part='id,snippet' indica que devuelva el id del video y snippet devuelve información relevante sobre este
def get_video_list(youtube, **kwargs):
    videos = []
    search_response = youtube.search().list(
        channelId=channel_id,
        type='video',
        part='id,snippet',
        maxResults=80,  # maximum number of results to retrieve
        **kwargs
    ).execute()

#Sobre la búsqueda realizada cojemos el título, el id para poner el enlace y con videos.append se añade la url y el título en el array videos
    for search_result in search_response.get("items", []):
        title = search_result["snippet"]["title"]
        video_id = search_result["id"]["videoId"]
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        videos.append((video_url, title))
#Devuelve el array
    return videos

# Creamos un objeto con la api de youtube indicando la clave
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# Llamamos a la función y vamos metiendo el array en el archivo lista.txt
videos = get_video_list(youtube)
with open('lista.txt','a') as f:
    print(json.dump(videos, f))

# Abrir el archivo original y leer su contenido. Añadimos el encoding y errors por si hay caracteres raros como emojis, para traducirlos por ?
with open("lista.txt", "r", encoding="utf-8-sig", errors="replace") as f:
    contenido = eval(f.read())

# Abrir un nuevo archivo CSV en modo escritura
with open("lista.csv", "a",newline="", encoding="utf-8-sig", errors="replace") as f:
    writer = csv.writer(f)

    # Escribir cada fila del archivo original en el archivo CSV
    for fila in contenido:
        writer.writerow(fila)

#añado unos saltos de línea para poder distinguir cada búsqueda
with open("lista.csv", "a") as f:
    f.write("\n \n \n")

#elimino el archivo lista.txt para tener solo el csv
os.system ('rm -r lista.txt')
