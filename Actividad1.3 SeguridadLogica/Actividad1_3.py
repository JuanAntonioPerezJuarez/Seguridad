def capa_1(entrada):
    # Lógica de la primera capa de seguridad
    return entrada[::-1]  # Invertir la entrada

def capa_2(entrada):
    # Lógica de la segunda capa de seguridad
    return "".join([chr(ord(char) + 1) for char in entrada])  # Desplazar los caracteres un paso hacia adelante en el código ASCII

def capa_3(entrada):
    # Lógica de la tercera capa de seguridad
    return entrada.replace("a", "b").replace("e", "f").replace("i", "j").replace("o", "p").replace("u", "v")  # Reemplazar vocales por la siguiente en el alfabeto

def capa_4(entrada):
    # Lógica de la cuarta capa de seguridad
    return entrada + "xYz"  # Agregar una cadena al final

# Función principal que aplica todas las capas de seguridad
def seguridad_logica(entrada):
    resultado = capa_1(entrada)
    resultado = capa_2(resultado)
    resultado = capa_3(resultado)
    resultado = capa_4(resultado)
    return resultado

# Ejemplo de uso
entrada = "HolaMundo"
resultado_seguro = seguridad_logica(entrada)
print("Entrada original:", entrada)
print("Resultado seguro:", resultado_seguro)
