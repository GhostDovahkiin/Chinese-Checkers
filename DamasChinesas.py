#!-*- enconding: utf8 -*-
import GUI
import Logica




nome = []

numJogadores = GUI.menuInicial()
tabuleiro = GUI.criarTabuleiro()

tabuleiro = Logica.adicionarPecas(tabuleiro,numJogadores)
letras = Logica.letra()
for i in range(numJogadores):
    a = i
    nome.insert(i,input("Digite seu nome(Jogador {}): ".format(a+1)))

print("\n\n")
GUI.imprimirTabuleiro(tabuleiro)
print()
ganhador = 0
while ganhador == 0:
    
    GUI.playerNome(numJogadores, nome, tabuleiro)
    m = Logica.verificaSeGanhou(letras, numJogadores, tabuleiro)
    if m == True:
        ganhador += 0

    else:
        ganhador += 1
        print("Parabéns, você ganhou!")
        
