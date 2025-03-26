import os

def limpar_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

def area_triangulo():
    limpar_terminal()
    print("Olá! Vamos descobrir a área do seu triangulo? Simbora!")

    base = int(input("Informe a base:\nresposta: "))
    altura = int(input("Informe a altura:\nresposta: "))

    formula = (base*altura)/2

    print(f"Seu triangulo tem a área de {formula}")
    

