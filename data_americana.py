from datetime import datetime

# pega a data atual e formata no padrão americano
data_atual = datetime.now().strftime("%Y-%m-%d")

print("Data atual (formato americano):", data_atual)
# Exemplo de saída: Data atual (formato americano): 2024-06-15