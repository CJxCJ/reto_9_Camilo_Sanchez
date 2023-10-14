Carnetotal = lambda N, M, K, GALLINAS = float(6), GALLOS = float(7), POLLITOS = float(1) : GALLINAS * N + GALLOS * M + POLLITOS * K

if __name__ == "__main__":
    N = float(input("Cantidad de gallinas: "))
    M = float(input("Cantidad de gallos: "))
    K = float(input("Cantidad de pollos: "))
    pesototal = Carnetotal(N, M, K)

    print("El peso total de las carnes es: " + str(pesototal) + " KG")

