## pip install qrcode[pil]
## pip install pytz
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
    horarioFuso = dadosHorario.astimezone(fuso_horario).strftime('%d,%m,%Y,%H,%M')
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
    codigo = str(getCode()) + ";"
    cnpj = "010039854672584123654;"
    qr.add_data(cnpj +codigo+ getTime())
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("image.jpg")


main()

impressao.imprimir()