# Checar o primeiro valor, depois o ultimo, se os dois forem iguais, continuar, se não, retornar false
# Aumentar o dedo até chegar no número do meio


# Usando algoritimo fraco

def isPalindrome(number) -> bool:
    if number <= 0:
        return False
    str_number = str(number)
    size = len(str_number)
    if int(str_number[0]) == 0:
        return False
    for i in range(size//2):
        if str_number[i] == str_number[size - i - 1]:
            continue
        return False
    return True

"""
print("-- Teste isPalindrome --")
print(isPalindrome(10))
print(isPalindrome(1))
print(isPalindrome(101))
print(isPalindrome(10011))
print(isPalindrome(10101))
"""

def isPalindromeReverse(number: int) -> bool:
    str_number = str(number)
    if number <= 0:
        return False
    if str_number != str_number[::-1]:
        return False
    return True
"""
print("-- Teste isPalindromeReverse --")
print(isPalindromeReverse(10))
print(isPalindromeReverse(1))
print(isPalindromeReverse(101))
print(isPalindromeReverse(10011))
print(isPalindromeReverse(10101))
print(isPalindromeReverse(-101))
"""
"""
longestPalindrome
a minha idéia atual é: colocar todos os elementos em um dicionário de elementos com chaves igual a os elementos da string, e como par dessas chaves vai estar um array com os indexes
de cada elemento que corresponde a sua chave.
nós percorremos a string inteira achando os elementos, se for um elemento novo, ele é adicionado como chave ao dicionário, e seu index é salvo, se não for ele só é adicionado à 
chave já existente.
após isso tentanmos criar palindromes com cada elemento que tenha mais de uma ocorrência, começando com os elementos de maior distância uns com os outros

ideia mais otimizada do professor: tentar utilizar de passo a passo para cada elemento da lista, de forma que voce cheque i ndividualmente qual deles é palindrome, e slve ele se ele
for maior do que o palindrome atual

ideia gigachad: Manacher's algorithim
"""

def longestPalindrome(string: str) -> str:
    #print(f"-- {string} --")
    longest_match = ""
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            print(j, i)
            target = string[i:j+1]
            print(target)
            if target == target[::-1]:
                if len(target) >= len(longest_match):
                    longest_match = target
                    print("target LOCKED")
    return longest_match

print(longestPalindrome("aba"))
print(longestPalindrome("ab"))
print(longestPalindrome("ababc"))
print(longestPalindrome("cabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabaccabadabac"))

# DESAFIO PARA CASA -> PERMUTATIONS