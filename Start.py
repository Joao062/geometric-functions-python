import os
from Projetos import Projeto_1, Projeto_2, Projeto_3, Projeto_4, Projeto_5
def limpar_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')
limpar_terminal()
print("Olá! Esse é o Menu para acessar os projetinhos que eu fiz!")
escolha = int(input("\nAcesse escrevendo seu número abaixo:\n\n[1] O quadrilatero é um quadrado?\n[2] Área do quadrilatero\n[3] Perímetro do quadrilatero\n[4] Área do triangulo\n[5] Perimetro do triangulo\n\n"))

match escolha:
    case 1:
        Projeto_1.Quadrilatero()
    case 2:
        Projeto_2.area_quadrilatero()
    case 3:
        Projeto_3.perimetro_quadrilatero()
    case 4:
        Projeto_4.area_triangulo()
    case 5:
        Projeto_5.perimetro_triangulo()
    case _:
        print("Deixou uma panela cair em cima do seu teclado?")


