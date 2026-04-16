def generar_cadenas(alfabeto: list[str], max_len: int) -> list[str]:
    resultado = [""]
    for i in range(1, max_len + 1):
        nuevas = []
        for cadena in resultado:
            for simbolo in alfabeto:
                nueva_cadena = cadena + simbolo
                nuevas.append(nueva_cadena)
        resultado = resultado + nuevas
    
    # eliminar duplicados
    final = []
    for elemento in resultado:
        if elemento not in final:
            final.append(elemento)
    
    return final

def pertenece(cadena: str, lenguaje: list[str]) -> bool:
    for elemento in lenguaje:
        if elemento == cadena:
            return True
    return False

def union(l1: list[str], l2: list[str]) -> list[str]:
    resultado = l1.copy()
    for elemento in l2:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def concatenacion(l1: list[str], l2: list[str]) -> list[str]:
    resultado = []
    for x in l1:
        for y in l2:
            nueva = x + y
            resultado.append(nueva)
    return resultado

def kleene_star(l: list[str], max_iter: int) -> list[str]:
    resultado = [""]
    actual = [""]
    for i in range(1, max_iter + 1):
        nuevo = []
        for x in actual:
            for y in l:
                cadena = x + y
                nuevo.append(cadena)
        for elemento in nuevo:
            if elemento not in resultado:
                resultado.append(elemento)
        actual = nuevo
    return resultado

def kleene_plus(l: list[str], max_iter: int) -> list[str]:
    ks = kleene_star(l, max_iter)
    resultado = []
    for elemento in ks:
        if elemento != "":
            resultado.append(elemento)
    return resultado

def analizar_crecimiento(l: list[str]) -> list[dict]:
    # Retornará una lista de diccionarios para poder consumirlo en JS/Frontend
    datos = []
    for i in range(1, 6):
        resultado = kleene_star(l, i)
        # Pseudocódigo dice imprimir, nosotros retornaremos datos estructurados
        # IMPRIMIR "Iteración:", i | IMPRIMIR "Cantidad:", tamaño(resultado)
        datos.append({
            "iteracion": i,
            "cantidad": len(resultado)
        })
    return datos
