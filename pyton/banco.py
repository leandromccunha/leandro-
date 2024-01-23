from tarfile import ExtractError
import textwrap

def menu():
    menu = """\n
                MENU
    [d]\t  Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova Conta
    [lc]\t Listar Contas
    [nu]\t Novo Usuário
    [q]\t Sair
    """
    return input(textwrap.dedent(menu))

def depositar (saldo,valor,extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR${valor:.2f}\n"
        print("\n deposito realizado")
    else:
        print("\n DEPOSITO N REALIZADO")
    return saldo , extrato

def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    ex_saldo = valor > saldo
    ex_limite = valor > limite
    ex_saques = numero_saques >= limite_saques
    
    if ex_saldo:
        print ('falhou n tem saldo')
    elif ex_limite:
        print (' falhou n tem limite')
    elif ex_saques:
        print ('falhou m ppossui mais saques')

    elif valor> 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques +=1
        print ("sacado")
    else:
        print("o valor informado e invalido")

    return saldo , extrato

def exibir_extrato(saldo,/,*,extrato):

    print ('nao form realiszafas movimentaçoes' if not extrato else extrato)
    print(saldo)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento : ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(" Usuário não encontrado, fluxo de criação de conta encerrado! ")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 'd':
            valor = float(input('informe o valor do deposito: '))
            saldo , extato = depositar(saldo,valor,extrato)
        
        elif opcao == 's':
            valor = float(input('informe o valor de saque:'))
            saldo , extrato = sacar(

                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato = extrato)
        elif opcao =='nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)

            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao =="q":
            break
main()