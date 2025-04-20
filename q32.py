# 32. Leia um número inteiro (3 dígitos),
#  calcule e escreva a diferença entre o número e seu inverso.

num = int(input('Número de 3 digitos: '))

centena = num // 100
dezena = (num % 100) // 10
unidade = (num % 100) % 10

inverso = unidade * 100 + dezena * 10 + centena
diferença = num - inverso

print(f'O inverso de {num} é {inverso} e {num} - {inverso} = {diferença}')