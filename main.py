"""
Disciplina: Fundamentos de Programação
Nome: Éverton da Cunha Sousa
Matrícula: 537858  
"""

from module.functionality import CadastrarCliente, GerarRelatorioDosClientes, MostrarClientesCadastrados, MostrarDadosDoCliente

while True:
    op = int(input('''=========<EdShop>=========
[1] Cadastrar cliente
[2] Mostrar dados do cliente
[3] Mostrar clientes cadastrados
[4] Gerar relatório
[0] sair
=========================
Opção: '''))

    if op == 1:

        infor_User = {
            'nomeCompleto': '',
            'login': '',
            'senha': '',
            'email': '',
            'dataNascimento': '',
            'numeroCelular': '',
            'endereco': '',
        }

        infor_User['nomeCompleto'] = str(
            input("=========<Cadastrar Cliente>=========\nNome completo: ")).strip()
        infor_User['login'] = str(input("login: ")).strip()
        infor_User['senha'] = str(input("Senha: ")).strip()
        infor_User['email'] = str(input("E-mail: ")).strip()
        infor_User['dataNascimento'] = str(
            input("Data de nascimento (dd/mm/aaaa): ")).strip().split("/")
        infor_User['numeroCelular'] = str(
            input("Número de celular (sem ponto, vírgula, traço ou parêntese): ")).strip()
        infor_User['endereco'] = str(input(
            "Endereço (rua, número, complemento, bairro, cidade, CEP, ponto de referencia): ")).strip()

        if CadastrarCliente(infor_User):
            print("Login já existente!\n")
        print("\nCadastrado com sucesso\n")

    elif op == 2:
        login = str(
            input("=========<Mostrar Dados do Cliente>=========\nLogin: "))
        email = str(input("E-mail: "))
        senha = str(input("Senha: "))

        list = MostrarDadosDoCliente(email, senha, login)
        nome, login, senha, email, data, celular, endereco = list["nomeCompleto"], list["login"], list[
            "senha"], list["email"], list["dataNascimento"], list["numeroCelular"], list["endereco"]
        data = str(data['dia']) + "/" + \
            str(data['mes']) + "/" + str(data['ano'])
        print("=========================")
        print(f' Nome completo: {nome}\n Login: {login}\n Senha: {senha}\n E-mail: {email}\n Data de nascimento: {data}\n Número de celular: {celular}\n Endereço: {endereco}')

    elif op == 3:
        print("=========<Mostrar Clientes Cadastrados>=========")
        print(MostrarClientesCadastrados())
    elif op == 4:
        print("=========<Gerar Relatórios dos Clientes>=========")
        print(GerarRelatorioDosClientes())
    elif op == 0:
        break
