def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("depósito concluído")
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(*,limite_saques, saldo, valor_saque, numero_saques, limite, extrato):
    if numero_saques >= limite_saques:
        print("Limite de saques diários excedido!")
    elif valor_saque > saldo:
        print("Saldo insuficiente!")
    elif valor_saque > limite:
        print("Valor do saque excedeu o limite!")
    elif valor_saque <= 0:
        print("Valor de saque inválido!")
    elif valor_saque > 0:
        saldo -= valor_saque
        numero_saques += 1
        extrato.append(f"Saque: R$ {valor_saque:.2f}")
        print("Saque realizado com sucesso")
    return saldo, numero_saques, extrato

def gerar_extrato(extrato, saldo):
    print("************* Extrato *************")
    [print(operacao) for operacao in extrato]
    if extrato == []:
        print("Não foram realizadas movimentações")
    print (f"\nSaldo Atual R$: {saldo}")
    print("Obrigado por utilizar nossos serviços!!!")
    print("\n***********************************")

def mostrar_saldo(saldo):
    return(print(f"Seu saldo atual é: R$ {saldo}"))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuario com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = ("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (logradouro, nro - bairro -cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("*** Usuário criado com sucesso!!! ***")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("*** Conta criada com sucesso ***")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuario nao encontardo, fluxo de criacao de conta encerrado")

def main():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Consultar Saldo
    [5] Criar novo usuario
    [6] Criar nova conta
    [0] Sair

    => """

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = input(menu)
        if opcao == "1":
            valor_deposito = input("Digite o valor do depósito")
            saldo, extrato = depositar(float(valor_deposito), saldo, extrato)

        if opcao == "2":
            valor_saque = input("Digite o valor do saque")
            saldo, numero_saques, extrato = sacar(
                                        limite_saques = LIMITE_SAQUES, 
                                        saldo = saldo, 
                                        valor_saque = float(valor_saque), 
                                        numero_saques = numero_saques, 
                                        limite = limite,
                                        extrato = extrato
                                    )

        if opcao == "3":
            gerar_extrato(extrato, saldo)

        if opcao == "4":
            mostrar_saldo(saldo)  

        if opcao == "5":
            criar_usuario(usuarios) 

        if opcao == "6":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta) 

        if opcao == "0":
            break

main()
