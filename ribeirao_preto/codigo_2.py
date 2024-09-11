def verificar(string):
    count_a = string.lower().count('a')
    existe_a = count_a > 0
    return existe_a, count_a

entrada = input("Digite uma string: ")

existe, quantidade = verificar(entrada)

if existe:
    print(f"A letra 'a'/'A' ocorre {quantidade} vezes na string informada.")
else:
    print("A letra 'a'/'A'  não ocorre na string informada.")
