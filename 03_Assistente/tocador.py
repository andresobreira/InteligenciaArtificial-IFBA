def iniciar_tocador():
    return None

def atuar_sobre_tocador(acao, objeto, parametro_de_atuacao):
    if acao in ["tocar"] and objeto == "música":
        print('Tocando a música')
    elif acao in ["parar"] and objeto == "música":
        print('Parando a música')