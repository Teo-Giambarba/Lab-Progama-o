"""
Usar numpy para realizar analize de dados de uma database csv

"""
import csv
import datetime as dt
import numpy as np


data = np.array([])
#Data,Região,Produto,Quantidade Vendida,Preço Unitário,Valor Total

with open("vendas.csv", newline='') as file:
    reader = csv.reader(file, delimiter=',', quotechar='|')
    start = 0
    for row in reader:
        if start == 0:
            start = 1 #não queremos a primeira linha
            continue
        elif start == 1:
            data = np.hstack((data, row))
            start = 2
            continue
        data = np.vstack((data, row))

valor_total_raw = data[:, 5]
valor_total = np.array([], dtype=float)
for item in valor_total_raw:
    valor_total = np.append(valor_total, float(item))

media = np.mean(valor_total)
mediana = np.median(valor_total)
desvio = np.std(valor_total)
maior_valor = np.max(valor_total)
print(f'Média do valor total: {media}')
print(f'Médiana do valor total: {mediana}')
print(f'Desvio padrão do valor total: {desvio}')
print(f'Maior valor total: {maior_valor}')

qtd_raw = data[:, 3]
qtd = np.array([], dtype=float)
for item in qtd_raw:
    qtd = np.append(qtd, float(item))

maior_qtd = np.max(qtd)
print(f'Maior quantidade de Vendas: {maior_qtd}')

#Mapear cada regiao para um dict com par regiao:index
#Detectar qual regiao certo elemento tem
#Jogar seu valor para um certo index dependendo da regiao
regioes = {}
index = 0
for item in data:
    if item[1] not in regioes:
        regioes[item[1]] = [index, 0]
        index += 1

for item in data:
    regioes[item[1]][1] += float(item[5])

print('Total de vendas por regiao:')
for key in regioes:
    print(f'{key} --- {regioes[key][1]:.2f}')

datas = data[:, 0]
dias_unicos = np.unique(datas)
vendas_por_dia = []

for dia in dias_unicos:
    vendas_dia = qtd[datas == dia]
    vendas_por_dia.append(sum(vendas_dia))

media_vendas_dia = np.mean(vendas_por_dia)
print(f'Média de vendas por dia: {media_vendas_dia:.2f}')

"""
Determinar dia da semana com maior número de vendas

Calcular variação diária no valor total de vendas
"""
#Converter as datas para o formato de data
#Mapear cada dia da semana para um index
#Somar a quantidade de vendas para cada dia
#Determinar o dia com a maior quantidade de vendas

vendas_dia_semana = {}
for item in data:
    dia = (dt.datetime.strptime(item[0], '%Y-%m-%d')).weekday()
    vendas_dia_semana[dia] = vendas_dia_semana.get(dia, 0.0) + float(item[3])

dias_semana = {
    0 : "Segunda",
    1 : "Terça",
    2 : "Quarta",
    3 : "Quinta",
    4 : "Sexta",
    5 : "Sábado",
    6 : "Domingo",
    }

maior_vendas_dia_semana = max(vendas_dia_semana.values())
print(f'Dia da semana com maior quantidade de vendas: {dias_semana[list(vendas_dia_semana.keys())[list(vendas_dia_semana.values()).index(maior_vendas_dia_semana)]]}') # me perdoa por essa abominação

diferença_dias = np.mean(np.diff(qtd, axis=0))

print(f'Variação média de venda dos dias: {diferença_dias:.2f}')
