from datetime import date
import datetime

def checarCnpjTempo(cnpj_nota,data,hora):

    cnpj_list = ["27518561000214","46.241.741/0001-65"]#adicione aqui o novo CNPJ

    ctr = False

    for cnpj in cnpj_list:
        if(cnpj_nota == cnpj):
            if checkTime(str(data) + str(hora)):
                ctr = True

    if ctr == True:
        return True
    else:
        return False

def checkTime(time):
    tolerancia = 30

    tempoAtual = datetime.datetime.now()
    print(time)
    tempoLeitura = datetime.datetime.strptime(time,'%Y%m%d%H%M%S')

    variacao = tempoAtual - tempoLeitura

    if variacao.seconds < 60*tolerancia:
        return True
    else:
        return False