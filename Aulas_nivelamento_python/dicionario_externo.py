import json

def carregar_cadastro():
    cadastro, carregado = None, False

    try:
        with open('Aulas_nivelamento_python\cadastro.json', 'r', encoding='utf8') as arquivo:
            cadastro = json.load(arquivo)
            arquivo.close()
        carregado = True
    except Exception as e:
        print(f'Ocorreu um erro ao abrir o arqivo: {str(e)}')

    return cadastro, carregado


if __name__ == '__main__':
    cadastro, carregado = carregar_cadastro()
    
    # if cadastro is not None:
    if carregado:
        pessoas = cadastro['pessoas']
        print(pessoas)
    else:
        print('Cadastro não disponível.')