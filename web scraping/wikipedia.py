import PySimpleGUIQt as sg
from bs4 import BeautifulSoup as bs
import requests as rq

layout = [[sg.Text(" Digite o tema a ser pesquisado:")],
          [sg.Input(key='Input')],
          [sg.Output(key='Output')],
          [sg.Button('Pesquisar', key='Search'), sg.Button('Limpar', key='Clear'), sg.Button('Sair', key='Quit')]]

window = sg.Window('WikiSearch v1.0 - by Daniel Moura', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'Clear':
        window['Input'].update('')
        window['Output'].update('')
    else:
        busca = values['Input']
        busca = busca.replace(" ", '_')
        url = "https://pt.wikipedia.org/wiki/"+busca
        try:
            page = rq.get(url=url)
            soup = bs(page.content, 'html.parser')
            cont = soup.find(id='mw-content-text')
            texto = cont.get_text()
            window['Output'].update(f'{texto}')
        except:
            window['Output'].update('Erro de Conexão! Tente outra hora')
window.close()
