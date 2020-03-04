import re
import datetime

def esFecha(expFecha):
    # Extrae el año, mes y día del valor proporcionado
    try:
        anio=expFecha[0:4]
        mes=expFecha[5:7]
        dia=expFecha[-2:]
        datetime.date(int(anio),int(mes),int(dia))
    except ValueError :
        return False
    
    return True

def strtodate(expFecha):
    anio=expFecha[0:4]
    mes=expFecha[5:7]
    dia=expFecha[-2:]
    return datetime.date(int(anio), int(mes), int(dia))

def main():

    colegiatura=5600.00

    _fechapago=""
    fechacomprimiso=strtodate("2020/02/15")
    fechapago=fechacomprimiso
    while True:
        _fechapago=input("Cuándo hiciste el pago YYYY/MM/DD: ")
        if re.search("^[0-9]{4}/[0-9]{2}/[0-9]{2}$", _fechapago):
            if esFecha(_fechapago):
                fechapago=strtodate(_fechapago)
                break
            else:
                print("No es una fecha.")
        else:
            print("El formato no es YYYY/MM/DD")

    cargodiario=8.00
    diferencia=fechapago-fechacomprimiso
    pagofinal=0.00
    if diferencia.days>0:
        pagofinal=colegiatura+(diferencia.days*cargodiario)
    else:
        pagofinal=colegiatura

    print(pagofinal)