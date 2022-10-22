#
# Autores:
# Alexandre Moraes
#
# data: 22/10/2022

# Entrada de dados

preco = float(input("informe o preço do produto: ")) # Solicita o preço do produto
desconto = float(input("informe o valor do desconto: ")) # Solicita o valor do desconto

# Processamento de dados

preco_desconto = preco - (preco * (desconto)) # Calcula o valor do produto com desconto

# Saída de dados

print(f"O preço do produto com desconto é: R$ {preco_desconto:,.2f}") # exibe o valor do produto com desconto

print("fim do programa") # Informa ao usuário que o programa terminou