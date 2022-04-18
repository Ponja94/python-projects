import random
import PySimpleGUI as sg

class ChooseForMe:
    def __init__(self):
        self.answare=[
            'Every Cloud Has a Silver Lining',
            'When the Rubber Hits the Road',
            'Wild Goose Chase',
            'Under Your Nose',
            'Needle In a Haystack',
            'Fit as a Fiddle'
        ]

    def Start(self):
        layout = [
            [sg.Text('Ask something:')],
            [sg.Input()],
            [sg.Output(size=(50, 10))],
            [sg.Button('Choose for me!')]
        ]
        self.window = sg.Window('Choose',layout=layout)
        while True:
            self.events, self.values = self.window.Read()
            if self.events == 'Choose for me!':
                print(random.choice(self.answare))


chooseNow = ChooseForMe()
chooseNow.Start()
