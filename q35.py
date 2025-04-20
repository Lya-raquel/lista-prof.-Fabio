# 35. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem.
#  Ex.: número = 9534 ; soma = 9+5+3+4 = 21.

#num = int(input('Número de 4 digitos:'))

def main ():

    num = int(input('Número de 4 digitos: '))
    milhar = num // 1000
    centena = (num % 1000) // 100
    dezena = (num % 100) // 10
    unidade = (num % 100) % 10

    soma = milhar + centena + dezena + unidade

    print(f'A soma dos elementos de {num} é {soma} ')


main()