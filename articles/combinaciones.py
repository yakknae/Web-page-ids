import string

caracteres = string.ascii_letters + string.digits
caracter_especial = "_" + caracteres

# Usar un conjunto para evitar duplicados
combinaciones_unicas = set()

with open ("combinaciones.txt",'w') as archivo:
    for c1 in caracter_especial:
        for c2 in caracteres:
            for c3 in caracteres:
                combinaciones = f"{c1}{c2}{c3}".lower()
                if combinaciones not in combinaciones_unicas:
                    combinaciones_unicas.add(combinaciones)
                    archivo.write(combinaciones + "\n")