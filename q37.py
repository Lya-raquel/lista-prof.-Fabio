# 37. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

def main():
    idade = int(input('Sua idade expressa em dias: '))

    anos = idade // 365
    meses = (idade % 365) // 30
    dias = (idade % 365) % 30

    print(f'Sua idade é equivalente a {anos} anos, {meses} mêses e {dias} dias')


main()