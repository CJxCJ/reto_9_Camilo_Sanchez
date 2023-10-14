import math

def Volumenesfera(*args):
    if len(args) != 1:
        raise ValueError("error intente de nuevo")
    
    r1 = args[0]
    volesfera = (4/3) * math.pi * (r1 ** 3)
    return volesfera

def Areaesfera(*args):
    if len(args) != 1:
        raise ValueError("error intente de nuevo")
    
    r1 = args[0]
    aresfera = 4 * math.pi * (r1 ** 2)
    return aresfera

def Volumencono(*args):
    if len(args) != 2:
        raise ValueError("error intente de nuevo")
    
    r2, h = args
    volcono = (math.pi * (r2 ** 2) * h) / 3
    return volcono

def Areacono(*args):
    if len(args) != 2:
        raise ValueError("error intente de nuevo")
    
    r2, h = args
    arcono = (math.pi * r2) * (math.sqrt(h ** 2 + r2 ** 2)) + math.pi * (r2 ** 2)
    return arcono

def Volumentotal(*args):
    if len(args) != 3:
        raise ValueError("error intente de nuevo")
    
    r1, r2, h = args
    voltotal = ((4/3) * math.pi * (r1 ** 3)) + ((math.pi * (r2 ** 2) * h) / 3)
    return voltotal

def Areatotal(*args):
    if len(args) != 3:
        raise ValueError("error intente de nuevo")
    
    r1, r2, h = args
    artotal = ((math.pi * r2) * (math.sqrt(h ** 2 + r2 ** 2)) + math.pi * (r2 ** 2)) + 4 * math.pi * (r1 ** 2)
    return artotal

if __name__ == "__main__":
    r1 = float(input("Radio de la esfera: "))
    r2 = float(input("Radio del cono: "))
    h = float(input("Altura del cono: "))
    volumenE = Volumenesfera(r1)
    areaE = Areaesfera(r1)
    volumenC = Volumencono(r2, h)
    areaC = Areacono(r2, h)
    volumenT = Volumentotal(r1, r2, h)
    areaT = Areatotal(r1, r2, h)

    print("El volumen de la esfera es: " + str(volumenE))
    print("El área de la esfera es: " + str(areaE))
    print("El volumen del cono es: " + str(volumenC))
    print("El área del cono es: " + str(areaC))
    print("El volumen del cono y la esfera juntos es: " + str(volumenT))
    print("El área del cono y la esfera juntos es: " + str(areaT))
