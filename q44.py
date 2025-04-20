# 44. Sabendo que latão é constituído de 70% de cobre e 30% de zinco, 
# escreva um algoritmo que calcule a quantidade de cada um desses componentes
#  para se obter certa quantidade de latão (em kg), informada pelo usuário.

quantidade_kg = int(input('Quantidade de latão(kg): '))

qtd_cobre = quantidade_kg * 0.7
qtd_zinco = quantidade_kg * 0.3

print(f'Quantidade em cobre: {qtd_cobre} e quantidade em zinco: {qtd_zinco}')