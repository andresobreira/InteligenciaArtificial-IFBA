import unittest
from assistente_virtual import *

CHAMANDO_JOANA = "D:\\Dev\\IFBA\\IA_01_Assistente_Virtual\\audios\\chamando joana.wav"
CHAMANDO_MARIA = "D:\\Dev\\IFBA\\IA_01_Assistente_Virtual\\audios\\chamando outro nome.wav"

class TesteNomeAssistente(unittest.TestCase):

    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()

    def testar_01_reconhecer_nome(self):
        tem_transcricao, transcricao = transcrever_arquivo_de_audio(self.reconhecedor,CHAMANDO_JOANA)

        self.assertTrue(tem_transcricao) # usar essas funções de assert para fazer os testes, NÃO usar if, usar as opções de teste mesmo. 

        tokens = obter_tokens(transcricao)
        self.assertIsNotNone(tokens)
        self.assertEqual(tokens[0], self.nome_do_assistente)

    def testar_02_nao_reconhecer_outro_nome(self):
        tem_transcricao, transcricao = transcrever_arquivo_de_audio(self.reconhecedor,CHAMANDO_MARIA)

        self.assertTrue(tem_transcricao) 
        tokens = obter_tokens(transcricao)
        self.assertIsNotNone(tokens)
        self.assertNotEqual(tokens[0], self.nome_do_assistente)

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))

    executador = unittest.TextTestRunner()
    executador.run(testes)