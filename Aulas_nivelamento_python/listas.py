frutas = ['Banana','Maçã','Abacaxi','Uva','Larana','Manga']

if __name__ == '__main__':
    frutas.append('Caja')
    for posicao, fruta in enumerate(frutas):
        print(f'{fruta} é uma fruta. Posição = {posicao+1}')