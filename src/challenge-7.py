# Complete o código de forma que seja lido um valor N e seja retornado o seu valor fatorial.

n = int(input())

fat = 1
for i in range(1, n + 1):
  fat *= i
print(fat)



