from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import sys
import csv
import os

# Set DEVELOPER_KEY to the API key value from the Google Cloud Console
# Set YOUTUBE_API_SERVICE_NAME and YOUTUBE_API_VERSION to the API service name and version
# that you are using

if len(sys.argv) < 2:
    print ('Debes indicar la url del canal')
    sys.exit()

DEVELOPER_KEY = "AIzaSyDRKJT0IdWsLrbSjj3FbVAfVUEvYPTKNjo"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Set the channel ID for the channel you want to retrieve videos from
cadena= sys.argv[1]
channel_id = cadena.split("/")[-1]

# Define a function to retrieve the list of videos from the channel
def get_video_list(youtube, **kwargs):
    videos = []
    search_response = youtube.search().list(
        channelId=channel_id,
        type='video',
        part='id,snippet',
        maxResults=80,  # maximum number of results to retrieve
        **kwargs
    ).execute()

    for search_result in search_response.get("items", []):
        title = search_result["snippet"]["title"]
        video_id = search_result["id"]["videoId"]
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        videos.append((video_url, title))

    return videos

# Set up the API client with your API key and create a YouTube object
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# Call the function to get the list of videos and print them
videos = get_video_list(youtube)
with open('lista.txt','a') as f:
    print(json.dump(videos, f))

# Abrir el archivo original y leer su contenido
with open("lista.txt", "r", encoding="utf-8-sig", errors="replace") as f:
    contenido = eval(f.read())

# Abrir un nuevo archivo CSV en modo escritura
with open("lista.csv", "a",newline="", encoding="utf-8-sig", errors="replace") as f:
    writer = csv.writer(f)

    # Escribir cada fila del archivo original en el archivo CSV
    for fila in contenido:
        writer.writerow(fila)

with open("lista.csv", "a") as f:
    f.write("\n \n \n")

os.system ('rm -r lista.txt')

