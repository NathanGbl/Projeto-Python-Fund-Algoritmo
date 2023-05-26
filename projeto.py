from datetime import datetime, date
from time import sleep 

# Funções para alterar tudo dentro do arquivo
def ler_arquivo(nome_arquivo):
    lista_informacoes = []
    with open(nome_arquivo, 'r') as arquivo: # Abre o arquivo no modo leitura na variável arquivo
        for linha in arquivo: # Laço que itera sobre cada linha do arquivo
            dicionario = eval(linha.strip()) # Cada linha do arquivo é transformada em dicionário 
            lista_informacoes.append(dicionario) # Adiciona cada dicionário na lista 'lista_informacoes'
    return lista_informacoes

def substitui_info(nome_arquivo, lista_informacoes):
    with open(nome_arquivo, 'w') as arquivo: # Abre o arquivo no modo escrever na variável arquivo
        for informacao in lista_informacoes: # Para cada item(dicionário) na lista 'lista_informacoes' ele converte o dicionário para string, escreve no arquivo e quebra a linha para que cada linha seja os dados de um cliente
            arquivo.write(str(informacao) + '\n')

# Função que adiciona um cliente ao banco
def novo_cliente():
    print("Adicione um novo cliente.")
    print()
    nome = input('Nome: ').strip() # Linha 22, 23, 24 e 25 e 26 solicida dados
    cpf = input('CPF: ').strip()
    tipo_conta = input('Tipo de conta (Comum ou Plus?): ').capitalize().strip() # Tira os espaços de antes e depois da string e coloca a primeira letra como maiúscula
    saldo = float(input('Valor inicial da conta: R$'))
    senha_usuario = input('Senha: ')
    dados_clientes = {} # Criação do dicionário
    dados_clientes['Nome'] = nome # Linha 28, 29, 30, 31, 32 insere os dados no dicionário
    dados_clientes['CPF'] = cpf
    dados_clientes['Tipo de conta'] = tipo_conta
    dados_clientes['Saldo'] = saldo
    dados_clientes['Senha'] = senha_usuario
    dados_clientes['Extrato'] = []
    dados_clientes['Investimentos'] = []
    informacoes.append(dados_clientes) # Adiciona o dicionário como um elemento da lista informacoes
    print()
    print('Registrando informações...')
    sleep(3)
    print("Cliente adicionado com sucesso")

# Função que retira algum cliente do banco
def apagar_cliente():
    print("Apague um cliente.")
    print()
    cpf_apagar = input('Digite o cpf para apagar a conta: ') # Solicida o cpf que será apagado
    print()
    print('Buscando cpf...')
    sleep(3)
    print()
    for indice in range(len(informacoes)): # Laço itera sobre cada chave 'CPF' dos dicionários e, se achar o cpf, deleta, senão, avisa que o cpf não foi encontrado.
        if cpf_apagar == informacoes[indice]['CPF']:
            del informacoes[indice]
            print("Cliente apagado com sucesso")
            break
    else:
        print(f'CPF {cpf_apagar} não encontrado. Tente novamente mais tarde.')

# Função que mostra a lista com informacoes
def lista_clientes():
    print()
    print('Lista de clientes:')
    for indice in range(len(informacoes)): # itera sobre cada dicionário na lista cliente e imprimi o conteúdo do dicionário.
        print(informacoes[indice])
    print()

