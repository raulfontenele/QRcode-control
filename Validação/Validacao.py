from mySQL import mySQL
from tratamentoEntrada import tratamentoEntrada
from checarCnpjTempo import checarCnpjTempo
import serial
import playsound as play

#controller = serial.Serial('com7',9600)
def sendCommand():
    #controller = serial.Serial('com3',9600)
    #controller.write(b'1')
    print("enviou")
    #controller.close()

def main():
    my_sql = mySQL("localhost","root","","bd_Valts","user")
    my_sql.conectarBanco()
    while(True):
        var = input("Code:")
        variaveisNota = tratamentoEntrada(var)
        
        ##Verificar se as informações de cnpj e de horário batem
        if checarCnpjTempo(variaveisNota[0],variaveisNota[2],variaveisNota[3]) and my_sql.ConsultarCondicao("Num_nota",variaveisNota[1]):
            # sendCommand()
            print("QrCode válido")
            play.playsound('volte.mp3', True)
            my_sql.Inserir(variaveisNota[2],variaveisNota[3], variaveisNota[0], variaveisNota[1], variaveisNota[4])
        else:
            play.playsound('Qr.mp3', True)
            print("QrCode inválido")

main()
