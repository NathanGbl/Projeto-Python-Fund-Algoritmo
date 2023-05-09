# Função que adiciona um cliente ao banco
def novo_cliente():
    nome = input('Nome: ').strip() # Linha 2, 3, 4 e 5 solicida dados
    cpf = input('CPF: ').strip()
    tipo_conta = input('Tipo de conta (Comum ou Plus?): ').capitalize().strip()
    saldo = float(input('Valor inicial da conta: R$'))
    senha_usuario = input('Senha: ')
    dados_clientes = {} # Criação do dicionário
    dados_clientes['Nome'] = nome # Linha 9, 10, 11, 12, 13 insere os dados no dicionário
    dados_clientes['CPF'] = cpf
    dados_clientes['Tipo de conta'] = tipo_conta
    dados_clientes['Saldo'] = saldo
    dados_clientes['Senha'] = senha_usuario
    clientes.append(dados_clientes) # Adiciona o dicionário como um elemento da lista clientes

# Função que retira algum cliente do banco
def apagar_cliente():
    cpf_apagar = input('Digite o cpf para apagar a conta: ') # Solicida o cpf que será apagado
    for indice in range(len(clientes)): # Laço itera sobre cada chave 'CPF' dos dicionários e, se achar o cpf, deleta, senão, avisa que o cpf não foi encontrado.
        if cpf_apagar == clientes[indice]['CPF']:
            del clientes[indice]
            break
    else:
        print(f'CPF {cpf_apagar} não encontrado. Tente novamente mais tarde.')

# Função que mostra a lista com clientes
def lista_clientes():
    print('Lista de clientes:')
    for indice in range(len(clientes)): # itera sobre cada dicionário na lista cliente e imprimi o conteúdo do dicionário.
        print(clientes[indice])

# Função que debita um valor            
def debito():
    cpf_debito = input('Digite o CPF da sua conta: ') # Linha 34, 35, 36 solicita dados
    senha_debito = input('Digite sua senha: ')
    valor_debito = float(input('Digite o valor a ser debitado: '))
    for indice in range(len(clientes)): # Itera sobre cada dicionário na lista cliente e verifica os dados recebidos.
        if cpf_debito == clientes[indice]['CPF'] and senha_debito == clientes[indice]['Senha'] and clientes[indice]['Tipo de conta'] == 'Comum':
            clientes[indice]['Saldo'] -= valor_debito * 1.05
            if clientes[indice]['Saldo'] < -1000: # Se os dados estiverem corretos e o saldo ficar menor do que 1000 negativo, o valor é devolvido e o débito é cancelado.
                clientes[indice]['Saldo'] += valor_debito * 1.05
                print('Transação ultrapassou o limite de saldo negativo. Transação cancelada!')
            elif clientes[indice]['Saldo'] >= -1000: # Se os dados estiverem corretos e o saldo ficar acima de 1000 negativo, o débito é realizado
                print(f'Transação realizada com sucesso!\nSaldo: {clientes[indice]["Saldo"]}')
        elif cpf_debito == clientes[indice]['CPF'] and senha_debito == clientes[indice]['Senha'] and clientes[indice]['Tipo de conta'] == 'Plus':
            clientes[indice]['Saldo'] -= valor_debito * 1.03
            if clientes[indice]['Saldo'] < -5000:
                clientes[indice]['Saldo'] += valor_debito * 1.03
                print('Trasação ultrapassou o limite de saldo negativo. Transação cancelada!')
            elif clientes[indice]['Saldo'] >= -5000:
                print(f'Transação realizada com sucesso!\nSaldo: {clientes[indice]["Saldo"]}')

# Função que adiciona um valor na conta do usuario 
def deposito():
    cpf_deposito = input('CPF que você deseja enviar: ')
    senha_deposito = input('Senha: ')
    valor_deposito = float(input('Valor que irá depositar: '))
    for indice in range(len(clientes)): # Itera sobre cada dicionário na lista cliente e verifica os dados recebidos.
        if cpf_deposito == clientes[indice]['CPF'] and senha_deposito == clientes[indice]['Senha']:
            clientes[indice]['Saldo'] += valor_deposito # Se os dados estiverem corretos, o valor é adicionado à conta e o saldo é imprimido na tela.
            print(f'Saldo: {clientes[indice]["Saldo"]:.2f}')

