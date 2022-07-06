def maneiro(a, b):
    if a > 10 and b > 10:
        print(f"{a} e {b} sao maiores que 10")
    elif a > 10:
        print(f"{a} é maior que 10")
    elif b > 10 and a < 10:
        print(f"{b} é maior que 10")
    else:
        print("Nenhum número excede o limite 10")


print("O limite é 10!")

a1 = int(input("Digite um número: "))

a2 = int(input("Digite outro número: "))
maneiro(a1, a2)