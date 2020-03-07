## pip install qrcode[pil]
## pip install pytz
import qrcode
import datetime
from pytz import timezone


def getTime():
    dadosHorario = datetime.datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')
    horarioFuso = dadosHorario.astimezone(fuso_horario).strftime('%d.%m.%Y;%H:%M')
    #data_e_hora_sao_paulo_em_texto = horarioFuso.
    return horarioFuso


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
cnpj = "010039854672584123654;"
qr.add_data(cnpj + getTime())
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("image.jpg")

