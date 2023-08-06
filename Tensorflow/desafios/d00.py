import tensorflow as tf
from tensorflow import keras
import numpy as np

# Cria um modelo de rede neural com uma camada densa de uma unidade
model = tf.keras.Sequential([
  tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compila o modelo com um otimizador de gradiente descendente estocástico e uma perda de erro quadrático médio
model.compile(optimizer='sgd', loss='mse')

# Treina o modelo em um conjunto de dados de casas com um, dois e três quartos
xs = np.array([1, 2, 3], dtype=float)
ys = np.array([100000, 150000, 200000], dtype=float)
model.fit(xs, ys, epochs=5000)

# Prevê o preço de uma casa com quatro quartos
prediction = model.predict([7])
print(prediction)