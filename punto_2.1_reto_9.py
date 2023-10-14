def Contagios(*args):
    if len(args) != 2:
        raise ValueError("La función Contagios requiere exactamente 2 argumentos.")
    
    C, D = args
    nuevosContagios = C * (2 ** (D - 1))
    return nuevosContagios

if __name__ == "__main__":
    C = float(input("Numero de contagiados actuales: "))
    D = float(input("Dias transcurridos: "))
    contagiosfinal = Contagios(C, D)

    print("El número de contagiados en " + str(D) + " días es de " + str(contagiosfinal))
