#Ejercicio 1
def digitos(numero_de_tarjeta: str) -> int:
    return len(numero_de_tarjeta)

#Ejercicio 2
def obtener_prefijo(numero_de_tarjeta: str, tamaño_prefijo: int) -> int:
    prefijo = int(numero_de_tarjeta[:tamaño_prefijo])
    return prefijo

#Ejercicio 3
def tipo_tarjeta(numero_de_tarjeta: str) -> str:
    longitud_tarjeta = digitos(numero_de_tarjeta)
    prefijo = obtener_prefijo(numero_de_tarjeta, 2)

    if prefijo == 34 or prefijo == 37:
        if longitud_tarjeta == 15:
            return 'American Express'
    elif prefijo >= 51 and prefijo <= 55:
        if longitud_tarjeta == 16:
            return 'Mastercard'
    elif int(str(prefijo)[0]) == 4:
        if longitud_tarjeta == 13 or longitud_tarjeta == 16:
            return 'Visa'

    return 'Invalid'

#Ejercicio 4
def digitos_impares(numero_de_tarjeta: str) -> list[int]:
    digitos = [int(numero_de_tarjeta[i]) for i in range(len(numero_de_tarjeta)-1, -1, -2)]
    return digitos


#Ejercicio 5
def digitos_pares(numero_de_tarjeta: str) -> list[int]:
    digitos = [int(numero_de_tarjeta[i]) for i in range(len(numero_de_tarjeta)-2, -1, -2)]
    return digitos


#Ejercicio 6
def sumar_digitos(lista_digitos: list[int]) -> int:
    suma = 0
    for numero in lista_digitos:
        for digito in str(numero):
            suma += int(digito)
    return suma


#Ejercicio 7
def luhn(numero_de_tarjeta: str) -> bool:
    lista_digitos_pares = digitos_pares(numero_de_tarjeta)
    lista_digitos_impares = digitos_impares(numero_de_tarjeta)
    
    lista_digitos_pares_multiplicados = []
    
    suma_digitos_pares = 0
    suma_digitos_impares = 0
    
    for numero in lista_digitos_pares:
        lista_digitos_pares_multiplicados.append(str(numero*2))
    
    for numero in lista_digitos_pares_multiplicados:
        for letra in numero:
            suma_digitos_pares += int(letra)

    for numero in lista_digitos_impares:
        suma_digitos_impares += numero

    total = suma_digitos_impares + suma_digitos_pares

    return total % 10 == 0

#Ejercicio 8
def validar_tarjeta(numero_de_tarjeta : str) -> bool:
    str_tipo_tarjeta = tipo_tarjeta(numero_de_tarjeta)
    pasoLuhn = luhn(numero_de_tarjeta)

    return str_tipo_tarjeta != "Invalid" and pasoLuhn
