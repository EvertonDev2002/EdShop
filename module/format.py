def DataDicionario(data):
    " fatia a data em dia, mês e ano"
    data = {
        "dia": int(data[0]),
        "mes": int(data[1]),
        "ano": int(data[2]),
    }
    return data
