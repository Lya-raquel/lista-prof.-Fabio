# 36. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

def main():
    ano = int(input('Quantos anos você tem? '))
    mes = int(input('Quantos mêses? '))
    dias = int(input('Quantos dias? '))

    total_dias_anos = ano * 365
    total_dias_meses = mes * 30
  
    total_dias = total_dias_meses + total_dias_anos + dias

    print(f'A idade de {ano} anos, {mes} meses e {dias} dias é equivalente a {total_dias}')

main()