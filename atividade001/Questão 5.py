import random

def escolher_palavra():
    with open('palavras.txt', 'r') as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

def exibir_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    
    while tentativas > 0:
        print(f"\nA palavra é: {exibir_palavra(palavra, letras_corretas)}")
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_corretas.add(letra)
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            letras_erradas.add(letra)
            tentativas -= 1
            print(f"-> Você errou pela {6 - tentativas}ª vez. Tente de novo!")

        if all(letra in letras_corretas for letra in palavra):
            print(f"\nParabéns! Você adivinhou a palavra: {palavra}")
            break
    else:
        print(f"\nVocê foi enforcado! A palavra era: {palavra}")

if __name__ == "__main__":
    jogo_da_forca()