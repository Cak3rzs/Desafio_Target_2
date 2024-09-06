"2 Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência."

def sequencia(numero_usuario):
    fibonacci, fibonacci2 = 0, 1

    if numero_usuario == 0 or numero_usuario == 1:
        return True

    while fibonacci2 < numero_usuario:
        fibonacci, fibonacci2 = fibonacci2, fibonacci + fibonacci2

    if fibonacci2 == numero_usuario:
        return True
    else:
        return False

numero_usuario = int(input("Digite seu numero: "))

if sequencia(numero_usuario):
    print(f"O {numero_usuario} pertence à sequência Fibonacci!")
else:
    print(f"O {numero_usuario} não pertence à sequência Fibonacci!")