def calen():

    mesext = {1:"janeiro", 2 :"fevereiro", 3:"março", 4:"abril", 5:"maio", 6:"junho",
    7:"julho", 8:"agosto", 9:"setembro", 10:"outubro", 11:"novembro", 12:"dezembro"}

    dia = int(input("Digite um dia primo: "))
    mes = int(input("Digite um mês primo: "))
    ano = int(input("Digite uma ano primo: "))

    if dia > 31 and mes > 12:
        print("Esse dia não existe no caléndario")
    else:
        print(f"Então sua data é {dia}/{mes}/{ano} e por extenso fica {dia} de {mesext[int(mes)]} de {ano}")

calen()