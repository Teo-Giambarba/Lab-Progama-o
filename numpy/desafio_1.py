"""

1. Crie um array NumPy com trinta valores aleatorios entre 15 e 35 graus Celsius que representam temperaturas médias diárias ao longo do mês.
DONE

2. Calcule a média mensal.
DONE

3. Identifique a temperatura mais alta e a mais baixa.
DONE

4. Calcule a mediana do mes. (número central da lista, ordenada)
DONE

5. Apresenta uma lista com todas as ocorrências de temperaturas iguais ou superiores a 30.
DONE

6. Converta todas as temperaturas para Fahrenheit. (Em um novo array)
DONE

7. Divida o array em 4 semanas.
DONE~ish? DONE

8. Desenhe os gráficos diários e um gráfico de barras semanal.


"""
import numpy as np
import matplotlib.pyplot as mpl

#1
print("-CRIAR ARRAY-")
temperaturas = np.random.randint(15, 35 + 1, (30))
print(temperaturas)




#2 MEDIA MENSAL
print("-MEDIA MENSAL-")
sum = 0
for i in range(len(temperaturas)):
    sum += temperaturas[i]
print(sum/len(temperaturas))

# or

print(temperaturas.mean())




#3
print("-LOW / HIGH-")
highest = temperaturas[0]
lowest = temperaturas[0]
for i in range(1, len(temperaturas)):
    if temperaturas[i] > highest:
        highest = temperaturas[i]
    elif temperaturas[i] < lowest:
        lowest = temperaturas[i]
print(lowest, highest)

# or

print(np.min(temperaturas), np.max(temperaturas))




#4
print("-MEDIANA-")
sorted_arr = sorted(temperaturas)
if len(temperaturas) % 2 == 1:
    print(sorted_arr[int(len(sorted_arr)/2)])
print((sorted_arr[int(len(sorted_arr)/2)] + sorted_arr[int((len(sorted_arr) - 1)/2)])/2)

#or

print(np.median(np.sort(temperaturas)))




#5
print("-MAIOR OU IGAL A 30-")
higher_than_30 = []
for i in range(len(temperaturas)):
    if temperaturas[i] >= 30:
        higher_than_30.append(temperaturas[i])
print(higher_than_30)

# or

print(temperaturas[temperaturas >= 30])




#6 CONVERTE P FAHRENHEIT EM UM NOVO ARR
print("-FAHRENHEIT-")
# F = (C * 9 / 5) + 32
fahrenheit = []
for i in range(len(temperaturas)):
    fahrenheit.append((temperaturas[i] * 1.8) + 32)
print(fahrenheit)

# or 
fahrenheit = []
for element in np.nditer(temperaturas):
    fahrenheit.append((element * 1.8) + 32)


print(fahrenheit)
# or 
fahrenheit = np.copy(temperaturas) * 1.8 + 32

print(fahrenheit)




#7 DIVIDA O ARRAY EM 4 SEMANAS
print("-DIVIDIR EM 4 ARRAYS-")

temp_semanas = np.array_split(temperaturas, 4)
print(temp_semanas)





#8 IMPRIMIR O GRAFICO DAS TEMPERATURAS
medias_semanais = np.array([np.mean(semana) for semana in temp_semanas])

mpl.plot(temperaturas, marker="o")
mpl.title("Temperaturas Diárias no Mês")
mpl.xlabel("Dia")
mpl.ylabel("Temperatura (°C)")
mpl.show()

cores = ['skyblue', 'salmon', 'lightgreen', 'gold']
mpl.bar(list(range(1, 5)), medias_semanais, color = cores)
mpl.title("Médias Semanais no Mês")
mpl.xlabel("Semana")
mpl.ylabel("Temperatura (°C)")
mpl.xticks(list(range(1, 5)), ["Semana 1", "Semana 2", 'Semana 3', 'Semana 4'])
mpl.show()