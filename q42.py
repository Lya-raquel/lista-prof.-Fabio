# 42. Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano,
#  ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo.

import math

# Função para calcular a distância entre dois pontos
def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)
    return distancia

# Entradas do usuário
x1 = float(input("Digite a coordenada x do primeiro ponto (x1): "))
y1 = float(input("Digite a coordenada y do primeiro ponto (y1): "))
x2 = float(input("Digite a coordenada x do segundo ponto (x2): "))
y2 = float(input("Digite a coordenada y do segundo ponto (y2): "))

distancia = calcular_distancia(x1, y1, x2, y2)

print(f'A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é: {distancia:.2f}')
