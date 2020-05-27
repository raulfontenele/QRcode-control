import qrcode
import datetime
from pytz import timezone
from datetime import date
from datetime import time

import win32print
import win32ui
from PIL import Image, ImageWin

import impressao


def getTime():
    dadosHorario = datetime.datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')
    horarioFuso = dadosHorario.astimezone(fuso_horario).strftime('%Y%m%d%H%M%S')
    return horarioFuso

def getCode():

    today = date.today() 
    code = today.year*75 + today.month*63 + today.day*3
    return code

def main():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=30,
    )
    cod1 = "232003"
    cnpj = "01377961000344"
    cod2 = "59"
    nota = "000000000"
    rand = "0656103734702}"
    data = getTime()
    valor = "}0.00}}"
    rand2 = "y6n0+ip9s4YtB6m2Ko28mMl5lrVks+df8bOgZ9b+x1b8lkJ;X6d7+OsezXKencnjN1pFo12r;n;a;9Pf8TrKv58sfEOCUEAYak+ZNILWycAafPCzbuiTQZK7cFuNkQotp8m2cQa3tY4lJ9ARlOAIgjMjJ491sO9tk2g9Q9iqFan1gcKDVlfw4pPxcODean4fInLEir1G0D3fSIM9RltOYilmuwp;SQhIzctA99t4wvEzDcu0QQGiH1sy+uC;3XJDCHwMAuqdDYMBR+v3KhEMJOqJdWUozX63JDB80irlSotR+NvSSbA3c2EvvI84vz8ot2psN4EJx7v;T+obcs7ZZw=="
    qr.add_data(cod1+cnpj+cod2+nota+rand+data+valor+rand2)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("image.jpg")


main()

impressao.imprimir()