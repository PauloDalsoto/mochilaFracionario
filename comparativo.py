def mochila_gu(itens, capacidade):
    # Calcula o valor por unidade de peso e adiciona à lista
    itens_com_ratio = []
    for valor, peso in itens:
        ratio = valor / peso
        itens_com_ratio.append((valor, peso, ratio))
    
    # Ordena pela razão valor/peso (decrescente)
    itens_com_ratio.sort(key=lambda x: x[2], reverse=True)
    
    valor_total = 0.0  # valor acumulado
    peso_atual = 0.0   # peso usado na mochila
    itens_usados = []  # para mostrar o que foi adicionado
    
    for valor, peso, ratio in itens_com_ratio:
        if peso_atual + peso <= capacidade:
            # Cabe totalmente
            valor_total += valor
            peso_atual += peso
            itens_usados.append((valor, peso, 1.0))  # 100% do item
    
    return valor_total, itens_usados

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

def print_resultado(valor_max, itens_usados, capacidade):
    print(f"Capacidade da mochila: {capacidade}")
    print(f"Valor máximo obtido: {valor_max}\n")
    
    print("Itens escolhidos (apenas inteiros, sem frações):")
    for v, p, f in itens_usados:
        print(f" - Valor: {v}, Peso: {p}, Fração usada: {f}")
        
if __name__ == "__main__":
    # Lista de itens (valor, peso)
    itens = [
        (50, 2),
        (40, 1),
        (70, 3)
    ]

    capacidade = 5
    
    # Aloritmo guloso]
    print("Algoritmo Guloso:\n")
    valor_max, itens_usados = mochila_gu(itens, capacidade)
    print_resultado(valor_max, itens_usados, capacidade)
    
    print("\n" + "="*40 + "\n")
    
    # Programação dinâmica
    print("Programação Dinâmica:\n")
    valor_max, itens_usados = mochila_dp(itens, capacidade)
    print_resultado(valor_max, itens_usados, capacidade)
    
    
