import serial
from datetime import date
import datetime

def sendCommand():
    controller = serial.Serial('com4',9600)
    controller.write(b'1')
    controller.close()

def checkTime(time):
    tolerancia = 30

    tempoAtual = datetime.datetime.now()
    tempoLeitura = datetime.datetime.strptime(time,'%d,%m,%Y,%H,%M')

    variacao = tempoAtual - tempoLeitura

    if variacao.seconds < 60*tolerancia:
        return True
    else:
        return False

def checkCode(codigo):
    #cnpj, código, (dia. mes. ano), hora, minuto
    cnpj = "010039854672584123654"

    today = date.today() 
    code = today.year*75 + today.month*63 + today.day*3
    print(code)

    ctr = False
    cods = codigo.split(";")
    if(cods[0] == cnpj):
        if int(cods[1]) == code:
            if checkTime(cods[2]):
                ctr = True

    if ctr == True:
        return True
    else:
        return False

   
def main():
    
    while(True):

        var = input("Code:")

        if checkCode(var):
            sendCommand()
            print("QrCode válido")
        else:
            print("QrCode inválido")

main()