# Função que debita um valor            
def debito():
    print("Realize um débito.")
    print()
    cpf_debito = input('Digite o CPF da sua conta: ') # Linha 70, 71, 85 solicita dados
    senha_debito = input('Digite sua senha: ')
    print()
    print('Buscando dados...')
    sleep(3)
    print()
    dado_encontrato = False # Varial de controle para validar dados
    for indice in range(len(informacoes)): # Laço que itera sobre cada chave 'CPF' e 'Senha'. Se achar troca o valor da variável de controle, senão não
        if cpf_debito == informacoes[indice]['CPF'] and senha_debito == informacoes[indice]['Senha']:
            dado_encontrato = True
    if dado_encontrato == False: # Se o valor da variável não mudou: para a função débito
        print('Dados não encontrados. Tente novamente mais tarde.')
    else: # Senão, continua
        print('Dados encontrados.')
        print()
        valor_debito = float(input('Digite o valor a ser debitado: '))
        print()
        for indice in range(len(informacoes)): # Itera sobre cada dicionário na lista informacoes e verifica os dados recebidos.
            if cpf_debito == informacoes[indice]['CPF'] and senha_debito == informacoes[indice]['Senha'] and informacoes[indice]['Tipo de conta'] == 'Comum' and informacoes[indice]['Saldo'] - valor_debito * 1.05 >= -1000: # Se os dados estiverem corretos e o saldo ficar acima de 1000 negativo, o débito é realizado
                    informacoes[indice]['Saldo'] -= valor_debito * 1.05 # Desconta o valor + taxas do valor da chave 'Saldo'
                    tarifa = valor_debito * 1.05 - valor_debito 
                    hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S') # variável que captura a data e a hora atuais e transforma em uma string formatada
                    informacoes[indice]['Extrato'].append(f'{hora_formatada}   - {valor_debito}   Tarifa: {tarifa}   Saldo: {informacoes[indice]["Saldo"]:.2f}') # Adiciona a string formatada para a lista Extrato
                    print(f"Taxas adicionadas neste débito: {tarifa}")
                    print(f'Saldo: {informacoes[indice]["Saldo"]}')
                    print(f'Débito realizado com sucesso!')
            elif cpf_debito == informacoes[indice]['CPF'] and senha_debito == informacoes[indice]['Senha'] and informacoes[indice]['Tipo de conta'] == 'Plus' and informacoes[indice]['Saldo'] - valor_debito * 1.03 >= -5000: # Se os dados estiverem corretos e o saldo ficar acima de 5000 negativo, o débito é realizado
                    informacoes[indice]['Saldo'] -= valor_debito * 1.03 # Desconta o valor + taxas do valor da chave 'Saldo'
                    tarifa = valor_debito * 1.03 - valor_debito
                    hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S') # variável que captura a data e a hora atuais e transforma em uma string formatada
                    informacoes[indice]['Extrato'].append(f'{hora_formatada}   - {valor_debito}   Tarifa: {tarifa}   Saldo: {informacoes[indice]["Saldo"]:.2f}') # Adiciona a string formatada para a lista Extrato
                    print(f"Taxas adicionadas neste débito: {tarifa}")
                    print(f'Saldo: {informacoes[indice]["Saldo"]}')
                    print(f'Débito realizado com sucesso!')
            else: # Se não aconteceu nada até agora, então o saldo ficou abaixo do limite.
                print('Transação excede o limite de saldo negativo. Tente novamente mais tarde.')

# Função que adiciona um valor na conta do usuario 
def deposito():
    print("Realize um depósito.")
    print()
    cpf_deposito = input('CPF que você deseja enviar: ') # Linhas 111, 112 e 125 solicita dados
    senha_deposito = input('Senha: ')
    dado_encontrado = False # Variável de controle para busca dos dados da linha 111 e 112
    print()
    print('Buscando dados...')
    print()
    sleep(3)
    for indice in range(len(informacoes)): # Laço que itera sobre cada chave 'CPF' e 'Senha'. Se encontrar, troca o valor da variável de controle. Senão, não.
        if cpf_deposito == informacoes[indice]['CPF'] and senha_deposito == informacoes[indice]['Senha']:
            dado_encontrado = True
            print('Dados encontrados.')
    if dado_encontrado == False: # Se o valor não foi trocado, para a função depósito
        print('Dados não encontrados. Tente novamente mais tarde.')
    else:
        valor_deposito = float(input('Valor que irá depositar: '))
        for indice in range(len(informacoes)): # Itera sobre cada dicionário na lista informacoes e verifica os dados recebidos.
            if cpf_deposito == informacoes[indice]['CPF'] and senha_deposito == informacoes[indice]['Senha']:
                informacoes[indice]['Saldo'] += valor_deposito # Se os dados estiverem corretos, o valor é adicionado à conta e o saldo é imprimido na tela.
                hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S') # variável que captura a data e a hora atuais e transforma em uma string formatada
                informacoes[indice]['Extrato'].append(f'{hora_formatada}   + {valor_deposito}   Tarifa: 0.00   Saldo: {informacoes[indice]["Saldo"]:.2f}') # Adiciona uma string formatada na lista extrato
                print(f'Saldo: {informacoes[indice]["Saldo"]:.2f}')

