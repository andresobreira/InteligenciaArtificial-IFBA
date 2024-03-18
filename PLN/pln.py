from nltk import word_tokenize, corpus
from nltk.corpus import floresta
from nltk.stem import RSLPStemmer

LINGUAGEM = 'portuguese'

def iniciar():
    iniciado, classificacoes, palavras_de_parada = False, None, None

    try:
        palavras_de_parada = set(corpus.stopwords.words(LINGUAGEM))

        classificacoes = {}
        for (palavra,classificacao) in floresta.tagged_words():
            classificacoes[palavra.lower()] = classificacao

        iniciado = True
    except Exception as e:
        print(f'Ocorreu um erro acessando o NLTK: {str(e)}')

    return iniciado, classificacoes, palavras_de_parada 

def obter_tokens(texto):
    tokens = word_tokenize(texto, LINGUAGEM)
    return word_tokenize(texto, LINGUAGEM)

def imprimir_tolkens(tokens):
    for token in tokens:
        print(token)

def eliminar_palavras_de_parada(tokens, palavras_de_parada):
    tokens_fitrados = []

    for token in tokens:
        if token not in palavras_de_parada:
            tokens_fitrados.append(token)

    return tokens_fitrados

def classificar_gramaticamente(tokens, classificacoes):
    for token in tokens:
        classificacao = classificacoes[token]
        print(f'{token} é um(a) {classificacao}')


def estemizar(tokens):
    estemizador = RSLPStemmer()
    
    for token in tokens:
        raiz = estemizador.stem(token)
        print(f"A raiz da palavra {token} é {raiz}")



if __name__ == "__main__":
    TEXTO = 'A verdadeira generosidade para com o futuro consiste em dar tudo ao presente.' # Albert Camus
    iniciado, classificacoes, palavras_de_parada  = iniciar()
    if iniciado:
        tokens = obter_tokens(TEXTO.lower()) # a biblioteca é case sensitive, passar sempre o texto em minusculo.
        # imprimir_tolkens(tokens)

        tokens = eliminar_palavras_de_parada(tokens,palavras_de_parada)
        # imprimir_tolkens(tokens)

        # classificar_gramaticamente(tokens,classificacoes)
        estemizar(tokens)