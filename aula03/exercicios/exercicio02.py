# 2) Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de 
# temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperatura = 27

if temperatura < 18:
    print('A temperatura está baixa')
elif temperatura >= 18 and temperatura <= 26:
    print('A temperatura é media')
elif temperatura > 26:
    print('A temperatura está alta')