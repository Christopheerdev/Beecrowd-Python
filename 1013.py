# Lê três valores inteiros na mesma linha
a, b, c = map(int, input().split())

# Fórmula para encontrar o maior entre dois números
maior_ab = (a + b + abs(a - b)) // 2

# Aplica novamente a fórmula para comparar com o terceiro número
maior = (maior_ab + c + abs(maior_ab - c)) // 2

# Exibe o resultado no formato pedido
print(f"{maior} eh o maior")
