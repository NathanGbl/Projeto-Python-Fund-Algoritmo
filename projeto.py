from datetime import datetime, date
# Função que adiciona um cliente ao banco
def novo_cliente():
    print()
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
    dados_clientes['Extrato'] = []
    dados_clientes['Investimentos'] = []
    clientes.append(dados_clientes) # Adiciona o dicionário como um elemento da lista clientes

# Função que retira algum cliente do banco
def apagar_cliente():
    print()
    cpf_apagar = input('Digite o cpf para apagar a conta: ') # Solicida o cpf que será apagado
    for indice in range(len(clientes)): # Laço itera sobre cada chave 'CPF' dos dicionários e, se achar o cpf, deleta, senão, avisa que o cpf não foi encontrado.
        if cpf_apagar == clientes[indice]['CPF']:
            del clientes[indice]
            break
    else:
        print(f'CPF {cpf_apagar} não encontrado. Tente novamente mais tarde.')

# Função que mostra a lista com clientes
def lista_clientes():
    print()
    print('Lista de clientes:')
    for indice in range(len(clientes)): # itera sobre cada dicionário na lista cliente e imprimi o conteúdo do dicionário.
        print(clientes[indice])

# Função que debita um valor            
def debito():
    print()
    cpf_debito = input('Digite o CPF da sua conta: ') # Linha 34, 35, 36 solicita dados
    senha_debito = input('Digite sua senha: ')
    valor_debito = float(input('Digite o valor a ser debitado: '))
    for indice in range(len(clientes)): # Itera sobre cada dicionário na lista cliente e verifica os dados recebidos.
        if cpf_debito == clientes[indice]['CPF'] and senha_debito == clientes[indice]['Senha'] and clientes[indice]['Tipo de conta'] == 'Comum':
            if clientes[indice]['Saldo'] - valor_debito * 1.05 < -1000: # Se os dados estiverem corretos e o saldo ficar menor do que 1000 negativo, o valor é devolvido e o débito é cancelado.
                print('Transação ultrapassou o limite de saldo negativo. Transação cancelada!')
                break
            elif clientes[indice]['Saldo'] - valor_debito * 1.05 >= -1000: # Se os dados estiverem corretos e o saldo ficar acima de 1000 negativo, o débito é realizado
                clientes[indice]['Saldo'] -= valor_debito * 1.05
                tarifa = valor_debito * 1.05 - valor_debito
                hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S')
                clientes[indice]['Extrato'].append(f'{hora_formatada}   - {valor_debito}   Tarifa: {tarifa}   Saldo: {clientes[indice]["Saldo"]:.2f}') # Adiciona a string formatada para a lista Extrato
                print(f'Débito realizado com sucesso!\nSaldo: {clientes[indice]["Saldo"]}')
        elif cpf_debito == clientes[indice]['CPF'] and senha_debito == clientes[indice]['Senha'] and clientes[indice]['Tipo de conta'] == 'Plus':
            if clientes[indice]['Saldo'] - valor_debito * 1.03 < -5000:
                print('Trasação ultrapassou o limite de saldo negativo. Transação cancelada!')
                break
            elif clientes[indice]['Saldo'] >= -5000:
                clientes[indice]['Saldo'] -= valor_debito * 1.03
                tarifa = valor_debito * 1.03 - valor_debito
                hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S')
                clientes[indice]['Extrato'].append(f'{hora_formatada}   - {valor_debito}   Tarifa: {tarifa}   Saldo: {clientes[indice]["Saldo"]:.2f}') # Adiciona a string formatada para a lista Extrato
                print(f'Transação realizada com sucesso!\nSaldo: {clientes[indice]["Saldo"]}')

# Função que adiciona um valor na conta do usuario 
def deposito():
    print()
    cpf_deposito = input('CPF que você deseja enviar: ')
    senha_deposito = input('Senha: ')
    valor_deposito = float(input('Valor que irá depositar: '))
    for indice in range(len(clientes)): # Itera sobre cada dicionário na lista cliente e verifica os dados recebidos.
        if cpf_deposito == clientes[indice]['CPF'] and senha_deposito == clientes[indice]['Senha']:
            clientes[indice]['Saldo'] += valor_deposito # Se os dados estiverem corretos, o valor é adicionado à conta e o saldo é imprimido na tela.
            hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S')
            clientes[indice]['Extrato'].append(f'{hora_formatada}   + {valor_deposito}   Tarifa: 0.00   Saldo: {clientes[indice]["Saldo"]:.2f}')
            print(f'Saldo: {clientes[indice]["Saldo"]:.2f}')

