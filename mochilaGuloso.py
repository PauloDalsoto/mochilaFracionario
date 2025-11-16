def mochila_fracionaria(itens, capacidade):
    """
    itens: lista de tuplas (valor, peso)
    capacidade: peso máximo da mochila
    """
    
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
        else:
            # Pega apenas uma fração
            restante = capacidade - peso_atual
            fracao = restante / peso
            valor_total += valor * fracao
            peso_atual += peso * fracao
            itens_usados.append((valor, peso, fracao))
            break  # mochila cheia
    
    return valor_total, itens_usados

if __name__ == "__main__":
    # Lista de itens (valor, peso)
    itens = [
        (60, 10),
        (100, 20),
        (120, 30)
    ]
    
    capacidade = 50
    
    valor_max, itens_usados = mochila_fracionaria(itens, capacidade)
    
    print(f"Capacidade da mochila: {capacidade}")
    print(f"Valor máximo obtido: {valor_max:.2f}\n")
    
    print("Itens escolhidos:")
    for v, p, f in itens_usados:
        print(f" - Valor: {v}, Peso: {p}, Fração usada: {f*100:.1f}%")
