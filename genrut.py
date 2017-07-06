def crear(t, nametxt):
    rute = open(nametxt + ".txt", "a")
    rute.write(t + "\n")
    rute.close()


def generarut(desde, hasta):

    arreglo = []

    for i in range(desde, hasta):
        total = 0
        multiplo = 2
        rut = str(i)
        for rinverso in reversed(rut):
            total += int(rinverso) * multiplo

            if multiplo == 7:
                multiplo = 2
            else:
                multiplo += 1

            modulus = total % 11
            verificador = 11 - modulus

            if verificador == 10:
                div = "k"
            elif verificador == 11:
                div = "0"
            elif verificador < 10:
                div = verificador

        arreglo.append(rut + str(div))

    return arreglo

if "__main__" == __name__:

    desde = input("ingresa rut inicial ej:12345678 =>> ")
    hasta = input("ingresa rut final")
    nametxt = raw_input("ingresa nombre para archivo txt")

    for runs in generarut(desde, hasta):
        print (runs)
        crear(runs, nametxt)
