'''lista = {'João', 'Maria', 'Pedro'}
lista = dict() cria um dicionário vazio'''
lista = {'nome': 'Pedro', 'idade': 25,}
'''print(lista['nome'])
print(lista['idade'])                                                             


print("==" * 20)                                                          
print(f"{lista['nome']} tem {lista['idade']} anos.")
print("==" * 20)     

lista['sexo'] = 'M'  # Adiciona um novo par chave-valor ao dicionário
print(lista)

print("==" * 20)
del lista['idade']  # Remove o par chave-valor com a chave 'idade'
print(lista)

print("==" * 20)

filme = {'nome do filme': 'Veloses e Furiosos', 
         'Ano': 2001, 
         'Diretor': ' Rob Cohen'}

print(f"O filme {filme['nome do filme']} foi lançado em {filme['Ano']} e dirigido por {filme['Diretor']}.")

print(filme.values())  # Exibe todos os valores do dicionário
print(filme.keys())    # Exibe todas as chaves do dicionário
print(filme.items())   # Exibe todos os pares chave-valor do dicionário

print("==" * 20)
for k, v in filme.items():
    print(f"O {k} é {v}")

print("==" * 20)

pessoas = {'nome': 'Ana', 'idade': 30, 'sexo': 'F'}
#print(pessoas[0]) # Isso causará um erro, pois dicionários não suportam indexação por posição
print(f'O {pessoas['nome']} tem {pessoas["idade"]} anos')  # Acessa o valor associado à chave 'nome'

print("==" * 20)    

del pessoas['sexo']  # Remove o par chave-valor com a chave 'sexo'

pessoas['nome'] = 'Maria'  # Atualiza o valor associado à chave 'nome'
pessoas['idade'] = 28      # Atualiza o valor associado à chave 'idade'
print(pessoas)  # Exibe o dicionário atualizado

pessoas['peso'] = 65.5  # Adiciona um novo par chave-valor ao dicionário
print(pessoas)  # Exibe o dicionário atualizado
 
brasil =[]
estados1 = {'nome': 'São Paulo', 'sigla': 'SP'}
estados2 = {'nome': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estados1)
brasil.append(estados2)
print(brasil)
print(brasil[0])  # Acessa o nome do primeiro estado na lista
print(brasil[1]["nome"])  # Acessa a sigla do segundo estado na lista


print("==" * 20)    


materia = dict()
curso = list()

for c in range (0,3):
    materia['sigla'] = str(input("Digite a Sigla da Matéria: "))
    materia["nome"] = str(input("Digite o nome da Matéria: "))
    curso.append(materia.copy())
print(curso)

for m in curso:
    for k, v , in m.items():
        print(f"O Campo {k} tem valor {v}")

lista = []
dic=dict()

nome = input("Digite: ")

idade = int(input("Digite idade: "))

lista.append(nome)
lista.append(idade)
print("==" * 20)  

dic = {"nome": lista[0], "idade": lista[1]}
print(lista)
print(dic["nome"])
'''

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005},
     'DS5': {'km': 17000, 'ano': 2015},
     'Fusca': {'km': 130000, 'ano': 1979}, 'Jetta': {'km': 56000, 'ano': 2011},
    'Passat': {'km': 62000, 'ano': 1999 }
    }

for item in dados.items():
    print(item)
for item in dados.items():
    print(item[1]['ano'])