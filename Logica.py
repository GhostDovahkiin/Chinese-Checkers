letras = ["A","B","C","D","E","F"]
def letra ():
    ovo = letras
    return ovo
def adicionarPecas(tabuleiro,numJogadores):
    contador = 0
    if numJogadores == 2:
        for q in range(4):
            for w in range(q+1):
                tabuleiro[q][w] = letras[0]
        contador = 3
        for q in range(13,17):
            for w in range(contador, -1, -1):
                tabuleiro[q][w] = letras[1]
            contador -= 1
        return tabuleiro
    elif numJogadores == 3:
        for q in range(4):
            for w in range(q+1):
                tabuleiro[q][w] = letras[0]
        contador = 1
        for q in range(9, 13):
            for w in range(contador):
                tabuleiro[q][w] = letras[1]
            contador += 1
        contador = 10
        for q in range(9,13):
            for w in range(9,contador):
                tabuleiro[q][w] = letras[2]
            contador += 1
        return tabuleiro
    elif numJogadores == 4:
        contador = 4
        for q in range(4,8):
            for w in range(contador):
                tabuleiro[q][w] = letras[0]
            contador -= 1
        contador = 1
        for q in range(9,13):
            for w in range(contador):
                tabuleiro[q][w] = letras[1]
            contador += 1
        contador = 10
        for q in range(9,13):
            for w in range(9,contador):
                tabuleiro[q][w] = letras[2]
            contador += 1
        contador = 13    
        for q in range(4,8):
            for w in range(9,contador):
                tabuleiro[q][w] = letras[3]
            contador -=1
        return tabuleiro
    elif numJogadores == 6:
        for q in range(4):
            for w in range(q+1):
                tabuleiro[q][w] = letras[0]
        contador = 3
        for q in range(13,17):
            for w in range(contador, -1, -1):
                tabuleiro[q][w] = letras[3]
            contador -= 1
        contador = 4
        for q in range(4,8):
            for w in range(contador):
                tabuleiro[q][w] = letras[1]
            contador -= 1
        contador = 1
        for q in range(9,13):
            for w in range(contador):
                tabuleiro[q][w] = letras[2]
            contador += 1
        contador = 10
        for q in range(9,13):
            for w in range(9,contador):
                tabuleiro[q][w] = letras[4]
            contador += 1
        contador = 13    
        for q in range(4,8):
            for w in range(9,contador):
                tabuleiro[q][w] = letras[5]
            contador -=1
        return tabuleiro
def executarMovimento(linha, coluna, linhaDestino, colunaDestino,tabuleiro):
    tabuleiro[linhaDestino][colunaDestino] = tabuleiro[linha][coluna]
    tabuleiro[linha][coluna] = "0"

    return tabuleiro
