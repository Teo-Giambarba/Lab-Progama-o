"""
IRIS DATASET

SETOSA, VERSICOLOUR, VIRGINICA - tipos de familias da planta

pegar o conjunto de numeros e reconhecer qual é a familia.

Faça uma normalização dos dados:
padronize em uma escala de 0 a 1

usando numpy

trasnformar o dataset para que suas colunas tenham média 0 e desvio padrão 1 (menor -1, maior 1, média 0)

Padronização é valor menos media dividido pelo desvio padrão (em cada elemento da coluna)
"""

import numpy as np
from sklearn.datasets import load_iris

iris_ds = load_iris()

data = iris_ds.data

targets = iris_ds.target

print(data)
print(targets)