# 31. Leia um número inteiro (4 dígitos binários),
#  calcule e escreva o equivalente na base decimal.

# Função para converter um número binário de 4 dígitos para decimal
def binario_para_decimal(binario):
    # Verifica se o número binário tem 4 dígitos
    if len(binario) != 4 or not all(digito in '01' for digito in binario):
        return "Erro: O número deve ter exatamente 4 dígitos binários (0 ou 1)."
    
    # Converte o número binário para decimal
    decimal = int(binario, 2)
    return decimal

# Lê um número binário do usuário
numero_binario = input("Digite um número binário de 4 dígitos: ")

# Chama a função e imprime o resultado
resultado = binario_para_decimal(numero_binario)
print(f"O equivalente decimal de {numero_binario} é: {resultado}")