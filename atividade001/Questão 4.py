un_t = ["Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove"]
dec_t = ["", "Dez", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]
sp = ["Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]

n=int(input("Digite um número de 0 até 99: "))

dec = n // 10
un = n % 10

print("\nVocê escolheu:")

if 0 <= n <= 9:
     print(un_t[n])
elif 10 <= n <= 19:
        if n == 10:
            print(dec[1])
        else:
            print(sp[n - 11])
elif 20 <= n <= 99:
    if un == 0:
        print(dec_t[dec])
    else:
        print(f"{dec_t[dec]} e {un_t[un]}.")
else:
    exit("Um Número Invalido :/")