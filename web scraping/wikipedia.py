#!python3

from bs4 import BeautifulSoup as bs
import requests as rq

while True:

    busca = input("Digite o tema: ")
    busca = busca.replace(" ", '_')
    url = "https://pt.wikipedia.org/wiki/"+busca
    page = rq.get(url=url)
    soup = bs(page.content, 'html.parser')
    conteudo = soup.find(class_="mw-parser-output")
    texto = conteudo.get_text()

    print(texto)

    with open(busca+'.txt', 'wb') as f:
        f.write(texto.encode())
    f.close()
