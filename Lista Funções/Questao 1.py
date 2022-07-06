def maneiro(a, b):
    if a > b:
        print(f"{a} é maior que {b}")
    elif b > a:
        print(f"{b} é maior que {a}")
    else:
        print("Números Iguais")

a1 = int(input("Digite um número: "))
a2 = int(input("Digite outro número: "))
maneiro(a1, a2)