# Função que mostra o extrato da conta bancaria do usuario
def extrato():
    print()
    print('Consulte seu extrato aqui.')
    cpf_extrato = input('Digite o cpf para exibir o extrato: ') # Linhas 137 e 138 solicitam dados
    senha_extrato = input('Digite a senha: ')
    print()
    print('Buscando dados...')
    sleep(3)
    dado_encontrado = False # Variável de controle para busca dos dados da linha 137 e 138
    for indice in range(len(informacoes)): # Laço que itera sobre cada chave 'CPF' e 'Senha'. Se encontrar, troca o valor da variável de controle. Senão, não.
        if cpf_extrato == informacoes[indice]['CPF'] and senha_extrato == informacoes[indice]['Senha']:
            dado_encontrado = True
    if dado_encontrado == False:
        print('Dados não encontrados. Tente novamente mais tarde.')
    else:
        print()
        for indice in range(len(informacoes)): # Itera sobre cada dicionário
            if cpf_extrato == informacoes[indice]['CPF'] and senha_extrato == informacoes[indice]['Senha']: # Verifica o CPF e senha. Ao encontrar exibi as informações do dicionário
                print(f'Nome: {informacoes[indice]["Nome"]}')
                print(f'CPF: {informacoes[indice]["CPF"]}')
                print(f'Conta: {informacoes[indice]["Tipo de conta"]}')
                for index in range(len(informacoes[indice]['Extrato'])): # Itera sobre cada elemento da lista que está na chave Extrato e imprimi.
                    print(f'Data: {informacoes[indice]["Extrato"][index]}') # Cada elemento da lista Extrato é uma string formatada

# Função que faz transferencias 
def transf_contas():
    print("Faça uma transferência interna")
    print()
    cpf_origem = input('Digite o CPF da sua conta: ') # Linha 162, 163, 164 e 184 solicita dados.
    senha_origem = input('Digite sua senha: ')
    cpf_final = input('Digite o CPF do destinatário: ')
    print()
    print('Buscando dados...')
    sleep(3)
    print()
    dado_origem_encontrado = False # Variável de controle para busca dos dados da linha 162 e 163
    dado_destino_encontrado = False # Variável de controle para busca dos dados da linha 164
    for indice in range(len(informacoes)): # Laço que itera sobre cada chave 'CPF' e 'Senha'. Se encontrar, troca o valor de dado_origem_encontrado. Senão, não.
        if cpf_origem == informacoes[indice]['CPF'] and senha_origem == informacoes[indice]['Senha']:
            dado_origem_encontrado = True
            break
    for indice in range(len(informacoes)): # Laço que itera sobre cada chave 'CPF'. Se encontrar, troca o valor de dado_destino_encontrado. Senão, não.
        if cpf_final == informacoes[indice]['CPF']:
            dado_destino_encontrado = True
            break
    if dado_origem_encontrado == False or dado_destino_encontrado == False: # Se uma das variáveis de controle não mudou o valor, para a a função de transferência.
        print('Dados incorretos. Tente novamente mais tarde')
    else:
        print('Dados encontrados.')
        print()
        valor_transferencia = float(input('Digite o valor a ser debitado: '))
        print()
        for indice in range(len(informacoes)): # Laço que percorre a lista e encontra os dados de quem vai dar o dinheiro
            if cpf_origem == informacoes[indice]['CPF'] and senha_origem == informacoes[indice]['Senha'] and informacoes[indice]['Tipo de conta'] == 'Comum' and informacoes[indice]['Saldo'] - valor_transferencia >= -1000: # Se os dados estiverem corretos e o saldo ficar acima de 1000 negativo, a transferência é realizada
                    informacoes[indice]['Saldo'] -= valor_transferencia # Tira o valor da transferência do saldo do cliente de origem
                    hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S') # Variável que captura a data e a hora atuais e transforma em uma string formatada
                    informacoes[indice]['Extrato'].append(f'{hora_formatada}   - {valor_transferencia}   Tarifa: 0.00   Saldo: {informacoes[indice]["Saldo"]:.2f}') # Adiciona a string formatada para a lista Extrato
                    for index in range(len(informacoes)): # Laço que percorre a lista e encontra os dados de quem vai receber o dinheiro
                        if cpf_final == informacoes[index]['CPF']:
                            informacoes[index]['Saldo'] += valor_transferencia # Cliente de destino recebe o valor da transferência do cliente de origem
                            hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S') # Variável que captura a data e a hora atuais e transforma em uma string formatada
                            informacoes[index]['Extrato'].append(f'{hora_formatada}   + {valor_transferencia}   Tarifa: 0.00   Saldo: {informacoes[index]["Saldo"]:.2f}')
                    print(f'Transferência realizada com sucesso!\nSaldo: {informacoes[indice]["Saldo"]:.2f}')
                    break
            elif cpf_origem == informacoes[indice]['CPF'] and senha_origem == informacoes[indice]['Senha'] and informacoes[indice]['Tipo de conta'] == 'Plus' and informacoes[indice]['Saldo'] - valor_transferencia >= -5000: # Se os dados estiverem corretos e o saldo ficar acima de 5000 negativo, a transferência é realizada
                    informacoes[indice]['Saldo'] -= valor_transferencia # Tira o valor da transferência do saldo do cliente de origem
                    hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S')
                    informacoes[indice]['Extrato'].append(f'{hora_formatada}   - {valor_transferencia}   Tarifa: 0.00   Saldo: {informacoes[indice]["Saldo"]:.2f}')
                    for index in range(len(informacoes)): # Laço que percorre a lista e encontra os dados de quem vai receber o dinheiro
                        if cpf_final == informacoes[index]['CPF']:
                            informacoes[index]['Saldo'] += valor_transferencia # Cliente de destino recebe o valor da transferência do cliente de origem
                            hora_formatada = datetime.now().strftime('%d/%m/%Y %I:%M:%S') # Variável que captura a data e a hora atuais e transforma em uma string formatada
                            informacoes[index]['Extrato'].append(f'{hora_formatada}   + {valor_transferencia}   Tarifa: 0.00   Saldo: {informacoes[index]["Saldo"]:.2f}') # Adiciona a string formatada para a lista Extrato
                    print(f'Transferência realizada com sucesso!\nSaldo: {informacoes[indice]["Saldo"]:.2f}')
                    break
        else:
            print('Limite de saldo negativo atingido. Tente novamente mais tarde.')
