from extracaoDadosOffline import extracaoOffline
from extracaoDadosOnline import extracaoOnline 

def tratamentoEntrada(code):
   
    ##Verificar se é on-line ou off-line

    if code[0:5] == "https":
        retorno = extracaoOnline(code)
        return retorno
    else:
        retorno = extracaoOffline(code)
        return retorno
