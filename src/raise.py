# Raise é usada para lançar uma exceção manualmente
def calcular_raiz_quadrada(numero):
    if numero < 0:
        raise ValueError("Impossível calcular a raiz quadrada de um número negativo!")
    return numero ** 0.5

try:
    print(calcular_raiz_quadrada(81))
except ValueError as e:
    print(e)

# Criando exceções personalizadas
class ErroPersonalizado(Exception):
    pass

def verificar_valor(valor):
    if valor > 100:
        raise ErroPersonalizado("O valor não pode ser maior que 100!")

try:
    verificar_valor(150)
except ErroPersonalizado as e:
    print(e)

#
colors = ["red", "orange", "yellow", "green", "blue", "indigo","violet"]

def showElement(arr, index):

  if index > len(arr):
    raise IndexError("Attempted to access an index that does not exist!")
  
  return arr[index]
  
try:
    print(showElement(colors, 1))
except IndexError as e:
    print(e)
      
        