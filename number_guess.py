import random
jogar_novamente = True
while jogar_novamente == True:
    
    numero_aleatorio = random.randint(1,5)
    Numero = int(input("Digite um numero: "))
 
    if Numero == numero_aleatorio:
        print("Voce acertou")
    else:
        print("Voce nao acertou")
        print(f"O numero era:{numero_aleatorio}")

    Escolha1 = ("sim", "sim")
    resposta = input("Deseja tentar novamente? (sim/nao) ")
    if resposta in Escolha1:
         print("Certo")
    else:
        jogar_novamente = False
        print("Obrigado por jogar!") 