# Função que mostra o extrato da conta bancaria do usuario
def extrato():
    cpf_extrato = float(input('Digite o cpf para retirar o extrato: '))
    senhaextrato = input('Digite a senha: ')
    print(f'Nome: {nome}')
    print(f'CPF: {cpf_extrato}')
    print(f'Conta: {tipo_conta}')
    print(Transferencias)

# Função que faz transferencias 
def transf_contas():
    cpf_origem = input('Digite o CPF da sua conta: ') # Linha 74, 75, 76 e 77 solicita dados.
    senha_origem = input('Digite sua senha: ')
    cpf_final = input('Digite o CPF do destinatário: ')
    valor_transferencia = float(input('Digite o valor a ser debitado: '))
    print()
    for indice in range(len(clientes)): # Verifica se o cpf de origem existe no sistema.
        if cpf_origem == clientes[indice]['CPF'] and senha_origem == clientes[indice]['Senha']:
            break
    else:
        print('Dados incorretos.')
    for indice in range(len(clientes)): # Verifica se o cpf final existe no sistema.
        if cpf_final == clientes[indice]['CPF']:
            break
    else:
        print('Dados incorretos. Tente novamente mais tarde.')
    for indice in range(len(clientes)): # Realiza a retirada do valor da conta do cpf de origem.
        if cpf_origem == clientes[indice]['CPF'] and senha_origem == clientes[indice]['Senha'] and clientes[indice]['Tipo de conta'] == 'Comum':
            clientes[indice]['Saldo'] -= valor_transferencia
            if clientes[indice]['Saldo'] < -1000: # Se o saldo for menor que o permitido, a transação é cancelada
                clientes[indice]['Saldo'] += valor_transferencia
                print('Limite de saldo negativo atingido. Tente novamente mais tarde.')
                break
            else:
                for indice in range(len(clientes)): # Adiciona o valor à conta do cpf final.
                    if cpf_final == clientes[indice]['CPF']:
                        clientes[indice]['Saldo'] += valor_transferencia
                    break
                print(f'Transferência realizada com sucesso!\nSaldo: {clientes[indice]["Saldo"]:.2f}')
                break
        elif cpf_origem == clientes[indice]['CPF'] and senha_origem == clientes[indice]['Senha'] and clientes[indice]['Tipo de conta'] == 'Plus':
            clientes[indice]['Saldo'] -= valor_transferencia
            if clientes[indice]['Saldo'] < -5000: # Se o saldo for menor que o permitido, a transação é cancelada
                clientes[indice]['Saldo'] += valor_transferencia
                print('Limite de saldo negativo atingido. Tente novamente mais tarde.')
                break
            else:
                for indice in range(len(clientes)): # Adiciona o valor à conta do cpf final.
                    if cpf_final == clientes[indice]['CPF']:
                        clientes[indice]['Saldo'] += valor_transferencia
                    break
                print(f'Transferência realizada com sucesso!\nSaldo: {clientes[indice]["Saldo"]:.2f}')
                break
def invest(): # Função que faz operações livres 
    tipo_invest = input('Qual tipo de invstimento você deseja fazer?')
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
    elif entrada == 1: # Chama a função novo_cliente()
        novo_cliente()
        print(clientes)
    elif entrada == 2: # Chama a função apagar_cliente()
        apagar_cliente()
        print(clientes)
    elif entrada == 3: # Chama a função lsita_clientes()
        lista_clientes()
    elif entrada == 4: # Chama a função debito()
        debito()
    elif entrada == 5: # Chama a função deposito()
        deposito()
    elif entrada == 6: # Chama a função extrato()
        extrato()
    elif entrada == 7: # Chama a função tranf_contas()
        transf_contas()
    elif entrada == 8: # Chama a função invest()
        invest()