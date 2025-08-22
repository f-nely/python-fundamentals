numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número menor que 20: "))
    soma = soma + numero
else:
    print("loop encerrado com sucesso")
print(soma)