def invest(): # Função que faz operações livres
    print("Bem vindo a opção de investimento!")
    sleep(1)
    print("Insira os dados corretos para prosseguir")
    sleep(3)
    cpf_investimento = input('Digite o seu CPF: ') # Linhas 216 e 217 solicita dados
    senha_investimento = input('Digite a sua senha: ')
    print('Analisando dados...')
    sleep(2)
    print()
    dado_encontrado = False # Variável de controle para busca dos dados da linha 216 e 217
    for indice in range(len(informacoes)): # Laço que percorre a lista e encontra os dados de quem vai investir
        if cpf_investimento == informacoes[indice]['CPF'] and senha_investimento == informacoes[indice]['Senha']: # Se achar, muda o valor da variável de controle. Senão, não
            dado_encontrado = True
            print('Dados encontrados.')
    if dado_encontrado == False: # Se a variável não sofreu mudança no valor, para a função.
        print('Dados Incorretos')
    else:
        print()
        print('[1] Tesouro Direto')
        print('[2] Fundos Imobiliários')
        print('[3] Ações')
        print()
        tipo_invest = input('Tipo de investimento que deseja fazer: ').strip() # Linhas 234, 235, 236 solicita dados
        valor_investimento = float(input('Valor a investir: '))
        tempo_investimento = input('Data para retirar o valor(dia/mês/ano): ')
        tempo = tempo_investimento.split('/') # Separa dia, mês e ano com base na '/'
        data_investimento = date(int(tempo[2]), int(tempo[1]), int(tempo[0])) - date.today() # Diferença entre a data que o valor será retirado e a data que o valor foi investido
        for indice in range(len(informacoes)): # Itera sobre os dicionários presentes na lista informacoes
            if cpf_investimento == informacoes[indice]['CPF'] and senha_investimento == informacoes[indice]['Senha'] and informacoes[indice]['Tipo de conta'] == 'Comum' and informacoes[indice]['Saldo'] - valor_investimento >= -1000 and tipo_invest == '1': # Se os dados estiverem corretos e o saldo ficar acima de 1000 negativo, o investimento é realizado
                informacoes[indice]['Saldo'] -= valor_investimento # Tira o valor do saldo para investimento
                investimento = valor_investimento * data_investimento.days/365 * 1.08 # Valor já com os rendimentos do investimento
                informacoes[indice]['Investimentos'].append(f'{investimento:.2f}') # Coloca o valor do investimento na chave Investimentos
                break
            elif cpf_investimento == informacoes[indice]['CPF'] and senha_investimento == informacoes[indice]['Senha'] and informacoes[indice]['Tipo de conta'] == 'Plus' and informacoes[indice]['Saldo'] - valor_investimento >= -5000 and tipo_invest == '1': # Se os dados estiverem corretos e o saldo ficar acima de 5000 negativo, o investimento é realizado
                informacoes[indice]['Saldo'] -= valor_investimento # Tira o valor do saldo para investimento
                investimento = valor_investimento * data_investimento.days/365 * 1.08 # Valor já com os rendimentos do investimento
                informacoes[indice]['Investimentos'].append(f'{investimento:.2f}') # Coloca o valor do investimento na chave Investimentos
                break
            elif cpf_investimento == informacoes[indice]['CPF'] and senha_investimento == informacoes[indice]['Senha'] and informacoes[indice]['Tipo de conta'] == 'Comum' and informacoes[indice]['Saldo'] - valor_investimento >= -1000 and tipo_invest == '2':
                informacoes[indice]['Saldo'] -= valor_investimento
                investimento = valor_investimento * data_investimento.days/365 * 1.08
                informacoes[indice]['Investimentos'].append(f'{investimento:.2f}')
                break
            elif cpf_investimento == informacoes[indice]['CPF'] and senha_investimento == informacoes[indice]['Senha'] and informacoes[indice]['Tipo de conta'] == 'Plus' and informacoes[indice]['Saldo'] - valor_investimento >= -5000 and tipo_invest == '2':
                informacoes[indice]['Saldo'] -= valor_investimento
                investimento = valor_investimento * data_investimento.days/365 * 1.08
                informacoes[indice]['Investimentos'].append(f'{investimento:.2f}')
            elif cpf_investimento == informacoes[indice]['CPF'] and senha_investimento == informacoes[indice]['Senha'] and informacoes[indice]['Tipo de conta'] == 'Comum' and informacoes[indice]['Saldo'] - valor_investimento >= -1000 and tipo_invest == '3':
                informacoes[indice]['Saldo'] -= valor_investimento
                investimento = valor_investimento * data_investimento.days/365 * 1.08
                informacoes[indice]['Investimentos'].append(f'{investimento:.2f}')
                break
            elif cpf_investimento == informacoes[indice]['CPF'] and senha_investimento == informacoes[indice]['Senha'] and informacoes[indice]['Tipo de conta'] == 'Plus' and informacoes[indice]['Saldo'] - valor_investimento >= -5000 and tipo_invest == '3':
                informacoes[indice]['Saldo'] -= valor_investimento
                investimento = valor_investimento * data_investimento.days/365 * 1.08
                informacoes[indice]['Investimentos'].append(f'{investimento:.2f}')
                break
        else:
            print('Limite de saldo negativo atingido. Tente novamente mais tarde.')

