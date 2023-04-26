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

# Preenche a frota no tabuleiro

def preenche_frota(frota,navio,linha,coluna,orientacao,tamanho):
    posicao = define_posicoes(linha,coluna,orientacao,tamanho)
    for k, lista in frota.items():
        if k == navio:
            lista.append(posicao)
            return frota
    frota[navio] = [posicao]
    return frota