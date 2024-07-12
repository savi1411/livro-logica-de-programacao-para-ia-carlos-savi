'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Estruturas de Controle
'''

## Exemplo de criação e manipulação de Listas
frutas = ["maçã", "banana", "cereja"] 
primeira_fruta = frutas[0]  # Acessa "maçã" 
frutas.append("laranja") 
print(frutas) 
# saída: ['maçã', 'banana', 'cereja', 'laranja'] 

 # Outros métodos de manipulação de Listas:
frutas.remove("banana") 
frutas.insert(1, "manga") 
ultima_fruta = frutas.pop() 
print(frutas) 
# saída: ['maçã', 'manga', 'cereja']

## Exemplo Completo com Listas

# Criação da lista de compras 
lista_de_compras = ["leite", "ovos", "pão"] 
 
# Adicionando itens à lista 
lista_de_compras.append("queijo") 
lista_de_compras.append("manteiga") 
 
# Removendo um item da lista 
lista_de_compras.remove("ovos") 
 
# Inserindo um item em uma posição específica 
lista_de_compras.insert(1, "frutas") 
 
# Removendo e retornando o último item da lista 
ultimo_item = lista_de_compras.pop() 
 
# Visualizando a lista final 
print("Lista de compras final:", lista_de_compras) 
print("Último item removido:", ultimo_item)

## Criação e Manipulação de Arrays 

# Exemplo de criação de um Array: 
import numpy as np 
meu_array = np.array([1, 2, 3, 4, 5]) 

# Exemplo de métodos de um Array: 
soma = meu_array.sum() 
media = meu_array.mean() 
print("Soma dos elementos do array:", soma) 
print("Média dos elementos do array:", media) 

# Exemplo Completo com Arrays 
# Suponha que você está analisando os resultados de um experimento científico 
#   e precisa calcular algumas estatísticas básicas. 

# Criação do array com os resultados do experimento 
resultados = np.array([23, 19, 31, 27, 25]) 
 
# Calculando a soma dos resultados 
soma_resultados = resultados.sum() 
 
# Calculando a média dos resultados 
media_resultados = resultados.mean() 
 
# Calculando o desvio padrão dos resultados 
desvio_padrao = resultados.std() 
 
# Visualizando os resultados 
print("Soma dos resultados:", soma_resultados) 
print("Média dos resultados:", media_resultados) 
print("Desvio padrão dos resultados:", desvio_padrao) 

## Exemplo de criação de Tupla: 
pontos = (4, 5, 6) 
 
# Exemplo de acesso a uma Tupla: 
primeiro_ponto = pontos[0]  # Acessa 4 
 
# Exemplo Completo com Tuplas 

# Criação de tuplas com coordenadas dos pontos 
ponto_a = (2, 3) 
ponto_b = (5, 7) 
ponto_c = (1, 9) 
 
# Acessando os elementos da tupla 
x_a, y_a = ponto_a 
x_b, y_b = ponto_b 
x_c, y_c = ponto_c 
 
# Visualizando as coordenadas 
print("Coordenadas do ponto A:", ponto_a) 
print("Coordenadas do ponto B:", ponto_b) 
print("Coordenadas do ponto C:", ponto_c) 

## Criação e Manipulação de Dicionários 

# Exemplo de criação de um Dicionário: 
estudante = {"nome": "Carlos", "idade": 21, "curso": "Engenharia"} 
 
# Exemplo de acesso a um Dicionário: 
nome = estudante["nome"]  # Acessa "Carlos" 
 
# Exemplo de manipulação de Dicionário: 
estudante["idade"] = 22 
estudante["nota"] = 9.5 
 
# Para remover um par chave-valor, usamos o método pop(). 
idade = estudante.pop("idade") 
 
## Exemplo Completo com Dicionários 

# Criação do dicionário com informações dos estudantes 
estudante = {"nome": "Carlos", "idade": 21, "curso": "Engenharia"} 
 
# Acessando as informações do dicionário 
nome = estudante["nome"] 
idade = estudante["idade"] 
curso = estudante["curso"] 
 
# Adicionando novas informações ao dicionário 
estudante["nota"] = 9.5 
estudante["ano"] = "3º ano" 
 
# Exemplo de uso de método de Dicionário:
idade_removida = estudante.pop("idade") 
 
# Visualizando o dicionário final e a idade removida 
print("Informações do estudante:", estudante) 
print("Idade removida:", idade_removida)
 
## Exemplo de Uso em IA: Estruturas de Dados

# sistema que classifique e-mails como "Spam" ou "Não Spam" 
#   com base em palavras-chave presentes nos e-mails.

# Palavras-chave e suas classificações 
palavras_chave = { 
    "promoção": "Spam", 
    "desconto": "Spam", 
    "oferta": "Spam", 
    "grátis": "Spam", 
    "urgente": "Spam", 
    "fatura": "Não Spam", 
    "pagamento": "Não Spam", 
    "conta": "Não Spam", 
    "reunião": "Não Spam", 
    "projeto": "Não Spam" 
} 
print(palavras_chave) 

def classificar_email(email, palavras_chave): 
    # Convertendo o e-mail para minúsculas e dividindo em palavras 
    palavras_email = email.lower().split() 
     
    # Contadores para Spam e Não Spam 
    spam_count = 0 
    nao_spam_count = 0 
     
    # Verificando cada palavra no e-mail 
    for palavra in palavras_email: 
        if palavra in palavras_chave: 
            if palavras_chave[palavra] == "Spam": 
                spam_count += 1 
            else: 
                nao_spam_count += 1 
     
    # Classificando o e-mail 
    if spam_count > nao_spam_count: 
        return "Spam" 
    else: 
        return "Não Spam" 
 
# Exemplo de classificação 
email = "Aproveite esta oferta exclusiva com desconto grátis" 
classificacao = classificar_email(email, palavras_chave) 
print(f"O e-mail foi classificado como: {classificacao}") 
 
# Teste com mútiplos emails
emails = [ 
    "Aproveite esta promoção e ganhe um desconto exclusivo", 
    "Sua fatura do cartão está disponível para pagamento", 
    "Reunião do projeto foi agendada para amanhã", 
    "Ofertas imperdíveis de produtos grátis" 
] 
 
for email in emails: 
    classificacao = classificar_email(email, palavras_chave) 
    print(f"E-mail: {email}\nClassificação: {classificacao}\n") 
 