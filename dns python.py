#importamos la librería os y metemos el comando de IONOS en una variable
import os
comando = 'curl -X GET https://ipv4.api.hosting.ionos.com/dns/v1/dyndns?q=ZGU0OGI5ZGE0MmJlNGNjMjg2MzlhZDI1N2E2OTUzMDAuN0w4a2lDVXkyR29WY2FvWHhzVG5nN3BoQ2VSNXhKdUlkbEQ3ZHZLZWZSWExvSC1RLXNNT1JCYW1RYjRFQ0RzZ2p2QXNHSXNnS0JDeGxIejZVRkhwT1E'
#Declaramos una variable para la IP actualizada
import urllib.request
Ip_actual = (urllib.request.urlopen('https://ident.me').read().decode('utf-8'))

#Pongo el contenido de ip.txt en Ip_antigua
Ip_antigua = open("ip.txt","r").readline(20)

#Imprimo las dos variables para ver si funcionan correctamente
print ("Ip_antigua: "+Ip_antigua)
print ("Ip_actual: "+Ip_actual)

#Si no ha cambiado: nada, y si cambia: abre ip.txt y sobreescribe la línea con la nueva ip
if Ip_antigua == Ip_actual :
	print ("Nada ha cambiado")
else :
	print ("La Ip ha cambiado")
	os.system (comando)
	open("ip.txt", "w").write(str(Ip_actual))
os.system('pause')

