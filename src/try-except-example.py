"""
O Python irá tentar executar o bloco de código definido no try e, caso algum erro seja gerado, o comando except será chamado e seu código executado
"""
try:
    numero = 15 / 0
except:
    print("Divisão por zero não existe")

# Exceções pré-definidas no Python
try:
    numero = 15 / 0
except ZeroDivisionError:
    print("Division by zero does not exist")