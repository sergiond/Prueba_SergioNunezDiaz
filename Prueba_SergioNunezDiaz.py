#Sergio Núñez Díaz
#/etc/rc.d/init.d/crond start

import os, sys
import subprocess
import signal
from email.mime.text import MIMEText
import smtplib
import datetime
 


#EJERCICIO 1

class Programa(): #Creamos la clase Programa
    def __init__(self, nombre, script, ruta, nejecutable): #Definimos los atributos del objeto
        self.nombre = nombre 
        self.script = script
        self.ruta = ruta
        self.nejecutable = nejecutable

Prog = Programa("crond", "/etc/init.d/crond", "/var/run/crond.pid" ,"crond") #Instancia ejemplo
print(Prog.nombre + " | " + Prog.script + " | " + Prog.ruta + " | " +Prog.nejecutable )

#comprueba si el proceso se ejecuta y escribe en el fichero , el argumento corresponde con el nombre
def comprobarApp(arg):
    proceso = subprocess.Popen(["systemctl", "start", arg], stdout=subprocess.PIPE)
    while True:
        salida = proceso.stdout.readline()
        if salida == '' and process.poll() is not None:
            with open('/temp/informe.txt','a') as outFile:
                outFile.write(arg +'\n'+ "activo" +'\n' + str(datetime.datetime.now()))
        if salida:
            with open('/temp/informe.txt','a') as outFile:
                outFile.write(arg +'\n'+ "inactivo" +'\n' + str(datetime.datetime.now()))
            break
    rc = process.poll()
    return rc

### EJERCICIO 2
#Iniciar proceso
def InitApp (arg,estado):
    try:
        if estado == None:
            print("en ejecución")
    except :
        subprocess.run(["systemctl", "start", arg],shell=True)
#Finalizar proceso utilizando systemctl, en caso de que no finalice se lanzan las señales
def FinApp(arg,estado):
    try:
        if estado == None:
            subprocess.run(["systemctl", "stop", arg],shell=True)
            outs, errs = p1.communicate(timeout=10)
    except subprocess.TimeoutExpired as e:
        os.kill(arg, 15)
        time.sleep(5) 
    except:
        os.kill(arg, 9)
#Reinicio de proceso
def ResApp(arg):
    try:
        if estado == None:
            print("en ejecución")
            sys.exit()
    except :
        subprocess.run(["systemctl", "restart", arg,],shell=True)

#en este caso uso Popen() en vez de Run() para devolver none en caso afirmativo de proceso en ejecución
def EstatusApp(arg):
    try:
        process = subprocess.Popen(arg) 
        return process.poll()
    except: 
        print("Proceso no ejecutado")

#Ejercicio 3
#enviar informe solicitando la direción de correo electrónico

def EnviarInforme():

    ruta = "/temp/informe.txt"

    with open(ruta, 'rb') as fo:
        contenido = fo.read()

    remitente = "support@dinahosting.com"
    destinatario = input("indica Email de destino")
    message = "Hello, world!"
    
    mime_message = MIMEText(message, "plain")
    mime_message["From"] = remitente
    mime_message["To"] = destinatario
    mime_message["Subject"] = "Informe"
    
    smtp = SMTP("smtp.dinahosting.com")
    smtp.login(remitente, "clave")
    
    smtp.sendmail(remitente, destinatario, contenido)
    smtp.quit()
