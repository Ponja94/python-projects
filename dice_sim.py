# Simulador de dado para jogo
# Simular o uso de um dado para jogo

import random


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Quer gerar novo valor no dado?'

    def iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 's':
                self.gerarValorDoDado()
            elif resposta == 'n':
                print('nenhum número gerado')
            else:
                print('favor digitar sim ou não')

        except:
            print('ocorreu um erro ao receber sua resposta')

    def gerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()

simulador.iniciar()
