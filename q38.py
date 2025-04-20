# 38. Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações,
#  escrevendo o resultado em forma de fração.

num1= int(input('Numerador da primeira fração: '))
den1= int(input('Denominador da primeira fração: '))
num2= int(input('Numerador da segunda fração: '))
den2= int(input('Denominador da seguanda fração: '))

soma_numerador = (num1 * den2) + (num2 * den1)
denominador = den1 * den2

print(f'A soma {num1}/{den1} + {num2}/{den2} = {soma_numerador}/{denominador}')