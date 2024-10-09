"""
Temos que fazer um progama que vai conseguir calcular o triangulo de pascal e iremos depois imprimir ele
Primeiro temos que calcular o triangulo em questão, que vai ser composto de uma lista de listas onde cada elemento é adicionado no meio da lista,
e se ele tem dois vizinhos na lista anterior o seu valor é a soma desses dois elementos, senão, é um. cada iteração deve calcular um n numero de listas.
começando do triangulo de tamanho 1 e indo até o triangulo de tamanho n.
Devemos separa cade parte desse problema em duas partes, a criação do triangulo, o calculo de seus elementos das linhas e a impressão.

-- Vamos começar calculando os elementos --

Criar Lista de tamanho 0
elemento 0, não tem dois vizinhos, valor = 1
salvar lista
criar lista de tamanho 1
elemento 0, não tem dois vizinhos na antiga, valor = 1
elemento 1, não tem dois vizinhos na antiga, valor = 1
salvar lista
criar lista de tamanho 1
elemento 0, não tem dois vizinhos na antiga, valor = 1
elemento 1, tem dois (0 e 1) vizinhos na antiga, valor = 1 + 1 = 2
elemento 2, não tem dois vizinhos na antiga, valor = 1

    0
   0 1
  0 1 2
 0 1 2 3
0 1 2 3 4

Como definir vizinhos?
pegamos o elemento de index n
se ele for 0, ou len, seu valor = 1.
se não for, pegamos na lista anterior os elementos n-1 e n.

OK, agora temos que colocar isso em uma lista de listas.
em vez de checar a old_list apenas, vamos criar uma list_of_lists e vamos jogar os valores ali, depois vamos acessar usando o i-1 :)

Perfeito!!! agora precisamos só imprimir, eu lembro de ter feito algo parecido em 2018 com um problema onde tinha que imprimir os blocos do mario, acho que até o abrantes passou
algo parecido como lab:
Para cada coluna, adicionaremos uma quantidade de espaços inversamente proporcionais à quantidade de elementos,
após isso, vamos imprimir a linha elemento por elemento com um espaço entre cada elemento < how tho:

criar uma string, e para cada elemento do triangulo, adicionar um elemeneto e um espaço pra essa string ehehehe
adicionar espaços inversamente proporcional à o i da linha.

possivelmente eu podia fazer isso diretamente no for principal, mas dessa maneira tem duas partes diferentees
"""

def PascalTriangle(height: int):
    list_of_lists = []
    for i in range(height):
        new_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                new_list.append(1)
            else:
                new_list.append(list_of_lists[i - 1][j-1] + list_of_lists[i - 1][j])
        list_of_lists.append(new_list)
    for row_n in range(len(list_of_lists)):
        string = ""
        for element in list_of_lists[row_n]:
            string += f" {element}"
        print((" " * (height - row_n)) + string)
    return list_of_lists

PascalTriangle(20)