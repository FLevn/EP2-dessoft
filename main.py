# Define a posição do navio

def define_posicoes(linha, coluna, orientacao, tamanho):
    lista = []
    n = 0
    if orientacao == 'vertical':
        while n < tamanho:
            lista.append([linha+n,coluna])
            n += 1
    if orientacao == 'horizontal':
        while n < tamanho:
            lista.append([linha,coluna+n])
            n += 1
    return lista

# Preenche a frota

def preenche_frota(frota,navio,linha,coluna,orientacao,tamanho):
    posicao = define_posicoes(linha,coluna,orientacao,tamanho)
    for k, lista in frota.items():
        if k == navio:
            lista.append(posicao)
            return frota
    frota[navio] = [posicao]
    return frota

# Atualiza o tabuleiro depois de uma jogada

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

# Posiciona a frota no tabuleiro

def posiciona_frota(frota):
    tabuleiro = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],]
    for k, lista in frota.items():
        if k == "porta-aviões":
            i = 0
            while i < len(lista[0]):
                x = lista[0][i][0]
                y = lista[0][i][1]
                tabuleiro[x][y] = 1
                i += 1
        if k == "navio-tanque":
            i = 0
            j = 0
            while j < len(lista):
                while i < len(lista[j]):
                    x = lista[j][i][0]
                    y = lista[j][i][1]
                    tabuleiro[x][y] = 1
                    i += 1
                j += 1
                i = 0
        if k == "contratorpedeiro":
            i = 0
            j = 0
            while j < len(lista):
                while i < len(lista[j]):
                    x = lista[j][i][0]
                    y = lista[j][i][1]
                    tabuleiro[x][y] = 1
                    i += 1
                j += 1
                i = 0
        if k == "submarino":
            i = 0
            j = 0
            while j < len(lista):
                while i < len(lista[j]):
                    x = lista[j][i][0]
                    y = lista[j][i][1]
                    tabuleiro[x][y] = 1
                    i += 1
                j += 1
                i = 0
    return tabuleiro