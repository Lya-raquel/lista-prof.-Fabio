# 1. Leia uma velocidade em m/s, calcule e
# escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

# entrada
velocidade = int(input('Qual velocidade deseja calcular?'))

# processamento 
velocidade_hora = velocidade * 3.6

# saída
print(f'A velocidade {velocidade} m/s equilave a {velocidade_hora} km/h')