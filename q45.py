# 45. Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para
# decidir o numero de notas de cada valor que deve ser disponibilizado para o cliente que realizou o
# saque. Um possível critério seria o da "distribuição ótima" no sentido de que as notas de menor valor
# disponíveis fossem distribuídas em número mínimo possível. Por exemplo, se a maquina só dispõe de
# notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo deveria
# indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um
# algoritmo que receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o
# critério da distribuição ótima.

print('-' * 30)
print('CAIXA ELETRÔNICO')
print('-' * 30)
print('Notas de: ')
print(' R$ 50,00')
print(' R$ 10,00')
print(' R$ 5,00')
print(' R$ 1,00')

valor = int(input('Valor da quantia(R$): '))

notas50 = valor // 50
notas10 = (valor % 50) // 10
notas5 = (valor % 10) // 5
notas1 = (valor % 5) 

print('Notas a receber:')
print(f'{notas50} de R$ 50,00')
print(f'{notas10} de R$ 10,00')
print(f'{notas5} de R$ 5,00')
print(f'{notas1} de R$ 1,00')

