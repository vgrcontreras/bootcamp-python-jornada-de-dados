# 3) Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livro: dict = {
    'titulo': 'Game of Thrones',
    'autor': 'Test',
    'ano': 2005
}

for key, value in livro.items():
    print(f'{key}:', value)

