# Imports necessário para funcionamento do assistente:
import json , colorama
import speech_recognition as sr
from nltk import word_tokenize, corpus
from threading import Thread
from lampada import *
from tocador import * 


# 1ª Parte: transcrição da fala para uma string
# Configurações do assistente:
IDIOMA_CORPUS = "portuguese"
IDIOMA_FALA = "pt-br"
CAMINHO_CONFIGURACAO = "D:\\Dev\\IFBA\\IA\\03_Assistente\\config.json"
TEMPO_ESCUTA = 4

ATUADORES = [
    {
        "nome": "lampada",
        "iniciar": iniciar_lampada,
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_a_lampada,
    },
    {
        "nome": "tocador",
        "iniciar": iniciar_tocador,
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_tocador,
    }
]

# Realiza a configuração inicial do assistente:
def iniciar():
    iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = False, None, None, None, None

    try:
        reconhecedor = sr.Recognizer()
        palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))
        
        with open(CAMINHO_CONFIGURACAO, "r", encoding="utf8") as arquivo:
            configuracao = json.load(arquivo)
            nome_do_assistente = configuracao['nome']
            acoes = configuracao['acoes']
            arquivo.close()

        for atuador in ATUADORES:
            parametro_de_atuacao = atuador["iniciar"]()
            atuador["parametro_de_atuacao"] = parametro_de_atuacao

            iniciado = True
    except Exception as e:
        print(f"Erro iniciando o assistente: {str(e)}")


    return iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes

# Realiza a captura da fala do usuário:
def escutar_fala(reconhecedor):
    tem_fala, fala = False, None

    with sr.Microphone() as fonte_de_audio:
        try:
            reconhecedor.adjust_for_ambient_noise(fonte_de_audio)

            print('fale alguma coisa... 🎤')  

            fala = reconhecedor.listen(fonte_de_audio, timeout = TEMPO_ESCUTA, phrase_time_limit=TEMPO_ESCUTA)

            tem_fala = True
        except Exception as e:
            print(f'erro escutando fala: {str(e)}')

    return tem_fala, fala

# Traduz o áudio da fala para string:
def transcrever_fala(reconhecedor, fala):
    tem_transcricao, transcricao = False, None

    try:
        transcricao = reconhecedor.recognize_google(fala,language = IDIOMA_FALA).lower()
        
        tem_transcricao = True
    except Exception as e:
        print(f"Erro transcrevendo fala: {str(e)}")

    return tem_transcricao, transcricao


# 2ª Parte: realiza o processamento de linguagem natural
# Obtém tokens a partir da transcrição da fala:
def obter_tolkens(transcricao):
    return word_tokenize(transcricao)

# Elimina as palavras de parada (seriam os "acessorios" da lingua portuguesa):
def eliminar_palavras_de_parada(tokes, palavras_parada):
    tokens_filtrados = []

    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados

# 3ª Parte: validação e execução de comandos do assistente
# Valida comando de acordo com o Json de configuração:
def validar_comando(tokens,nome_assistente,acoes):
    valido, acao, objeto = False, None, None

    # exemplo: o comando sempre precisará ter pelo menos 3 palavras: "Joana, ligar a lampada" => vira: joana ligar lampada
    if len(tokens)>= 3:
        if tokens[0] == nome_assistente:
            acao = tokens[1] 
            objeto = tokens[2]
            
            for acao_prevista in acoes:
                if acao == acao_prevista["nome"]:
                    if objeto in acao_prevista["objetos"]:
                        valido = True
                        break         
        
    return valido, acao, objeto 

# Executa o comando validado:
def executar_comando(acao, objeto):
    print(colorama.Fore.BLUE + '✅ '+ f'Executando ação {acao} sobre {objeto}' + '\n' + colorama.Style.RESET_ALL)

    for atuador in ATUADORES:
        parametro_de_atuacao = atuador["parametro_de_atuacao"]
        atuacao = atuador["atuar"]

        processo = Thread(target = atuacao,args=(acao,objeto,parametro_de_atuacao))
        processo.start()

# Executando todos os passos em conjunto:
if __name__ == '__main__':
    iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()

    if iniciado:
        while True:
            tem_fala, fala = escutar_fala(reconhecedor)
            if tem_fala:
                tem_transcricao, transcricao = transcrever_fala(reconhecedor, fala)
                if tem_transcricao:
                    print(f"usuário falou: {transcricao}")

                    tokens = obter_tolkens(transcricao)
                    tokens = eliminar_palavras_de_parada(tokens,palavras_de_parada)
                    
                    valido, acao, objeto = validar_comando(tokens,nome_do_assistente, acoes)
                    
                    if valido:
                        executar_comando(acao, objeto)
                    else:
                        print("Comando inválido, por favor repita")
