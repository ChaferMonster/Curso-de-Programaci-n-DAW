from urllib.request import urlopen


url = urlopen("https://www.google.com/search?q=goggle&oq=goggle&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIJCAEQABgKGIAEMgkIAhAAGAoYgAQyCQgDEAAYChiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyBwgGEAAYgAQyCQgHEAAYChiABDIGCAgQRRg80gEIMjkxMGowajGoAgCwAgA&sourceid=chrome&ie=UTF-8")
with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\archivos\\Lista.txt","w") as fich:
        while 1:
            linea = str(url.readline())
            fich.write(linea)
            if linea == "":
                break
print (fich)
url.close()

print("La ruta mencionada no existe")