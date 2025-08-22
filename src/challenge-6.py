"""
Dado um valor inteiro N, complete o código abaixo de acordo com as condições:

Se N for ímpar, exiba no console: "Estranho";
Se N for par e for menor que 10, exiba no console: "Não é estranho";
Se N for par e estiver entre 10 e 20, exiba no console: "Estranho";
Se N for par e for maior que 20, exiba no console: "Não é estranho".
"""

n = int(input())

if (n % 2 != 0):
  print("Estranho")
elif (n % 2 == 0 and n < 10):
  print("Não é estranho")
elif (n % 2 == 0 and (n >= 10 and n <= 20)):
  print("Estranho")
elif (n % 2 == 0 and n > 20):
  print("Não é estranho")

"""
n = int(input())
        
if(n % 2 != 0):
    print("Estranho")
else:
    if(n < 10):
        print("Não é estranho")
    elif(n >= 10 and n <= 20):
        print("Estranho")
    else:
        print("Não é estranho")
"""

