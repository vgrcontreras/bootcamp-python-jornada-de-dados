### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

from faker import Faker

fake = Faker()

i = 1
while i < 20:
    json = {
    'nome': fake.name(),
    'address': fake.address(),
    'text': fake.text(),
    'page': i
}

    print(json)
    
    i += 1

print('não há mais páginas para imprimir')