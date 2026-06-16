def valida_posicao(entrada):
    if len(entrada) != 3:
        return False
    if entrada[0] not in "012":
        return False
    if entrada[2] not in "012":
        return False
    return True

def mostrar_tabuleiro(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

def verificar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == jogador:
            return True
    return False

tabuleiro = [" "] * 9

jogador_da_vez = "X"
ha_vencedor = False
jogadas = 0

while not ha_vencedor and jogadas < 9:

    mostrar_tabuleiro(tabuleiro)

    jogada = input(
        f"\nJogador {jogador_da_vez}, digite a posição (linha,coluna): "
    )
    if valida_posicao(jogada):
        linha = int(jogada[0])
        coluna = int(jogada[2])
        posicao = linha * 3 + coluna
        if tabuleiro[posicao] == " ":
            tabuleiro[posicao] = jogador_da_vez
            jogadas += 1
            if verificar_vitoria(tabuleiro, jogador_da_vez):
                ha_vencedor = True
            else:
                jogador_da_vez = "O" if jogador_da_vez == "X" else "X"
        else:
            print("Posição já ocupada!")
    else:
        print("Jogada inválida!")
print()

if ha_vencedor:
    mostrar_tabuleiro(tabuleiro)
    print(f"\nParabéns! Jogador {jogador_da_vez} venceu!")

else:
    mostrar_tabuleiro(tabuleiro)
    print("\nDeu velha!")