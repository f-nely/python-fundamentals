# Assert irá gerar essa exceção a depender de uma condição, ou seja, sempre que a condição definida no assert for falsa, uma exceção será gerada
try:
    numero = 15
    divisor = 0
    assert divisor != 0
except:
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada")

#
def calculate_area(length, width):
  assert length > 0, "Length: positive"
  assert width > 0, "Width: positive"

  return length * width

try:
    print(calculate_area(5, 10))  # Works
    print(calculate_area(-2, 5)) # Raises AssertionError
except:
    print("Length must be positive or Width must be positive")
finally:
    print("Execução finalizada") 
    
