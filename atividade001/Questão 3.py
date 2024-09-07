import re

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * len(cpf):
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    d1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    d2 = (soma * 10 % 11) % 10
    
    return cpf[-2:] == f"{d1}{d2}"

def main():
    cpf = input("Digite um CPF no formato xxx.xxx.xxx-xx: ")
    
    # Verificar o formato do CPF
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        exit("Esse CPF está fora do formato demandado, ou a pontuação está incorreta :/")
        return
    
    if validar_cpf(cpf):
        print("CPF válido.")
    else:
        exit("CPF inválido :/")

if __name__ == "__main__":
    main()
