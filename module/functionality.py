from module.validation import ValidacaoData, ValidacaoNumeroCelular, ValidacaoDuplicata
from module.format import DataDicionario

file = "db/DB_EDSHOW.txt"


def CadastrarCliente(infor):
    '''Essa função cadastra o cliente'''

    if ValidacaoDuplicata(file, infor['login']):
        if ValidacaoNumeroCelular(infor['numeroCelular']) and ValidacaoData(infor['dataNascimento']):
            infor['dataNascimento'], infor['numeroCelular'] = DataDicionario(
                infor['dataNascimento']), int(infor['numeroCelular'])

            with open(file, "a") as arquivo:
                arquivo.write(f'{infor}\n')
                arquivo.close()
        elif ValidacaoNumeroCelular(infor['numeroCelular']) == False:
            while True:
                numeroCelular = str(input(
                    "=========================\nDigite novamente o número de celular com 11 dígitos (sem ponto, vírgula, traço ou parêntese): ")).strip()

                if ValidacaoNumeroCelular(numeroCelular):
                    infor['dataNascimento'], infor['numeroCelular'] = DataDicionario(
                        infor['dataNascimento']), int(numeroCelular)
                    with open(file, "a") as arquivo:
                        arquivo.write(str(infor + '\n'))
                        arquivo.close()
                    break
        elif ValidacaoData(infor['dataNascimento']) == False:
            while True:
                dataNascimento = str(input(
                    "=========================\nDigite novamente a data de nascimento (dd/mm/aaaa): \n"))

                if ValidacaoData(dataNascimento):
                    infor['dataNascimento'], infor['numeroCelular'] = DataDicionario(
                        dataNascimento), int(infor['numeroCelular'])
                    with open(file, "a") as arquivo:
                        arquivo.write(str(infor + '\n'))
                        arquivo.close()
                    break
        elif ValidacaoNumeroCelular(infor['numeroCelular']) == False and ValidacaoData(infor['dataNascimento']) == False:
            while True:
                dataNascimento = str(input(
                    "=========================\nDigite novamente a data de nascimento (dd/mm/aaaa): \n"))
                numeroCelular = str(input(
                    "Digite novamente o número de celular com 11 dígitos (sem ponto, vírgula, traço ou parêntese): ")).strip()

                if ValidacaoData(dataNascimento) and ValidacaoNumeroCelular(numeroCelular):
                    infor['dataNascimento'], infor['numeroCelular'] = DataDicionario(
                        dataNascimento), int(numeroCelular)
                    with open(file, "a") as arquivo:
                        arquivo.write(str(infor + '\n'))
                        arquivo.close()
                    break
    else:
        return True


def MostrarDadosDoCliente(email, senha, login):
    ''' Essa função mostra das dados do client'''

    with open(file, "r") as linhas:
        arquivo = linhas.readlines()
        for linha in range(len(arquivo)):
            list = eval(arquivo[linha])
            if list["email"] == email and list["senha"] == senha and list["login"] == login:
                list = eval(arquivo[linha])
        linhas.close()
        return list


def MostrarClientesCadastrados():
    ''' Essa função mostra todos os clientes cadastro no sistema'''

    with open(file, "r") as linhas:
        arquivo = linhas.readlines()
        clientes = ""
        list = {}
        for i in range(len(arquivo)):
            list = eval(arquivo[i])
            clientes += str(1+i) + ". " + "Nome: " + \
                list['nomeCompleto'] + " | " + "Login: " + list['login'] + "\n"
    linhas.close()
    return clientes


def GerarRelatorioDosClientes():
    ''' Essa função gera um relatório em /doc'''

    from datetime import datetime
    data = datetime.today().strftime('%Y-%m-%d')
    data = data.split("-")
    with open(file, "r") as linhas:
        arquivo = linhas.readlines()
        quantidade = len(arquivo)
        topo = f'Relatório de Clientes\nA loja <EdShop> possui {quantidade} clientes que estão listados abaixo:\n'
        rodape = f'Russas, {data[2]} de {data[1]} de {data[0]}'
        clientes = ""
        list = {}
        for i in range(quantidade):
            list = eval(arquivo[i])
            clientes += str(1+i) + ". " + list['nomeCompleto'] + "\n"
    linhas.close()
    with open(f'doc/clientes_{data[2]}_{data[1]}_{data[0]}.txt', "w") as salvar:
        salvar.write(str(topo+clientes+rodape))
        salvar.close()
        return "Relatório gerado com sucesso!"
