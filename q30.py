# 30. Leia um número inteiro de minutos, calcule e escreva quantos dias,
# quantas horas e quantos minutos ele corresponde.

min = int(input('Minutos: '))

dias = min // 1440
horas = min // 60
minutos = min % 60

print(f'{min} são {dias} dias, {horas} horas e {minutos} minutos')