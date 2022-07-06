def contalizador(n):
    return len( str(n) )
def dig():
    num = int(input("Digite um número primo e irei dizer quantos dígitos ele tem: "))
    print(contalizador(num), "dígitos")
    
dig()