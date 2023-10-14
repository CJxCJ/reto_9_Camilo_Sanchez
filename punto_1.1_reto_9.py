Valorprestamo = lambda C, i, n: C * (1 + (i / 100)) ** n

if __name__ == "__main__":
    C = float(input("Valor del préstamo adquirido: "))
    i = float(input("Porcentaje del interés: "))
    n = float(input("Meses a los que se sacó el préstamo: "))
    valorfinal = Valorprestamo(C, i, n)
    valorfinalimit = "{:.2f}".format(valorfinal)

    print("El valor del préstamo es " + str(valorfinalimit))
