# 41. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
# distribuidor e dos impostos (aplicados ao custo de fábrica). 
# Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%,
#  escreva um algoritmo que leia o custo de fábrica de um carro  escreva o custo ao consumidor.

custo_fabrica = float(input('Digite o custo de fábrica do carro: '))

apl_distribuidor = 0.28 * custo_fabrica
apl_imposto = 0.45 * custo_fabrica
custo_final = custo_fabrica + apl_distribuidor + apl_imposto

print(f'O custo total do consumidor é de R${custo_final:.2f}')