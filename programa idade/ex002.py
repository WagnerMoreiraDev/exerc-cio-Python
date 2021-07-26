def idade_pessoa(id):
    idp = int(id)
    if idp <0:
        return 'idade inválida'
    elif idp <12:
        return  'você ainda é uma criança'
    elif idp <18:
        return 'você é adolecente'
    elif idp <65:
        return  'Você já é adulto'
    elif idp <100:
        return  'você está na melhor idade'
    else:
        return 'você é uma pessoa centenária'
