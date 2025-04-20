# 39. Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:
# D = R + S / 2 , onde R = (A + B) ** 2 e S = (B + C) ** 2

def main():
    a = int(input('Pimeiro número: '))
    b = int(input('Segundo número:'))
    c = int(input('Terceiro número: '))

    r = (a + b) ** 2
    s = (b + c) ** 2
    
    d = (r + s) / 2

    print(f'D = {d}')


main()