menu = """

[1] = Depositar
[2] = Sacar
[3] = Extrato
[0] = Sair

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 3

while True:

    opcao = input(menu)
    if opcao == "1":
        n = int(input("digite o valor a depositar: "))
        if n > 0:
            saldo += n
            print('deposito')
        else:
            print("não foi possivel efetuar a operação")
    
    elif opcao == "2":
        if numero_saques != 0 :
            n = int(input('Digite o valor a sacar'))
            if n >500 and n<0:
                print('o valor informado n foi permitido')
            else:
                if saldo > n:
                    saldo -= n
                    print("operação efetuada")
                    numero_saques -= 1
                else:
                    print('saldo insuficiente')

        else:
            print("limite de saques batido")
            

    elif opcao == "3":
        print(saldo)
    
    else:
        break