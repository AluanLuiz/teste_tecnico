def inverter_string(texto):
    # Inicializa uma string vazia para armazenar o resultado
    invertida = ""
    
    # Percorre a string original de trás para frente
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    
    return invertida

# Entrada da string (pode ser modificada ou capturada pelo input)
texto_original = input("Digite uma string para ser invertida: ")

# Inverter a string
texto_invertido = inverter_string(texto_original)

# Exibir o resultado
print(f"String invertida: {texto_invertido}")