def pegarProximaPosicao(linhaAtual, posicaoNaLinhaAtual, direcao, salto):
    if salto == True:
        quantidadeDeLinhasPraPular=2
    else:
        quantidadeDeLinhasPraPular=1

    
    proximaLinha = linhaAtual
    
    if direcao == "ul" or direcao == "ur":
        proximaLinha -= quantidadeDeLinhasPraPular
        
    elif direcao == "dl" or direcao == "dr":
        proximaLinha += quantidadeDeLinhasPraPular

    deslocamento = 0
    if (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=1 and proximaLinha<=4)) or   
    ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=14 and proximaLinha<=17)) or   
    ((linhaAtual>=5 and linhaAtual<=13) and (proximaLinha>=5 and proximaLinha<=13))):      
        deslocamento = 0
        
    elif (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=5 and proximaLinha<=9)) or 
    ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=9 and proximaLinha<=13))):     
        deslocamento = 4
        
    elif (((linhaAtual>=5 and linhaAtual<=9) and (proximaLinha>=1 and proximaLinha<=4)) or 
    ((linhaAtual>=9 and linhaAtual<=13) and (proximaLinha>=14 and proximaLinha<=17))):     
        deslocamento = -4

    posicaoNaProximaLinha = posicaoNaLinhaAtual
    if direcao=="ul":
        if (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=1 and proximaLinha<=4)) or  
        ((linhaAtual>=9 and linhaAtual<=13) and (proximaLinha>=9 and proximaLinha<=13)) or
        ((linhaAtual>=5 and linhaAtual<=6) and (proximaLinha>=3 and proximaLinha<=4))):       
            posicaoNaProximaLinha += deslocamento - quantidadeDeLinhasPraPular

            if linhaAtual == 6 and proximaLinha == 4:                                          
                posicaoNaProximaLinha += 1

        else:
            posicaoNaProximaLinha += deslocamento
            if linhaAtual == 14 and proximaLinha == 12:                                        
                posicaoNaProximaLinha -= 1
    elif direcao=="ur" :

        if (((linhaAtual>=5 and linhaAtual<=9) and (proximaLinha>=5 and proximaLinha<=9)) or  
        ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=14 and proximaLinha<=17)) or   
        ((linhaAtual>=14 and linhaAtual<=15) and (proximaLinha>=12 and proximaLinha<=13))):    
            posicaoNaProximaLinha += deslocamento + quantidadeDeLinhasPraPular

            if linhaAtual == 14 and proximaLinha == 12:                                        
                posicaoNaProximaLinha -= 1
        else:

            posicaoNaProximaLinha += deslocamento
            if linhaAtual == 6 and proximaLinha == 4:                                          
                posicaoNaProximaLinha += 1
    elif direcao=="dr" :
        if (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=1 and proximaLinha<=6)) or   
        ((linhaAtual>=9 and linhaAtual<=13) and (proximaLinha>=9 and proximaLinha<=15)) or    
        ((linhaAtual>=12 and linhaAtual<=13) and (proximaLinha>=14 and proximaLinha<=15))):   
            posicaoNaProximaLinha += deslocamento + quantidadeDeLinhasPraPular

            if ((linhaAtual == 4 and proximaLinha == 6) or                                    
            (linhaAtual == 12 and proximaLinha == 14)):                                       
                posicaoNaProximaLinha -= 1

            elif(linhaAtual==13 and (proximaLinha>=14 and proximaLinha<=15)):                  
                posicaoNaProximaLinha -= quantidadeDeLinhasPraPular
        else:
            posicaoNaProximaLinha += deslocamento            

    elif direcao=="dl" :
        if (((linhaAtual>=5 and linhaAtual<=9) and (proximaLinha>=5 and proximaLinha<=9)) or  
        ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=14 and proximaLinha<=17)) or  
        ((linhaAtual>=12 and linhaAtual<=13) and (proximaLinha>=14 and proximaLinha<=15))):   
            posicaoNaProximaLinha += deslocamento - quantidadeDeLinhasPraPular

            if linhaAtual == 12 and proximaLinha == 14:                                        
                posicaoNaProximaLinha += 1

        else:
            posicaoNaProximaLinha += deslocamento

            if linhaAtual == 4 and proximaLinha == 6:                                          
                posicaoNaProximaLinha -= 1
            
    elif direcao == "l":
        posicaoNaProximaLinha -= quantidadeDeLinhasPraPular

    else:
        posicaoNaProximaLinha += quantidadeDeLinhasPraPular

    return [proximaLinha, posicaoNaProximaLinha]


def pertenceAoTabuleiro(linha,coluna):

    linha=(int(linha)-1)
    coluna= (int(coluna)-1)

    if linha >= 0 and linha <= 3:

        if (linha == 0 and coluna == 0) or (linha == 1 and (coluna == 0 or coluna == 1)) or (linha == 2 and (coluna >= 0 and coluna <= 2)) or (linha == 3 and (coluna >= 0 and coluna <= 3)):
            return True
        else:
            return False
    
    elif linha >=4 and linha <= 7:

        if linha == 4 and (coluna >= 0 and coluna <= 12) or (linha == 5 and (coluna >= 0 and coluna <= 11)) or (linha == 6 and (coluna >= 0 and coluna <= 10)) or (linha == 7 and (coluna >= 0 and coluna <= 9)):
            return True
        else:
            return False
        
    elif linha >= 8 and linha <= 12:

        if linha == 8 and (coluna >= 0 and coluna <= 8) or linha == 9 and (coluna >= 0 and coluna <= 9) or linha == 10 and (coluna >= 0 and coluna <= 10) or linha == 11 and (coluna >= 0 and coluna <= 11) or linha == 12 and (coluna >= 0 and coluna <= 12):
            return True

        else: 
            return False

    elif linha >= 13 and linha <= 16:

        if linha == 13 and (coluna >= 0 and coluna <= 3) or linha == 14 and (coluna >= 0 and coluna <= 2) or linha == 15 and (coluna >= 0 and coluna <= 1) or linha == 16 and coluna == 0:
            return True

        else:
            return False

    else:
        return False

    
