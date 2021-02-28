from bs4 import BeautifulSoup as bs
import requests as rq

while True:
    busca = input("Digite o tema: ")
    if (busca == 'exit') or (busca == 'sair'):
        break
    else:
        busca = busca.replace(" ", '_')
        url = "https://pt.wikipedia.org/wiki/"+busca
        page = rq.get(url=url)
        soup = bs(page.content, 'html.parser')

        with open(busca+'.txt', 'wb') as f:
            busca = busca.replace("_", ' ')
            print(f'\n:: {busca} ::\n')
            for cont in soup.find_all('p'):
                texto = cont.get_text()
                texto = str(texto)
                print(texto)
                f.write(texto.encode())
        f.close()
