# 43. Um sistema de equações lineares do tipo , pode ser resolvido segundo mostrado abaixo
# Escreva um algoritmo que leia os coeficientes a, b, c, d, e e f, 
# calcule e escreva os valores de x e y.

a = int(input('Valor de a: '))
b = int(input('Valor de b: '))
c = int(input('Valor de c: '))
d = int(input('Valor de d: '))
e = int(input('Valor de e: '))
f = int(input('Valor de f: '))

x = (c * e - b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

print(f'x = {x} e y = {y}')