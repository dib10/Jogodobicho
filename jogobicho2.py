import random
from time import sleep
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
    elif numero in range(93, 97): #range no final sempre pega um número a menos
        return "Veado - Grupo 24 🦌"
    else:
        return "Vaca - Grupo 25 🐄"

print("\033[32mBem Vindo ao simulador de jogo do bicho 🐊\033[0m")

print("🦁Escolha uma modalidade para jogar")
modalidades = {
    1: "Dezena",
    2: "Centena",
    3: "Milhar (NÃO DISPONÍVEL)",
    4: "Grupo (NÃO DISPONÍVEL)"
}
for k, v in modalidades.items():
    print(f"[{k}] {v}") ## k seria key e v seria value, para representar cada item e seu correspondente
modalidade = 0
while not 1 <= modalidade <= 4: #vericar se o usuário digita uma das modalidades
    modalidade = int(input("Digite o número da modalidade: "))
    if not 1 <= modalidade <= 4:
        print("\033[31mModalidade inválida! Digite um número de 1 a 4.\033[0m")

print("🦁Modalidade selecionada:", modalidades[modalidade])

if modalidade == 1:  # dezena
    numero = None
    numero_gerado = random.randint(0, 9999)
    while numero not in range(0, 100):
        numero = int(input('🔟Digite uma dezena para jogar na modalidade "Dezena": '))
        valor_aposta = float(input("💰Digite o valor que deseja apostar:R$ "))
        possivel_ganho = valor_aposta * 60
        lucro = possivel_ganho - valor_aposta
        aposta_ultimos_dois = numero % 100
        sorteio_ultimos_dois = numero_gerado % 100
        animal_aposta = obter_animal(aposta_ultimos_dois)
        animal_sorteado = obter_animal(sorteio_ultimos_dois)
    print(" ")
    print("-" * 100)
    print(f' 🎮 Você está jogando na modalidade: {modalidades[modalidade]}')
    print(f' 💲 Caso você ganhe, seu lucro será de R$ {lucro}')
    print("-" * 100)
    print('O número está sendo sorteado, boa sorte!😉')
    sleep(3)
    print("-" * 100)
    if numero == sorteio_ultimos_dois or numero == numero_gerado:
        print(f'🥳Parabéns, você acertou a dezena! 🥳')
        print(f'💸💸\033[32mVocê investiu R${valor_aposta},e ganhou R${possivel_ganho}\033[m💸💸')

        print("-" * 100)
        print(f'\033[36mO número sorteado foi:\033[0m "\033[32m{numero_gerado}\033[0m"')
        print(f'\033[36mDezena do número sorteado é:\033[0m "\033[32m{str(numero_gerado % 100).zfill(2)}\033[0m"')  # aqui ele pega os dois últimos dígitos
        print("\033[1;36mAnimal sorteado:\033[m", animal_sorteado)
        print("-" * 100)
        print(f'\033[35mDezena apostada: \033[m{str(numero).zfill(2)}')
        print(f'\033[35mAnimal correspondente do número apostado:\033[m{obter_animal(numero)}')
    else:
        print(f'\033[31m😭Lamentamos mas você não acertou o número!😭\033[m')
        print(f'\033[31mInfelizmente você investiu R$ {valor_aposta}, e não obteve retorno\033[m.😞')
        print("-" * 100)
        print(f'\033[36mO número sorteado foi:\033[0m "\033[32m{numero_gerado}\033[0m"')
        print(f'\033[36mDezena do número sorteado é:\033[0m "\033[32m{str(numero_gerado % 100).zfill(2)}\033[0m"')  # aqui ele pega os dois últimos dígitos
        print("\033[1;36mAnimal sorteado:\033[m", animal_sorteado)
        print("-" * 100)
        print(f'\033[35mDezena apostada: \033[m{str(numero).zfill(2)}')
        print(f'\033[35mAnimal correspondente do número apostado:\033[m{obter_animal(numero)}')


elif modalidade == 2: #centena
    numero = None
    numero_gerado = random.randint(0,9999)
    while numero not in range(0,999):
        numero = int(input('🔟Digite uma centena para jogar na modalidade "Centena": '))
    aposta_ultimos_dois = numero % 100
    sorteio_ultimos_dois = numero_gerado % 100
    animal_aposta = obter_animal(aposta_ultimos_dois) #animal da sua aposta
    animal_sorteado = obter_animal(sorteio_ultimos_dois) #animal que foi sorteado
    print(" ")
    print("-" * 100)
    print(f' 🎮 Você está jogando na modalidade: {modalidades[modalidade]}')
    print("-" * 100)
    print('O número está sendo sorteado, boa sorte!😉')
    sleep(3)
    print("-" * 100)
    if numero == numero_gerado or numero == numero_gerado %1000:
        print(f'🥳Parabéns, você acertou a centena! 🥳')
        print("-" * 100)
        print(f'\033[36mO número sorteado foi:\033[0m "\033[32m{numero_gerado}\033[0m"')
        print(f'\033[36mCentena do número sorteado é:\033[0m "\033[32m{str(numero_gerado % 1000).zfill(3)}\033[0m"')  # aqui ele pega os tres últimos dígitos
        print("\033[1;36mAnimal sorteado:\033[m", animal_sorteado)
        print("-" * 100)
        print(f'\033[35mCentena apostada: \033[m{str(numero).zfill(3)}')
        print(f'\033[35mAnimal correspondente do número apostado: \033[m{obter_animal(numero%100)}')
    else:
        print(f'\033[31m😭Lamentamos mas você não acertou o número!😭\033[m')
        print("-" * 100)
        print(f'\033[36mO número sorteado foi:\033[0m "\033[32m{numero_gerado}\033[0m"')
        print(f'\033[36mCentena do número sorteado é:\033[0m "\033[32m{str(numero_gerado % 1000).zfill(3)}\033[0m"')  # aqui ele pega os tres últimos dígitos
        print("\033[1;36mAnimal sorteado:\033[m", animal_sorteado)
        print("-" * 100)
        print(f'\033[35mCentena apostada: \033[m{str(numero).zfill(3)}')
        print(f'\033[35mAnimal correspondente do número apostado: \033[m{obter_animal(numero%100)}')

