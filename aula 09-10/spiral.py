"""
Pegar uma matriz de tamanho e formato variavel e retornar uma lista de todos os seus valores em forma de espiral

Como eu penso em fazer isso:
Estou pensando em criar um progama que percorre a matriz em 2 estados distintos afetados pela sua direção:
Movendo na horizontal - Direita e Esquerda
Movendo na vertical - Cima e Baixo

o progama começa se movendo na horizontal, com a direção de +1, e ao chegar no fim da matriz ele vai mudar sua direção horizontal para -1
ele também vai anotar qual o i da matriz que ele está percorrendo em uma lista, e a sua posição atual.
ao se mover na horizontal com  a direção de +1, ele vai continuar até chegar no final também, e vai mudar sua direção vertical para -1
ele vai anotar o j da matriz que percorreu, e a sua posição atual
então ele vai novamente voltar à percorrer na horizontal, mas com a direção de -1, ou seja vai percorrer ao contrário, até chegar no começo
ele vai anotar o i que está percorrendo, etc etc, e vai depois chegar no começo, vai mudar sua direção para +1 e vai começar a ir na vertical.
ao ir na vertical ele vai anotar o j que está percorrendo, mas aqui ele vai ver que está tentando chegar em um i que já entrou, então ele para e troca de estado

leetcode

o meu codigo FUNCIONA, porem ele não é bem feito, muita repetição de código, seria bom usar uma função auxiliar ali pra melhorar a funcionalidade dele
a funcionalidade meio que de state machine é interessante porém.
"""

def Spiral(matriz: list):
    spiral = []
    height = len(matriz)
    length = len(matriz[0])
    ij = (0, -1) # Como a primeira operação é adicionar +1 em y, começamos
    state = "horizontal"
    direction = +1
    scanned_i = []
    scanned_j = []
    scans = height * length
    print(scans)
    while len(spiral) != scans:
        match state:
            case "horizontal":
                next_ij = (ij[0], ij[1] + direction)
                if next_ij[1] in scanned_j or next_ij[1] >= length or next_ij[1] < 0: # Exit case
                    scanned_i.append(ij[0])
                    print(f"i: {scanned_i}")
                    state = "vertical"
                else:
                    print(next_ij)
                    ij = next_ij
                    spiral.append(matriz[ij[0]][ij[1]])
            case "vertical":
                next_ij = (ij[0] + direction, ij[1])
                if next_ij[0] in scanned_i or next_ij[0] >= height or next_ij[0] < 0: # Exit case
                    scanned_j.append(ij[1])
                    print(f"j: {scanned_j}")
                    state = "horizontal"
                    direction *= -1 # Flips direction
                else:
                    print(next_ij)
                    ij = next_ij
                    spiral.append(matriz[ij[0]][ij[1]])
    print(spiral)

Spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]])