#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

def extracaoOnline(site):

    req = requests.get(str(site))
    lista_parametros = []

    if req.status_code == 200:
        content = req.content
        soup = BeautifulSoup(content, 'html.parser')

        ##Buscar o valor do cnpj da empresa
        table = soup.find_all(name='div', attrs={'class':'text'})

        string_pagina = str(table[0])
        
        string_pagina = string_pagina.replace("<",">")
        string_pagina = string_pagina.split('>')
        string_pagina = str(string_pagina[2]).split('\t')
        lista_parametros.append(string_pagina[-1])
        
        ##Buscar o número do cupom fiscal, a data e hora do mesmo
        
        table = soup.find_all(name='div', attrs={'id':'infos'}, recursive=True)
        string_pagina = str(table)
        string_pagina = string_pagina.replace("</strong>","<strong>")
        string_pagina = string_pagina.split("<strong>")


        lista_parametros.append(string_pagina[4])
        lista_parametros.append("".join(string_pagina[8][0:10].split("/")[::-1]))
        lista_parametros.append("".join(string_pagina[8][11:19].split(":")))

        ##Buscar o valor total do cupom fiscal

        table = soup.find_all(name='span', attrs={'class':'txtMax'})
        
        string_pagina = str(table[0])
        
        string_pagina = string_pagina.replace("<",">")
        string_pagina = string_pagina.split('>')
        lista_parametros.append(string_pagina[2].replace(",","."))

        return lista_parametros