import copy

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia_copy1 = contatos.copy()
copia_copy2 = contatos.copy()
print('copia_copy1["guilherme@gmail.com"] = {"nome": "Gui", "telefone": "8888-8888"} # muda totalmente a referência para um dicionário diferente (novo)')
copia_copy1["guilherme@gmail.com"] = {"nome": "Gui", "telefone": "8888-8888"} 
print(copia_copy1["guilherme@gmail.com"])  
print()
print('contatos') 
print(contatos["guilherme@gmail.com"])  
print()

copia_deepcopy = copy.deepcopy(contatos)
copia_deepcopy["guilherme@gmail.com"]["nome"] = "Gui da Manuela" 

print('copia_deepcopy["guilherme@gmail.com"]["nome"] = "Gui da Manuela" #refere-se a um dicionário diferente, então não altera o original')
print(copia_deepcopy["guilherme@gmail.com"])
print()
print('contatos') 
print(contatos["guilherme@gmail.com"])  
print()

copia_copy2["guilherme@gmail.com"]["telefone"] = "2245-1234"     #referência para o mesmo dicionário, então altera o original também

print('copia_copy2["guilherme@gmail.com"]["telefone"] = "2245-1234"     #referência para o mesmo dicionário, então altera o original também')
print(copia_copy2["guilherme@gmail.com"])  
print()

print('contatos #Original também alterado, pois copia_copy2 e contatos referenciam o mesmo dicionário')                                               
print(contatos["guilherme@gmail.com"])  
print()
