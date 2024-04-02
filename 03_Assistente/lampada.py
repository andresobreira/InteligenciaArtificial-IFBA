def iniciar_lampada():
    return None 

def atuar_sobre_a_lampada(acao, objeto, parametro_de_atuacao):
    if acao in ["ligar","acender"] and objeto == "lâmpada":
        print('Ligando a lampada')
    elif acao in ["desligar","apagar"] and objeto == "lâmpada":
        print('Desligando a lampada')
