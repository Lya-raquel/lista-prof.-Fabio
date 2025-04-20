valor = float(input('Valor do bem R$ :'))

# Processamento
parcela = valor // 3
# entrada = valor_bem - parcela - parcela
entrada = (valor % 3) + parcela

# Saída
print('> Parcelamento: ')
print(f'>> Entrada R$: {entrada:.2f}')
print(f'>> + 2x de R$: {parcela:.2f}')
print('---------------------------')