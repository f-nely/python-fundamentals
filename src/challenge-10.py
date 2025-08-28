"""
Defina um código que lê n pares de valores e retorna a divisão entre eles ou a exceção se isso não for possível
3
1 0
2 $
3 1
"""
n = int(input())

lista = []
for i in range(0,n):
  num1, num2 = input().split()
  try:
    int(num1) / int(num2)
  except ValueError as e:
    print(e)
  except ZeroDivisionError:
    print("Error: Division or modulo by zero occurred")

"""
n = int(input())

for i in range(0, n):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print ("Erro:",e)
    except ValueError as e:
        print ("Erro:",e)
"""