def localVazio(proximaLinha,proximaColuna,tabuleiro):

    if tabuleiro[proximaLinha][proximaColuna] == "0":
        return True

    else:
        return False

def verificarSuaPeca (tabuleiro,letra,numJogadores,linha,coluna):
    
    if numJogadores == 2:

        if tabuleiro[linha][coluna] == letra:
            return True

        else:
            return False

    elif numJogadores == 3:

        if tabuleiro[linha][coluna] == letra:
            return True

        else:
            return False

    elif numJogadores == 4:
        if tabuleiro[linha][coluna] == letra:
            return True

        else:
            return False

    elif numJogadores == 6:
        if tabuleiro[linha][coluna] == letra:
            return True

        else:
            return False

def Salto(tabuleiro,linha,coluna,direcao):
    Jogada1 = pegarProximaPosicao(linha, coluna, direcao, salto=False)
    proximalinha = Jogada1[0]-1
    proximaColuna = Jogada1[1]-1
    LocalDisp = localVazio(proximalinha,proximaColuna,tabuleiro)

    if LocalDisp == True:
        return Jogada1
    else:
        Jogada = pegarProximaPosicao(linha, coluna, direcao, salto=True)
        return Jogada

def SaltoComposto(tabuleiro,linha,coluna,direcao,jogada):
    if len(jogada) > 3:
        for i in jogada[2:]:
            direcao = i
            A = Salto(tabuleiro, linha, coluna, direcao)
            linha = A[0]
            coluna = A[1]
            
        return A
    else:
        move = Salto(tabuleiro,linha,coluna,direcao)
        return move

def verificaSeGanhou(letras, numJogadores, tabuleiro):
    if numJogadores == 2:
        def ganhouLocal1(letras):
          for i in range(4):
            for j in tabuleiro[i]:
              if [j] != letras[0]:
                    return False
                    break
        return True

        def ganhouLocal2(letras):
            for i in range(4):
                for j in tabuleiro[i+14]:
                    if [j] != letras[3]:
                        return False
                        break
        return True

    elif numJogadores == 3:
        def ganhouLocal3(letras):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][j] != letras[0]:
                        return False
                        break
                elemento -= 1
            return True

        def ganhouLocal4(letras):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][-j-1] != letras[3]:
                        return False
                        break
                elemento -= 1
            return True

        def ganhouLocal2(letras):
            for i in range(4):
                for j in tabuleiro[i+14]:
                    if [j] != letras[5]:
                        return False
                        break
    elif numJogadores == 4:
        def ganhouLocal3(letras):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][j] != letras[2]:
                        return False
                        break
                elemento -= 1
            return True

        def ganhouLocal4(letras):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][-j-1] != letras[3]:
                        return False
                        break
                elemento -= 1
            return True

        def ganhouLocal5(letras):
            elemento = 1
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i][j] != letras[5]:
                        return False
                        break
                elemento += 1
            return True

        def ganhouLocal6(letras):
                elemento = 1
                for i in range(4):
                    for j in range(elemento):
                        if tabuleiro[i][-j-1] != letras[6]:
                            return False
                            break
                    elemento += 1
                return True

    elif numJogadores == 6:
        def ganhouLocal1(letras):
          for i in range(4):    
            for j in tabuleiro[i]:
              if [j] != letras[0]:
                    return False
                    break
        return True

        def ganhouLocal2(letras):
            for i in range(4):
                for j in tabuleiro[i+14]:
                    if [j] != letras[1]:
                        return False
                        break
        def ganhouLocal3(letras):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][j] != letras[2]:
                        return False
                        break
                elemento -= 1
            return True

        def ganhouLocal4(letras):
            elemento = 4
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i+5][-j-1] != letras[3]:
                        return False
                        break
                elemento -= 1
            return True

        def ganhouLocal5(letras):
            elemento = 1
            for i in range(4):
                for j in range(elemento):
                    if tabuleiro[i][j] != letras[4]:
                        return False
                        break
                elemento += 1
            return True

        def ganhouLocal6(letras):
                elemento = 1
                for i in range(4):
                    for j in range(elemento):
                        if tabuleiro[i][-j-1] != letras[5]:
                            return False
                            break
                    elemento += 1
                return True

def JogadaValida(tabuleiro,numjogadores, nome):
    import GUI
    fim = False
    while not fim:
        try:
            GUI.Jogada(tabuleiro)
            fim = True
        except IndexError:
            print("Jogada Inválida, tente novamente")
            GUI.Jogada(tabuleiro)
            fim = False




            
