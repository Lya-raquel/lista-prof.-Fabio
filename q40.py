# 40. Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada:
#  o número de anos que ele fuma, o n de cigarros fumados por dia 
# e o preço de uma carteira (1 carteira tem 20 cigarros).

anos = int(input('Quantos anos você fuma? '))
cigarros_dias = int(input('Quantos cigarros você fuma por dia? '))
preço = int(input('Qual o preço de uma carteira? '))

valor_por_cigarro = preço / 20
gasto_dia = valor_por_cigarro * cigarros_dias
gasto_total = (anos * 365) * gasto_dia

print(f'A quantidade de dinheiro que você já gastou é de {gasto_total} em {anos} anos')
