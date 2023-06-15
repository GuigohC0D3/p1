numero = int(input('Digite um numero: '))
fatorial = 1

for x in range(1, numero + 1):
    fatorial *= x
        
print('O fatorial do numero {} é: {}'.format(numero, fatorial))