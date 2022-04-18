# Guessing the number

import random
import PySimpleGUI as sg


class GuessNumber:
    def __init__(self):
        self.random_value = 0
        self.min_value = 1
        self.max_value = 100
        self.try_again = True

    def Start(self):
        # Layout
        layout = [
            [sg.Text('Your Guess', size=(39, 0))],
            [sg.Input(size=(18, 0), key='GuessValuee')],
            [sg.Button('Guess!')],
            [sg.Output(size=(39, 10))]
        ]
        # Window
        self.window = sg.Window('Guess a number!', layout=layout)
        self.RandomNumberGenerator()
        try:
            while True:
                # Reciv values
                self.event, self.value = self.window.Read()
                # Do something with values
                if self.event == 'Guess!':
                    self.guess_value = self.value['GuessValuee']
                    while self.try_again == True:
                        if int(self.guess_value) > self.random_value:
                            print('lower')
                            break
                        elif int(self.guess_value) < self.random_value:
                            print('higher')
                            break
                        if int(self.guess_value) == self.random_value:
                            print('CONGRATULATIONS!')
                            self.try_again = False
                            break
        except:
            print('Please enter only numbers')
            self.Start()

    def RandomNumberGenerator(self):
        self.random_value = random.randint(self.min_value, self.max_value)


guess = GuessNumber()
guess.Start()
