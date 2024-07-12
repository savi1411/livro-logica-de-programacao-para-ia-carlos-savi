'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Bibliotecas Essenciais para IA com Python
'''

## Biblioteca NumPy 

# Operações Básicas com Arrays
import numpy as np 
 
# Criando um array 
arr = np.array([1, 2, 3, 4, 5]) 
 
# Operações básicas 
soma = np.sum(arr) 
media = np.mean(arr) 
produto = np.prod(arr) 
 
print("Array:", arr) 
print("Soma:", soma) 
print("Média:", media) 
print("Produto:", produto) 

## Biblioteca Pandas

# Manipulação de dados com DataFrames
import pandas as pd 
 
# Criando um DataFrame 
dados = { 
    'Produto': ['Produto A', 'Produto B', 'Produto C'], 
    'Vendas': [100, 150, 200], 
    'Lucro': [30, 50, 70] 
} 
df = pd.DataFrame(dados) 
 
# Operações básicas 
total_vendas = df['Vendas'].sum() 
media_lucro = df['Lucro'].mean() 
 
print("DataFrame:\n", df) 
print("Total de Vendas:", total_vendas) 
print("Média de Lucro:", media_lucro) 

## Biblioteca Matplotlib
import matplotlib.pyplot as plt 
 
# Dados de vendas 
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'] 
vendas = [100, 120, 130, 115, 140] 
 
# Criando o gráfico 
plt.plot(meses, vendas) 
plt.xlabel('Meses') 
plt.ylabel('Vendas') 
plt.title('Vendas ao longo dos meses') 
plt.show() 

## Biblioteca Scikit-learn
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score 
 
# Carregando o dataset Iris 
iris = load_iris() 
X = iris.data 
y = iris.target 
 
# Dividindo os dados em treino e teste 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 
 
# Treinando o modelo KNN 
knn = KNeighborsClassifier(n_neighbors=3) 
knn.fit(X_train, y_train) 
 
# Fazendo previsões 
y_pred = knn.predict(X_test) 
 
# Calculando a acurácia 
acuracia = accuracy_score(y_test, y_pred) 
print("Acurácia do modelo KNN:", acuracia) 

## Biblioteca TensorFlow
import tensorflow as tf 
from tensorflow.keras.datasets import mnist 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, Flatten 
from tensorflow.keras.utils import to_categorical 
 
# Carregando o dataset MNIST 
(X_train, y_train), (X_test, y_test) = mnist.load_data() 
X_train, X_test = X_train / 255.0, X_test / 255.0 
y_train, y_test = to_categorical(y_train), to_categorical(y_test) 
 
# Criando o modelo 
model = Sequential([ 
    Flatten(input_shape=(28, 28)), 
    Dense(128, activation='relu'), 
    Dense(10, activation='softmax') 
]) 
 
# Compilando o modelo 
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) 
 
# Treinando o modelo 
model.fit(X_train, y_train, epochs=5, batch_size=32) 
 
# Avaliando o modelo 
loss, accuracy = model.evaluate(X_test, y_test) 
print("Acurácia do modelo:", accuracy)

## Biblioteca Keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D 
 
# Ajustando os dados para o formato necessário pela CNN 
X_train = X_train.reshape(-1, 28, 28, 1) 
X_test = X_test.reshape(-1, 28, 28, 1) 
 
# Criando o modelo 
model = Sequential([ 
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)), 
    MaxPooling2D((2, 2)), 
    Flatten(), 
    Dense(128, activation='relu'), 
    Dense(10, activation='softmax') 
]) 
 
# Compilando o modelo 
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) 

# Treinando o modelo 
model.fit(X_train, y_train, epochs=5, batch_size=32) 
 
# Avaliando o modelo 
loss, accuracy = model.evaluate(X_test, y_test) 
print("Acurácia do modelo:", accuracy) 

## Biblioteca NLTK (Natural Language Toolkit)

# Instalação e Importação 
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

# Carrega o léxico de sentimentos
nltk.download('vader_lexicon') 

# Inicializando o analisador de sentimentos 
sid = SentimentIntensityAnalyzer() 

# Textos de exemplo 
textos = [
    "I love this product, it is amazing!",
    "The service was terrible and I do not recommend it.",
    "It is an average item, nothing special."
]

# Análise de sentimentos 
for texto in textos: 
    print(f"Texto: {texto}") 
    ss = sid.polarity_scores(texto) 
    for k in ss: 
        print(f"{k}: {ss[k]}") 
    print()
