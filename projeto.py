'''Essa função solicita os dados e adiciona estes em um dicionário
e depois coloca esse dicionário na lista.'''
def novo_cliente(): # Função que adiciona um cliente ao banco
    nome = input("Nome: ")
    cpf = input("CPF: ")
    tipo_conta = input("Tipo de conta (Comum ou Plus?): ")
    valor_inicial_conta = int(input("Valor inicial da conta: R$"))
    senha_usuario = input("Senha: ")
    dados_clientes = {}
    dados_clientes['Nome'] = nome
    dados_clientes['CPF'] = cpf
    dados_clientes['Tipo de conta'] = tipo_conta
    dados_clientes['Valor inicial da conta'] = valor_inicial_conta
    dados_clientes['Senha'] = senha_usuario
    clientes.append(dados_clientes.copy())
    
'''Essa função itera em cada chave CPF comparando o cpf digitado com o que existe na chave.
Se estiver, exclui. Senão, pergunta novamente o cpf para apagar.'''
def apagar_cliente(): # Função que retira algum cliente do banco
    cpf_apagar = input('Digite o cpf para apagar a conta: ')
    for indice in range(len(clientes)):
        if cpf_apagar == clientes[indice]['CPF']:
            del clientes[indice]
            break
    else:
        print(f'CPF {cpf_apagar} não encontrado. Tente novamente mais tarde.')

def lista_clientes(): # Função que mostra a lista com clientes
    for x in range(len(clientes)):
        print("%s" % clientes[x], end=" ")
        print(" ")
    print(" ")
    
def debito(): # Função que debita um valor
    cpf_debito = float(input("Digite o CPF da sua conta: "))
    senha_debito = input('Digite sua senha: ')
    valor_debito = float(input('Digite o valor a ser debitado: '))

def deposito(): # Função que adiciona um valor na conta do usuario 
    cpf_deposito = float(input("CPF que você deseja enviar: "))
    senha_deposito = input("Senha: ")
    valor_deposito = float(input("Valor que irá depositar: "))

def extrato(): # Função que mostra o extrato da conta bancaria do usuario
    cpf_extrato = float(input('Digite o cpf para retirar o extrato: '))
    senhaextrato = input('Digite a senha: ')
    print(f'Nome: {nome}')
    print(f'CPF: {cpf_extrato}')
    print(f'Conta: {tipo_conta}')
    print(Transferencias)

def tranf_contas(): # Função que faz transferencias 
    cpf_transferencia = float(input("Digite o cpf para realizar a transferencia: "))
    senha_transferencia = input('Digite sua senha: ')
    cpf_destino_transferencia = float(input('Digite o cpf do destinatário: '))
    valor_transferecia = float(input('Valor da tranferência: '))

def invest(): # Função que faz operações livres 
    tipo_invest = input("Qual tipo de invstimento você deseja fazer??")
    investimento = float(input('Valor a investir: '))
    tempo_investimento = int(input('Tempo de investimeto em meses: '))

clientes = []

# Menu de navegação do banco
while True:
    print()
    print('[1] Novo cliente') 
    print('[2] Apagar cliente')
    print('[3] Listar clientes')
    print('[4] Débito')
    print('[5] Depósito')
    print('[6] Extrato')
    print('[7] Transferência entre contas')
    print('[8] Investimentos')
    print('[9] Sair')
    entrada = int(input('Escolha uma das opções acima: '))
    print()
    if entrada == 9:
        print("Muito obrigado por ter escolhido nosso banco!")
        break
    elif entrada == 1:
        novo_cliente()
        print(clientes)
    elif entrada == 2:
        print(apagar_cliente())
        print(clientes)
    elif entrada == 3:
        print(lista_clientes())
    elif entrada == 4:
        print(debito())
    elif entrada == 5:
        print(deposito())
    elif entrada == 6:
        print(extrato())
    elif entrada == 7:
        print(tranf_contas())
    elif entrada == 8:
        print(invest()) 

