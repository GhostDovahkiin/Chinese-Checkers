import time
import Logica
import playsound
def menuInicial():
    def cls(): 
        print("\n" * 25)
    print("""             ❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏
             ❏                                         DAMAS CHINESAS                                               ❏
             ❏                                                                                                      ❏
             ❏                             •Grupo: Pedro Henrique  | Lucas Antonio                                  ❏ 
             ❏                                                                                                      ❏
             ❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏❏""")
    print()
    playsound.playsound('mus01.mp3')
    players = int(input("Informe a quantidade de players: "))
    if players == 2 or players == 3 or players == 4 or players == 6:
        return players
    else:
        time.sleep(0.5)
        cls()
        menuInicial()

"""def ListaJogadores(players):
    jogadores = []
    cont = 0
    for i in range(players):
        jogadores.append(str(input("Informe seu nome: ")))
        cont += 1
"""

def limparTela():
    return ("\n"*50)


def criarTabuleiro():
    tabuleiro = []
    for linha in range(4):
          tabuleiro.append([])
          for coluna in range(linha+1):
                  tabuleiro[linha].append("0")

    for linha in range (9,4,-1):
          tabuleiro.append([])
          for coluna in range(linha+4):
                  tabuleiro[len(tabuleiro)-1].append("0")

    for linha in range(10,14):
          tabuleiro.append([])
          for coluna in range(linha):
                  tabuleiro[len(tabuleiro)-1].append("0")

    for linha in range(4,0,-1):
          tabuleiro.append([])
          for coluna in range(linha):
                 tabuleiro[len(tabuleiro)-1].append("0")
    return(tabuleiro)


def imprimirLinhaComEspaco(tabuleiro, linha, espaco):
    print(" "*espaco,end="")
    for i in tabuleiro[linha]:
        print(i,"",end="")
    print("")
        
def imprimirTabuleiro(tabuleiro):       
    cont = 0
    linha = 1
    for i in range(13,9,-1): 
        print(70*" ",linha,end="")  
        imprimirLinhaComEspaco(tabuleiro,cont,i)
        cont += 1
        linha += 1
    cont = 4
    for i in range(1,6):
        print(70*" ",linha,end="")
        imprimirLinhaComEspaco(tabuleiro,cont,i)
        cont += 1
        linha += 1
    cont = 9   
    for i in range(4,0,-1):
        print(69*" ",linha,end="")
        imprimirLinhaComEspaco(tabuleiro,cont,i)
        cont += 1
        linha += 1
    cont = 13    
    for i in range(10,14):
        print(69*" ",linha,end="")
        imprimirLinhaComEspaco(tabuleiro,cont,i)
        cont += 1
        linha += 1

def Jogada(tabuleiro):

    jogada = input("Digite sua linha - Sua posição na linha - Sua jogada : ").split("-")
    linha = int(jogada[0])
    coluna = int(jogada[1])
    direcao = jogada[2]
    print(5*"\n")
    pertence = Logica.pertenceAoTabuleiro(linha,coluna)
    movimento = Logica.SaltoComposto(tabuleiro, linha,coluna,direcao,jogada)
    proximaLinha = (movimento[0]) - 1
    proximaColuna = (movimento[1]) -1

    if pertence == False:
        print("Jogada Inválida ...")
        imprimirTabuleiro(tabuleiro)
        Jogada(tabuleiro)
        while pertence == False:
            print("Jogada nao pôde ser efetuada, tente novamente")
            jogada = input("Digite sua linha - Sua posição na linha - Sua jogada : ").split("-")
            linha = int(jogada[0])
            coluna = int(jogada[1])
            direcao = jogada[2]
            pertence = Logica.pertenceAoTabuleiro(linha,coluna),
            localVago = Logica.localVazio(proximaLinha,proximaColuna,tabuleiro)

        
    linha -= 1
    coluna -= 1
    tabuleiro = Logica.executarMovimento(linha,coluna,proximaLinha,proximaColuna,tabuleiro)
    imprimirTabuleiro(tabuleiro)

def playerNome(numJogadores, nome, tabuleiro):
    if numJogadores == 2:
        print("""Vez de : {} \nPeça: "{}" """ .format(nome[0], "A"))
        Logica.JogadaValida(tabuleiro, nome, tabuleiro)    
        if numJogadores == 2:
            print("""Vez de : {} \nPeça: "{}" """ .format(nome[1], "B"))
            Logica.JogadaValida(tabuleiro, nome, tabuleiro) 
    elif numJogadores == 3:
        print("""Vez de : {} \nPeça: "{}" """ .format(nome[0], "A"))
        Jogada(tabuleiro)    
        if numJogadores == 3:
            print("""Vez de : {} \nPeça: "{}" """ .format(nome[1], "B"))
            Jogada(tabuleiro)
            if numJogadores == 3:
                print("""Vez de : {} \nPeça: "{}" """ .format(nome[2], "C"))
                Jogada(tabuleiro)
    elif numJogadores == 4:
        print("""Vez de : {} \nPeça: "{}" """ .format(nome[0], "A"))
        Jogada(tabuleiro)    
        if numJogadores == 4:
            print("""Vez de : {} \nPeça: "{}" """ .format(nome[1], "B"))
            Jogada(tabuleiro)
            if numJogadores == 4:
                print("""Vez de : {} \nPeça: "{}" """ .format(nome[2], "C"))
                Jogada(tabuleiro)
                if numJogadores == 4:
                    print("""Vez de : {} \nPeça: "{}" """ .format(nome[3], "D"))
                    Jogada(tabuleiro)
    else:
        print("""Vez de : {} \nPeça: "{}" """ .format(nome[0], "A"))
        Jogada(tabuleiro)    
        if numJogadores == 6:
            print("""Vez de : {} \nPeça: "{}" """ .format(nome[1], "B"))
            Jogada(tabuleiro)
            if numJogadores == 6:
                print("""Vez de : {} \nPeça: "{}" """ .format(nome[2], "C"))
                Jogada(tabuleiro)
                if numJogadores == 6:
                    print("""Vez de : {} \nPeça: "{}" """ .format(nome[3], "D"))
                    Jogada(tabuleiro)
                    if numJogadores == 6:
                        print("""Vez de : {} \nPeça: "{}" """ .format(nome[4], "E"))
                        Jogada(tabuleiro)
                        if numJogadores == 6:
                            print("""Vez de : {} \nPeça: "{}" """ .format(nome[5], "F"))
                            Jogada(tabuleiro)
