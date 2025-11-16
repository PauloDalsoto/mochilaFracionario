def mochila_dp(itens, capacidade):
    n = len(itens)

    # DP[i][w] = melhor valor usando itens até i com capacidade w
    DP = [[0] * (capacidade + 1) for _ in range(n + 1)]

    # Construção da tabela
    for i in range(1, n + 1):
        valor, peso = itens[i - 1]
        for w in range(1, capacidade + 1):
            if peso <= w:
                DP[i][w] = max(
                    DP[i - 1][w],                 # não pega o item
                    valor + DP[i - 1][w - peso]   # pega o item
                )
            else:
                DP[i][w] = DP[i - 1][w]

    # Valor máximo
    valor_max = DP[n][capacidade]

    # Reconstrução dos itens usados
    itens_usados = []
    w = capacidade
    for i in range(n, 0, -1):
        if DP[i][w] != DP[i - 1][w]:  # se o valor mudou, o item foi incluído
            valor, peso = itens[i - 1]
            itens_usados.append((valor, peso, 1))  # fração = 1 (item inteiro)
            w -= peso

    return valor_max, itens_usados[::-1]  # reverte para ordem original


if __name__ == "__main__":
    itens = [
        (60, 10),
        (100, 20),
        (120, 30)
    ]

    capacidade = 50
    
    valor_max, itens_usados = mochila_dp(itens, capacidade)
    
    print(f"Capacidade da mochila: {capacidade}")
    print(f"Valor máximo obtido: {valor_max}\n")
    
    print("Itens escolhidos (apenas inteiros, sem frações):")
    for v, p, f in itens_usados:
        print(f" - Valor: {v}, Peso: {p}, Fração usada: {f}")
