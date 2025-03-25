import os
def limpar_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')
        
def area_quadrilatero():
    limpar_terminal()
    escolha = int(input("Olá! Esse é o bot para saber a área do quadrilatero!\n\nPor favor, me informe qual é o tipo de quadrilatero que você quer saber:\n\n[1] Trapézio\n[2] paralelogramo\n[3] Retângulo\n[4] Losango\n[5] Quadrado\n\nDigite um número: "))

    match escolha:
        case 1:
            limpar_terminal()
            maiorBase = int(input("Informe a maior base:\n\n"))
            menorBase = int(input("Informe a menor base:\n\n"))
            altura = int(input("Informe a altura:\n\n"))

            formula = ((maiorBase + menorBase)*altura)/2

            print(f"O trapézio informado tem a área de {formula}.")
        case 2:
            limpar_terminal()
            base = int(input("informe a base:\n\n"))
            altura = int(input("informe a altura:\n\n"))

            formula = base*altura
            print(f"A área do seu paralelogramo é de {formula}")
        case 3:
            limpar_terminal()
            base = int(input("informe a base:\n\n"))
            altura = int(input("informe a altura:\n\n"))
            
            formula = base*altura
            print(f"A área do seu  retangulo é de {formula}")
        case 4:
            limpar_terminal()
            diagonal1 = input("Informe a primeira diagonal:\n\n")
            diagonal2 = input("Informe a segunda diagoal:\n\n")

            formula = diagonal1*diagonal2/2

            print("A área do seu losango é de {formula}")
        case 5:
            base = int(input("informe a base:\n\n"))
            altura = int(input("informe a altura:\n\n"))

            formula = base*altura
            print(f"A área do seu quadrado é de {formula}")
            
        case _:
            print("Rapaiz... ativa o numLock aí.")
    