# Função que mostra o extrato da conta bancaria do usuario
def extrato():
    print()
    cpf_extrato = input('Digite o cpf para retirar o extrato: ')
    senhaextrato = input('Digite a senha: ')
    print()
    for indice in range(len(clientes)): # Itera sobre cada dicionário
        if cpf_extrato == clientes[indice]['CPF'] and senhaextrato == clientes[indice]['Senha']: # Verifica os dados
            print(f'Nome: {clientes[indice]["Nome"]}')
            print(f'CPF: {clientes[indice]["CPF"]}')
            print(f'Conta: {clientes[indice]["Tipo de conta"]}')
            for index in range(len(clientes[indice]['Extrato'])): # Itera sobre cada elemento da lista que está na chave Extrato e imprimi.
                print(f'Data: {clientes[indice]["Extrato"][index]}') # Cada elemento da lista Extrato é uma string formatada

# Função que faz transferencias 
def transf_contas():
    print()
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
            if clientes[indice]['Saldo'] - valor_transferencia < -1000: # Se o saldo for menor que o permitido, a transação é cancelada
                print('Limite de saldo negativo atingido. Tente novamente mais tarde.')
                break
            else:
                clientes[indice]['Saldo'] -= valor_transferencia
                hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S') # Hora da transação
                clientes[indice]['Extrato'].append(f'{hora_formatada}   - {valor_transferencia}   Tarifa: 0.00   Saldo: {clientes[indice]["Saldo"]:.2f}') # Adiciona a string formatada para a lista Extrato
                for index in range(len(clientes)): # Adiciona o valor à conta do cpf final.
                    if cpf_final == clientes[index]['CPF']:
                        clientes[index]['Saldo'] += valor_transferencia
                        hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S')
                        clientes[index]['Extrato'].append(f'{hora_formatada}   + {valor_transferencia}   Tarifa: 0.00   Saldo: {clientes[index]["Saldo"]:.2f}')
                print(f'Transferência realizada com sucesso!\nSaldo: {clientes[indice]["Saldo"]:.2f}')
                break
        elif cpf_origem == clientes[indice]['CPF'] and senha_origem == clientes[indice]['Senha'] and clientes[indice]['Tipo de conta'] == 'Plus':
            if clientes[indice]['Saldo'] - valor_transferencia < -5000: # Se o saldo for menor que o permitido, a transação é cancelada
                print('Limite de saldo negativo atingido. Tente novamente mais tarde.')
                break
            else:
                clientes[indice]['Saldo'] -= valor_transferencia
                hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S')
                clientes[indice]['Extrato'].append(f'{hora_formatada}   - {valor_transferencia}   Tarifa: 0.00   Saldo: {clientes[indice]["Saldo"]:.2f}')
                for index in range(len(clientes)): # Adiciona o valor à conta do cpf final.
                    if cpf_final == clientes[index]['CPF']:
                        clientes[index]['Saldo'] += valor_transferencia
                        hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S')
                        clientes[index]['Extrato'].append(f'{hora_formatada}   + {valor_transferencia}   Tarifa: 0.00   Saldo: {clientes[index]["Saldo"]:.2f}')
                print(f'Transferência realizada com sucesso!\nSaldo: {clientes[indice]["Saldo"]:.2f}')
                break
def invest(): # Função que faz operações livres
    print()
    print('[1] Tesouro Direto')
    print('[2] Fundos Imobiliários')
    print('[3] Ações')
    print()
    cpf_investimento = input('Digite o seu CPF: ') # Linhas 147 a 151 recebe dados
    senha_investimento = input('Digite a sua senha: ')
    tipo_invest = input('Tipo de investimento que deseja fazer: ').capitalize()
    valor_investimento = float(input('Valor a investir: '))
    tempo_investimento = input('Data para retirar o valor(dia/mês/ano): ')
    tempo = tempo_investimento.split('/')
    data_investimento = date(int(tempo[2]), int(tempo[1]), int(tempo[0])) - date.today()
    for indice in range(len(clientes)): # Itera sobre os dicionários presentes na lista clientes
        if cpf_investimento == clientes[indice]['CPF'] and senha_investimento == clientes[indice]['Senha'] and tipo_invest == '1':
            clientes[indice]['Saldo'] -= valor_investimento # Tira o valor do investimento
            investimento = valor_investimento * data_investimento.days/365 * 1.08
            clientes[indice]['Investimentos'].append(f'{investimento:.2f}') # Coloca o valor do investimento na chave Investimentos
            break
        elif cpf_investimento == clientes[indice]['CPF'] and senha_investimento == clientes[indice]['Senha'] and tipo_invest == '2':
            clientes[indice]['Saldo'] -= valor_investimento
            investimento = valor_investimento * data_investimento.days/365 * 1.08
            clientes[indice]['Investimentos'].append(f'{investimento:.2f}')
            break
        elif cpf_investimento == clientes[indice]['CPF'] and senha_investimento == clientes[indice]['Senha'] and tipo_invest == '3':
            clientes[indice]['Saldo'] -= valor_investimento
            investimento = valor_investimento * data_investimento.days/365 * 1.08
            clientes[indice]['Investimentos'].append(f'{investimento:.2f}')
            break
    else:
        print('Dados incorretos. Tente novamente mais tarde.')

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