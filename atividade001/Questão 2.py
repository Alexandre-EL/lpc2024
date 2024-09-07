def palindromo(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

seq = input("Digite uma sequência de caracteres: ")

if palindromo(seq):
    print(f'"{seq}" é um palíndromo.')
else:
    print(f'"{seq}" não é um palíndromo.')