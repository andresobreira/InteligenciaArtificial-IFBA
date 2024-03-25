CADASTRO = {
    'descricao': 'cadastro de pessoas',
    'pessoas': [
        {
            'nome': 'Maria da Silva',
            'idade': 25,
            'profissao': 'Engenheira'
        },
        {
            'nome': 'José dos Santos',
            'idade': 32,
            'profissao': 'Matemático'
        },
        {
            'nome': 'João Souza',
            'idade': 18,
            'profissao': 'Estudante'
        },
    ]
}

if __name__ == '__main__':
    pessoas = CADASTRO['pessoas']
    for pessoa in pessoas:
        print(pessoa)
        print(pessoa['nome'])

    print()
    CADASTRO['versao'] = '1.0'
    print(CADASTRO)
    
    CADASTRO.pop('versao')
    print(CADASTRO)