def amigo(text,letra):
   cont = 0
   for i in text:
       if i == letra:
           cont += 1
   return (f"Existe {cont} letra ou números {letra} no seu texto")
     


text = str(input("Digite o texto: "))
letra = str(input("Digite a letra ou o número que você quer ver: "))

print(amigo(text,letra))