"""
Dado um número inteiro N, complete o código abaixo para que seja exibido a tabuada do valor, seguindo o formato
"""

N = int(input())

for i in range(1, 11):
  print(f"{N} x {i} = {i * N}")


""" N = int(input())

for i in range(1, 11):
    print("{} x {} = {}".format(N, i, N * i)) """

