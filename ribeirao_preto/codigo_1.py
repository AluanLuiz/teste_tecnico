def verif(n):
# Função que verifica se o número pertence a sequencia
    sequencia = seq_fibonacci(n)
    
    if n in sequencia:
        pertence = f"\nO número {n} pertence à sequência de Fibonacci."
        return pertence
    else:
        nao_pertence = f"\nO número {n} NÃO pertence à sequência de Fibonacci."
        return nao_pertence


def seq_fibonacci(n): 
# Função para gerar a sequencia de fibonacci até o numero digitado ou excede-lo.
    seq_fib = [0, 1]
    
    while seq_fib[-1] < n:
        seq_fib.append(seq_fib[-1] + seq_fib[-2])
    
    return seq_fib

print("*** Descrubra se determinado número faz parte da sequência de Fibonacci. ***")
num_input = int(input("Digite o número: "))

resultado = verif(num_input)
print(resultado)