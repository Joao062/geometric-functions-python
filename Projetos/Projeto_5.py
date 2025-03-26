import os
def limpar_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

def perimetro_triangulo():
    limpar_terminal()
    print("Olá, vamos descobrir qual é o perimetro do seu triangulo!")
    print("Vou precisar que apenas me informe os 3 lados do triangulo, vamo nessa!")

    lado1 = int(input("Informe o primeiro lado do seu triangulo:\n\nresposta: "))
    lado2 = int(input("Informe o segundo lado do seu triangulo:\n\nresposta: "))
    lado3 = int(input("Informe o terceiro lado do seu triangulo:\n\nresposta: "))

    formula = lado1+lado2+lado3

    print(f"Seu triangulo tem o perimetro de {formula}")
