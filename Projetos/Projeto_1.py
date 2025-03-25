import os
import time

def Quadrilatero():
    def idiota():        
        angulosIguais = input("Seu Quadrilatero possui os 4 angulos iguais? É só responder com S ou N .\n").lower()
        if (angulosIguais == "s"):
            limpar_terminal()
            ladosIguais = input("Seu quadrilatero possui os 4 lados iguais também? S ou N \n").lower()
            if (ladosIguais == "s"):
                print("Então seu quadrilatero é absolutamente um QUADRADO! Obrigado por consultar, se precisar de mais alguma coisa\nnão conte comigo, eu sou só um bot que responde se um quadrilatero é um \nQUADRADO!")
            elif (ladosIguais == "n"):
                print("Então não é um QUADRADO! só poder um QUADRADO se todos os lados forem iguais entre si assim como os angulos! Agradecemos a consulta, até depois!")
        elif(angulosIguais == "n"):
            limpar_terminal()
            print("Então não é um QUADRADO! A sua forma só pode ser um quadrado se todos os angulos forem iguais entre si, assim como os lados!")

    def normal():
        limpar_terminal()
        print("Por favor, informe todos os lados da sua forma geometrica:\n\n")
        lado1 = int(input("lado 1:\n"))
        lado2 = int(input("lado 2:\n"))
        lado3 = int(input("lado 3:\n"))
        lado4 = int(input("lado 4:\n"))
        limpar_terminal()
        print("Agora todos os angulos: \n\n")
        angulo1 = int(input("angulo 1:\n"))
        angulo2 = int(input("angulo 2:\n"))
        angulo3 = int(input("angulo 3:\n"))
        angulo4 = int(input("angulo 4:\n"))

        limpar_terminal()
        print("Certo, vamos ver.")
        time.sleep(1)
        limpar_terminal()
        print("Certo, vamos ver..")
        time.sleep(1)
        limpar_terminal()
        print("Certo, vamos ver...")
        time.sleep(1)

        lados = [lado1, lado2, lado3, lado4]
        x = len(set(lados)) == 1
        angulos = [angulo1, angulo2, angulo3, angulo4]
        y = len(set(angulos)) == 1

        if x and y:
            print("Sua forma geométrica é um QUADRADO! Parabéns!")
            print("Se precisar de mais alguma coisa, não conte comigo, só sei dizer se é um QUADRADO ou não... tchau!")
        else:
            print("Não é um quadrado, putz... que pena. Qualquer coisa me roda denovo, até mais!")
            
        
        
    def limpar_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    limpar_terminal()
    print("Olá! Esse é o bot projetado com calculos absurdos e complexos, para que possamos descobrir se a sua forma geometrica plana é um QUADRADO!")
    time.sleep(1)
    limpar_terminal()
    print("Então vamos começar!")
    time.sleep(3)
    limpar_terminal()
    print("Mas antes... você gostaria de descobrir do jeito normal ou do jeito idiota?")

    while True:
        resposta = input("0 - Normal\n1 - Idiota\n\n")
        if resposta == "0":
            normal()
        elif resposta == "1":
            idiota()
        else:
            print("Tá dificil de digitar 0 ou 1?\n\n")
        break
