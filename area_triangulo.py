
def calcular_area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero.")
    return (base * altura) / 2
