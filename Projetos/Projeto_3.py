import os

def limpar_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

def perimetro_quadrilatero():
    limpar_terminal()
    print("Eai meu chapa, bora descobrir o perimetro do seu quadrilatero!")
    lado1 = int(input("Informe um lado do seu quadrilatero:\n\nResposta: "))
    lado2 = int(input("Informe o proximo lado do seu quadrilatero:\n\nResposta: "))
    lado3 = int(input("Informe o terceiro lado do seu quadrilatero:\n\nResposta: "))
    lado4 = int(input("Informe o último lado do seu quadrilatero:\n\nResposta: "))

    perimetro = lado1+lado2+lado3+lado4

    print(f"perimetro do quadrilatero: {perimetro}")
    
    
