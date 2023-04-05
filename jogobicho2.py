import random

def obter_animal(numero):
    if numero in range(1, 5):
        return "Avestruz - Grupo 1"
    elif numero in range(5, 9):
        return "Águia - Grupo 2 🦅"
    elif numero in range(9, 13):
        return "Burro - Grupo 3"
    elif numero in range(13, 17):
        return "Borboleta - Grupo 4 🦋"
    elif numero in range(17, 21):
        return "Cachorro - Grupo 5 🐶"
    elif numero in range(21, 25):
        return "Cabra - Grupo 6 🐐"
    elif numero in range(25, 29):
        return "Carneiro - Grupo 7 🐏"
    elif numero in range(29, 33):
        return "Camelo - Grupo 8 🐫"
    elif numero in range(33, 37):
        return "Cobra - Grupo 9 🐍"
    elif numero in range(37, 41):
        return "Coelho - Grupo 10 🐇"
    elif numero in range(41, 45):
        return "Cavalo - Grupo 11 🐎"
    elif numero in range(45, 49):
        return "Elefante - Grupo 12 🐘"
    elif numero in range(49, 53):
        return "Galo - Grupo 13 🐔"
    elif numero in range(53, 57):
        return "Gato - Grupo 14 🐱"
    elif numero in range(57, 61):
        return "Jacaré - Grupo 15 🐊"
    elif numero in range(61, 65):
        return "Leão - Grupo 16 🦁"
    elif numero in range(65, 69):
        return "Macaco - Grupo 17 🐒"
    elif numero in range(69, 73):
        return "Porco - Grupo 18 🐖"
    elif numero in range(73, 77):
        return "Pavão - Grupo 19 🦚"
    elif numero in range(77, 81):
        return "Peru - Grupo 20 🦃"
    elif numero in range(81, 85):
        return "Touro - Grupo 21 🐂"
    elif numero in range(85, 89):
        return "Tigre - Grupo 22 🐅"
    elif numero in range(89, 93):
        return "Urso - Grupo 23 🐻"
    elif numero in range(93, 97):
        return "Veado - Grupo 24 🦌"
    else:
        return "Vaca - Grupo 25 🐄"

print("\033[32mBem Vindo ao simulador de jogo do bicho 🐊\033[0m")

aposta = None
while True:
    try:
        aposta = int(input("Aposte um número (0-9999): "))
        if aposta < 0 or aposta > 9999:
            print("\033[31mNúmero inválido, tente novamente.\033[0m")
        else:
            break
    except ValueError:
        print("\033[31mEntrada inválida, tente novamente.\033[0m")


sorteio = random.randint(0, 9999)

aposta_ultimos_dois = aposta % 100
sorteio_ultimos_dois = sorteio % 100


animal_aposta = obter_animal(aposta_ultimos_dois)
animal_sorteado = obter_animal(sorteio_ultimos_dois)

print("\033[1;36mNúmero sorteado:\033[m", sorteio)
print("\033[1;36mAnimal sorteado:\033[m", animal_sorteado)
print("\033[33mSeu número apostado:\033[m", aposta)
print("\033[33mSeu animal apostado:\033[m", animal_aposta)


if aposta == sorteio:
    print("\033[0;32mParabéns, você ganhou a aposta!\033[m")
elif animal_aposta == animal_sorteado:
    print('\033[0;32mVocê acertou o grupo do animal!\033[m, \033[1;31mmas errou o número.\033[m')##mod
elif animal_aposta == animal_sorteado and aposta == sorteio:
    print('\033[0;32mVocê acertou o número e o grupo do animal!\033[m')
else:
    print("\033[1;31mDesculpe, você perdeu a aposta.\033[m")




