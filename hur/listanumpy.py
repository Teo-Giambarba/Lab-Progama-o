# 1 | 4 | 5 | 9 | 18 | 19 | 27 | 30

import numpy as np

# 1 - Crie um array NumPy contendo os números de 1 a 10. Em seguida, transforme-o em um array bidimensional com 2 linhas e 5 colunas.
print(f"\n|Exercicio 1|\n")
array = np.arange(0, 10)
array = np.reshape(array, (2, 5)) # Alternativamente array = array.reshape((2, 5))

print(array)

# 4 - Crie um array de 20 números aleatórios entre 0 e 1. Calcule a média, o desvio padrão, o valor máximo e o mínimo desse array.
print(f"\n|Exercicio 4|\n")
array = np.random.ranf(20)
desvio = np.std(array)
media = np.mean(array)
maximo = np.max(array)
minimo = np.min(array)
print(f"{array}\nDesvio = {desvio}\nMédia = {media}\nMinimo, Máximo = {minimo} | {maximo}")

# 5 - Crie uma matriz 4x4 preenchida com números de 1 a 16. Obtenha a transposta dessa matriz e multiplique a matriz original pela transposta
print(f"\n|Exercicio 5|\n")
matriz = np.random.uniform(1, 16, 16).reshape(4,4)
trans_matriz = np.transpose(matriz)
matriz *= trans_matriz
print(matriz)

# 9 - Dado o seguinte array de valores x=[1,2,3,4,5] e y=[2,4,6,8,10], use numpy.interp para estimar os valores de y correspondentes a x=[1.5,2.5,3.5,4.5].


# 18 - 18. Crie um array representando os coeficientes do polinômio p(x) = x^3 - 4x^2 +6x - 24. Use funções do NumPy para calcular:
# a. As raízes do polinômio.
# b. O valor de p(x) para x=2.