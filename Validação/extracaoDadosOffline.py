def extracaoOffline(code):
    if code.find("}")  == -1:
        cods = code.split("{")
    else:
        cods = code.split("}")

    # codUF_qrcode =  cods[0][0:5]
    cnpj_qrcode = cods[0][6:20]
    nnota_qrcode = cods[0][22:31]
    data = cods[1][0:8]
    hora = cods[1][8:14]
    valor_compra = cods[2]

    return [cnpj_qrcode,nnota_qrcode,data,hora,valor_compra]
