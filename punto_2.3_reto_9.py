def Promedio(*args):
    if len(args) != 5:
        raise ValueError("La función Promedio requiere exactamente 5 argumentos.")
    
    prom = sum(args) / 5
    return prom

def Mediana(*args):
    if len(args) != 5:
        raise ValueError("La función Mediana requiere exactamente 5 argumentos.")
    
    medi = list(args)
    return sorted(medi)[2]

def PromedioMultiplicativo(*args):
    if len(args) != 5:
        raise ValueError("La función PromedioMultiplicativo requiere exactamente 5 argumentos.")
    
    promultiplicativo = (args[0] * args[1] * args[2] * args[3] * args[4]) ** (1/5)
    return promultiplicativo

def Ordenascendente(*args):
    if len(args) != 5:
        raise ValueError("La función Ordenascendente requiere exactamente 5 argumentos.")
    
    ascen = list(args)
    return sorted(ascen)

def Ordendescendente(*args):
    if len(args) != 5:
        raise ValueError("La función Ordendescendente requiere exactamente 5 argumentos.")
    
    descen = list(args)
    return sorted(descen, reverse=True)

def Mayor(*args):
    if len(args) != 5:
        raise ValueError("La función Mayor requiere exactamente 5 argumentos.")
    
    may = list(args)
    return max(may)

def Menor(*args):
    if len(args) != 5:
        raise ValueError("La función Menor requiere exactamente 5 argumentos.")
    
    men = list(args)
    return min(men)

def Potmayorxmenor(*args):
    if len(args) != 5:
        raise ValueError("La función Potmayorxmenor requiere exactamente 5 argumentos.")
    
    pot = list(args)
    return max(pot) ** min(pot)

def Raizcubicamenor(*args):
    if len(args) != 5:
        raise ValueError("La función Raizcubicamenor requiere exactamente 5 argumentos.")
    
    cub = list(args)
    return min(cub) ** (1/3)

if __name__ == "__main__":
    v = float(input("Valor v: "))
    w = float(input("Valor w: "))
    x = float(input("Valor x: "))
    y = float(input("Valor y: "))
    z = float(input("Valor z: "))
    
    promedio = Promedio(v, w, x, y, z)
    mediana = Mediana(v, w, x, y, z)
    promedio_multiplicativo = PromedioMultiplicativo(v, w, x, y, z)
    orden_ascendente = Ordenascendente(v, w, x, y, z)
    orden_descendente = Ordendescendente(v, w, x, y, z)
    mayor_valor = Mayor(v, w, x, y, z)
    menor_valor = Menor(v, w, x, y, z)
    potencia_mayor_x_menor = Potmayorxmenor(v, w, x, y, z)
    raiz_cubica_menor = Raizcubicamenor(v, w, x, y, z)

    print("Promedio: " + str(promedio))
    print("Mediana: " + str(mediana))
    print("Promedio Multiplicativo: " + str(promedio_multiplicativo))
    print("Orden Ascendente: " + str(orden_ascendente))
    print("Orden Descendente: " + str(orden_descendente))
    print("Mayor Valor: " + str(mayor_valor))
    print("Menor Valor: " + str(menor_valor))
    print("Potencia Mayor x Menor: " + str(potencia_mayor_x_menor))
    print("Raíz Cúbica del Menor Valor: " + str(raiz_cubica_menor))
