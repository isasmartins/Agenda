def exibirtudo():

    
    arquivo = open('agenda.txt', 'r')
    dados = arquivo.read()
    arquivo.close()

    print(contatos)
    principal() 

def cadastro(nome, rua, cep, bairro, estado, telefone):

        arquivo = open('agenda.txt', 'r')
        agendaAtual = arquivo.read()
        arquivo.close()
        
        dadosNovos = "\n\nNome: " + nome + "\nRua: " + rua + "\nCep: " + cep + "\nBairro: " + bairro + "\nEstado: " + estado + "\nTelefone: " + telefone
        agendaNova = agendaAtual + dadosNovos

        arquivo = open('agenda.txt', 'w')
        arquivo.write(agendaNova)
        arquivo.close()
        print("\nCadastrado com sucesso!\n\n")
        principal()

def consulta(nome):
    arquivo = open('agenda.txt', 'r')
    dados = arquivo.readlines()
    arquivo.close()
    
    posicao = dados.index("Nome: " + nome+ "\n")
    posicaoTotal = posicao + 5

    result = dados[posicao:posicaoTotal]
    resultTotal = "".join(result)
    
    print("\n" + resultTotal)
    principal()

def principal():
   
    if opcao == 1:
        exibirtudo()
        
    elif opcao == 2:
        print("Cadastrar Agenda\n")
        nome = input("Digite o nome: ")
        rua = input("Digite a rua: ")
        cep = input("Digite o cep: ")
        bairro = input("Digite o bairro: ")
        estado = input("Digite o estado: ")
        telefone = input("Digite o telefone: ")
        
        cadastrar(nome, rua, cep, bairro, estado, telefone)
        
    elif opcao == 3:
        nome = input("Digite o nome: ")
        consultar(nome)
    elif opcao == 0:
        exit()
        
principal()
