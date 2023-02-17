import sys
import hashlib

usuario= sys.argv[1]
contrasena= sys.argv[2]

f=open(".htpasswd","a")
f.write(usuario+":"+hashlib.md5(contrasena.encode('utf-8')).hexdigest()+"\n")
