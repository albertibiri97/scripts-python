#Script propiedad de Alberto Moreno Cordón

import os

from datetime import datetime

import ftplib

import tarfile

import logging





# Obtener la fecha actual

fecha = datetime.now()

fechaestringeada = fecha.strftime("%Y%m%d")



# Comprimir directorio public_html

nombre_archivo = "backup"+fechaestringeada+".tar.gz"

comprimir = tarfile.open(nombre_archivo, "w:gz")

comprimir.add("/home/usuario/apache")

comprimir.close()



# Conectarse al servidor FTP

ftp = ftplib.FTP()

ftp.connect("192.168.1.128",21)

ftp.sendcmd('USER alberto_virtual')

ftp.sendcmd('PASS usuario')

# Subir archivo comprimido al servidor

archivoasubir = open(nombre_archivo, "rb")

ftp.storbinary("STOR " + nombre_archivo, archivoasubir)

archivoasubir.close()





# Eliminar archivo local

os.remove(nombre_archivo)



# Borrar la copia de seguridad más antigua si hay más de 10 en el servidor

lista_archivos = ftp.nlst()

lista_archivos.sort()

if len(lista_archivos) > 10:

    ftp.delete(lista_archivos[0])

ftp.quit()





from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import smtplib #importar el modulo de protocolos de correo

sender='alberto@amcred.es' #Dirección del remitente

receiver='alberto@amcred.es' #Dirección del destinatario

password='Contraseña' #Contraseña de la cuenta del remitente

#Detalles de conexión al servidor de correo

smtp_server=smtplib.SMTP("smtp.ionos.es",587)

smtp_server.ehlo() #Iniciando la conexión por IMAP

smtp_server.starttls() #Configurando la conexión con encriptación TLS

smtp_server.ehlo() #Iniciando de nuevo la conexión con encriptación TLS

smtp_server.login(sender,password) #Logeándose en el servidor de correo

#Mensaje que se enviará

mensaje ='''

La copia de seguridad de la web se ha realizado correctamente

'''

#Añadiendo contenido en cabeceras de Asunto, remitente y destinatario

mensajeconcabeceras = MIMEMultipart()

mensajeconcabeceras["Subject"] = "Copia seguridad OK"

mensajeconcabeceras["From"] = sender

mensajeconcabeceras["To"] = receiver

mensajeconcabeceras.attach(MIMEText(mensaje))





#Enviar el correo

smtp_server.sendmail(sender,receiver,mensajeconcabeceras.as_string())

smtp_server.quit()#Cerrando el servicio de correo


