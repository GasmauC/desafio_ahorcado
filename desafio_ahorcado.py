from random import * 

lista = ['panadero','dinosaurio','helipuerto','tiburon']

def elegir_palabra(palabra):
    opcion = choice(palabra)
    return opcion

def mostrar_giones(palabra_secreta, letras_adivinadas):
    tablero_visual = []

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero_visual.append(letra)
        else:
            tablero_visual.append('_')
    
    print(" ".join(tablero_visual))

def validar():
    letra = input("Ingrese una letra: ").lower()

    while not letra.isalpha() or len(letra) != 1:
        print("Error: Eso no es una letra.")
        letra = input("Intente nuevamente. Ingrese una letra: ").lower()
    return letra

def control_vidas(letra,palabra_oculta):
    
    if letra in palabra_oculta:
        return True
    else:
        return False

vidas = 5
letras_adivinadas = []  #memoria de aciertos
palabra = elegir_palabra(lista) 

# 2 EL JUEGO 
while vidas > 0:
    
    # A Mostramos cómo va el juego
    mostrar_giones(palabra, letras_adivinadas)
    print(f"Vidas restantes: {vidas}")

    # B Pedimos la letra (usando tu función)
    letra = validar()

    # C Verificamos si acertó (usando tu función)
    es_acierto = control_vidas(letra, palabra)

    # D Tomamos decisiones según lo que devolvió la función
    if es_acierto:
        print("¡Adivinaste una!")
        letras_adivinadas.append(letra) # Guardamos el acierto
    else:
        print("¡Fallaste!")
        vidas -= 1  # Restamos vida

    coincidencias = 0
    for letra_secreta in palabra:
        if letra_secreta in letras_adivinadas:
            coincidencias += 1
    
    # Si la cantidad de coincidencias es igual al largo de la palabra... ganaste!!!
    if coincidencias == len(palabra):
        print(f"¡GANASTE! La palabra era: {palabra}")
        break  
# 3 FIN DEL JUEGO
if vidas == 0:
    print("Perdiste. Fin del juego.")
