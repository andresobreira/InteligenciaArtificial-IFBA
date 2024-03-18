def somar(numero_a,numero_b):
    soma = numero_a + numero_b 
    return soma

def somar_e_multiplicar(numero_a,numero_b):
    soma = numero_a + numero_b
    multiplicacao = numero_a * numero_b
    return soma, multiplicacao

def somar_e_imprimir(numero_a,numero_b):
    soma = somar(numero_a,numero_b)
    print(f"O resultado da soma é {soma}")

if __name__ == "__main__":
    resultado = somar(10,5)
    print(f"O resultado da soma é {resultado}")
    somar_e_imprimir(10,20)
    somar_e_multiplicar
    soma, multiplicacao = somar_e_multiplicar(4,6)
    print(f'soma = {soma}')
    print(f'multiplicação = {multiplicacao}')