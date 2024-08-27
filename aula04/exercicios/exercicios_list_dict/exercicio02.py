# 2) Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista_linguagens: list = ["Python", "Java", "C++", "JavaScript"]

list.remove('C++')
list.append('Ruby')

print(list)