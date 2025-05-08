def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 10)

def verificar_vitoria(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != " ":
            return True

    # Verificar colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != " ":
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    for turno in range(9):
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")

        try:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))

            if tabuleiro[linha][coluna] != " ":
                print("Posição já ocupada! Tente novamente.")
                continue

            tabuleiro[linha][coluna] = jogador_atual

            if verificar_vitoria(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                return

            jogador_atual = "O" if jogador_atual == "X" else "X"
        except (ValueError, IndexError):
            print("Entrada inválida! Tente novamente.")

    exibir_tabuleiro(tabuleiro)
    print("Empate!")

if __name__ == "__main__":
    jogo_da_velha()