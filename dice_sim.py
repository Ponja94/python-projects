# Dice Simulator

import random
import PySimpleGUI as sg

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        # Layout
        sg.theme('Dark Blue 3')
        self.layout = [
            [sg.Text('Play the Dice?')],
            [sg.Button('Yes'), sg.Button('No')]
        ]


    def Start(self):

        # Window
        self.window = sg.Window('Dice simulator', layout=self.layout)
        # Read values from window
        self.events, self.values = self.window.Read()
        # do something with values

        try:
            if self.events == 'y' or self.events == 'yes':
                self.generateDiceValue()
            elif self.events == 'n' or self.events == 'no':
                print('Ok, thanks.')
            else:
                print('Please enter yes or no')

        except:
            print('ocorreu um erro ao receber sua resposta')

    def generateDiceValue(self):
        print(random.randint(self.min_value, self.max_value))


simulator = DiceSimulator()

simulator.Start()
