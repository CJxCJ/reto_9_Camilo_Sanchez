Compra = lambda P, M, H, PAN = float(300), LECHE = float(3300), HUEVOS = float(350) : PAN * P + LECHE * M + HUEVOS * H

if __name__ == "__main__":
    P = float(input("Cantidad de panes: "))
    M = float(input("Cantidad de bolsas de leche: "))
    H = float(input("Cantidad de huevos: "))
    B = float(input("Valor del billete con el que se paga: "))

    total = Compra(P, M, H)

    vueltas = lambda B, total: B - total

    deuda = vueltas(B, total)

    if deuda > 0:
        print("Sus vueltas son " + str(deuda) + " COP")
    elif deuda < 0:
        print("Quedó debiendo " + str(abs(deuda)) + " COP")
    else:
        print("El pago fue exacto")
