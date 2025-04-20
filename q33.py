# 33. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.
# (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

num = int(input('Número de 3 digitos: '))

centena = num // 100
dezena = (num % 100) // 10
unidade = (num % 100) % 10

inverso = unidade * 100 + dezena * 10 + centena

soma = num + inverso

print(f'O inverso de {num} é {inverso} e {num} + {inverso} = {soma}')