informacoes = ler_arquivo("clientes.txt") # Variável 'informacoes' recebe uma lista de dicionários da função ler_arquivo()

print("Bem vindo ao banco quem poupa tem!")
# Menu de navegação do banco
while True:
    print("Lembre-se de sempre finalizar o programa com a opção 9 para salvar todas alterações realizadas.")
    sleep(2)
    print(" ")
    print('[1] Novo cliente') 
    print('[2] Apagar cliente')
    print('[3] Listar clientes')
    print('[4] Débito')
    print('[5] Depósito')
    print('[6] Extrato')
    print('[7] Transferência entre contas')
    print('[8] Investimentos')
    print('[9] Sair')
    entrada = input('Escolha uma das opções acima: ')
    print()
    while entrada != '1' and entrada != '2' and entrada != '3' and entrada != '4' and entrada != '5' and entrada != '6' and entrada != '7' and entrada != '8' and entrada != '9': # Laço que funcionará até que o usuário escreva uma opção válida
        entrada = input('Opção inválida. Tente novamente:')
    entrada = int(entrada)
    if entrada == 9:
        print('Salvando alterações...')
        sleep(2)
        substitui_info("clientes.txt", informacoes) # Reescreve o arquivo com os dados presentes na variável informacoes (que é uma lista de dicionários)
        print("Suas informações foram salvas com sucesso!")
        print("Muito obrigado por ter escolhido nosso banco!")
        print()
        break
    elif entrada == 1: # Chama a função novo_cliente()
        novo_cliente()
        print(" ")
    elif entrada == 2: # Chama a função apagar_cliente()
        apagar_cliente()
        print(" ")
    elif entrada == 3: # Chama a função lsita_clientes()
        lista_clientes()
    elif entrada == 4: # Chama a função debito()
        debito()
        print(" ")
    elif entrada == 5: # Chama a função deposito()
        deposito()
        print(" ")
    elif entrada == 6: # Chama a função extrato()
        extrato()
        print(" ")
    elif entrada == 7: # Chama a função tranf_contas()
        transf_contas()
        print(" ")
    elif entrada == 8: # Chama a função invest()
        invest()