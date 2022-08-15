def ValidacaoInteiro(n):
    ''' Essa função valida se o número é inteiro'''
    for index in range(len(n)):
        verifica = n[index]
        if not verifica.isnumeric():
            return False
    return True


def ValidacaoNumeroCelular(nc):
    ''' Essa função valida se o número de celular está correto'''
    if len(nc) == 11 and ValidacaoInteiro(nc):
        return True
    else:
        return False


def ValidacaoData(dn):
    ''' Essa função valida se a data está correta '''
    from datetime import datetime
    ano = datetime.today().strftime('%Y-%m-%d')
    ano = ano.split("-")

    if ValidacaoInteiro(dn):
        if int(dn[0]) <= 31 and int(dn[1]) <= 12 and int(ano[0]) - int(dn[2]) <= 60:
            return True
        else:
            return False
    else:
        return False


def ValidacaoDuplicata(file, login):
    ''' Essa função valida se há duplicata do mesmo login '''
    with open(file, "r") as linhas:
        arquivo = linhas.readlines()
        for linha in range(len(arquivo)):
            list = eval(arquivo[linha])
            if list["login"] == login:
                linhas.close()
                return False
        return True
