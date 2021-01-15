# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import speech_recognition as sr
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import requests as rq
import string
import random
import time
import os

r = sr.Recognizer()

bot = ChatBot('Sexta-feira')
bot.set_trainer(ListTrainer)
bot.train(['Oi',
           'Olá',
           'Olá',
           'Oi',
           'Tudo bem?',
           'Tudo, e com você?',
           'Estou bem',
           'Que bom', ])


def recVoz(r):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            speech = r.recognize_google(audio, language='pt-BR')
            return speech
    except sr.UnknownValueError:
        print('Erro de reconhecimento de fala')
        time.sleep(2)
        main()


def piadas():
    aleatorio = random.randint(1, 7)
    url = 'https://www.piadas.com.br'
    page = rq.get(url=url, timeout=2)
    soup = bs(page.content, 'html.parser')
    if aleatorio == 1:
        conteudo = soup.find(class_="views-row views-row-2 views-row-even")
    elif aleatorio == 2:
        conteudo = soup.find(class_="views-row views-row-3 views-row-even")
    elif aleatorio == 3:
        conteudo = soup.find(class_="views-row views-row-4 views-row-even")
    elif aleatorio == 4:
        conteudo = soup.find(class_="views-row views-row-5 views-row-even")
    elif aleatorio == 5:
        conteudo = soup.find(class_="views-row views-row-6 views-row-even")
    elif aleatorio == 6:
        conteudo = soup.find(class_="views-row views-row-7 views-row-even")
    elif aleatorio == 7:
        conteudo = soup.find(class_="views-row views-row-8 views-row-even")
    piada = conteudo.get_text()
    print('Sexta-feira: ...')
    main()


def pass_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def pesqGoogle():
    print("Sexta-feira: ...")
    speech = recVoz(r)
    print('Você: ', speech)
    speech = speech.replace(" ", '+')
    url = "https://www.google.com.br/search?q="+speech
    os.system(
        "cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe "+url)
    main()


def pesqYoutube():
    print("Sexta-feira: ...")
    speech = recVoz(r)
    print('Você: ', speech)
    video = speech.replace(" ", '+')
    url = "https://www.youtube.com/results?search_query="+video
    pesquisa = (u"Segue vídeos com o tema "+speech)
    tts.Speak(pesquisa)
    os.system(
        "cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe "+url)
    main()


def wikipedia():
    print('Sexta-feira: Qual tema deseja pesquisar?')
    pesquisa = (u"Qual tema deseja pesquisar?")
    tts.Speak(pesquisa)
    speech = recVoz(r)
    print('Você: ', speech)
    busca = speech.replace(" ", '_')
    url = "https://pt.wikipedia.org/wiki/"+busca
    page = rq.get(url=url)
    soup = bs(page.content, 'html.parser')
    conteudo = soup.find(id="mw-content-text")
    paragrafo = conteudo.find('p')
    texto = paragrafo.get_text()
    print('Sexta-feira: '+texto)
    pesquisa = (u""+texto)
    tts.Speak(pesquisa)

    def write(texto, busca, encoding='utf-8', errors='strict'):
        data = str(texto).encode(encoding, errors=errors)
        try:
            with open(busca, 'wb') as f:
                f.write(data)
        except IOError as e:
            if e.errno == 2:
                os.makedirs(os.path.dirname(busca), exist_ok=True)
                return write(texto, busca, encoding, errors)
            else:
                raise e
    main()


def traduzir():
    print('Fale o que deseja traduzir...')
    speech = recVoz(r)
    print('Você: ', speech)
    texto = speech.replace(" ", '%20')
    origem = 'pt'
    destino = 'en'
    url = "https://translate.google.com.br/?hl=pt-BR#"+origem+"/"+destino+"/"+texto
    os.system(
        "cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe "+url)
    main()


def treinoExtra(bot):
    print('Treinando Diálogo\n')
    titulo = (u"Treinando Diálogo")
    tts.Speak(titulo)

    print('\nFale uma pergunta: ')
    pergunta = (u"Fale uma pergunta")
    tts.Speak(pergunta)
    print('Bot: ...')
    speech = recVoz(r)
    print('Você: ', speech)
    pergunta = speech

    print('\nFale a resposta: ')
    resposta = (u"Fale a resposta")
    tts.Speak(resposta)
    print('Bot: ...')
    speech = recVoz(r)
    print('\nVocê: ', speech)
    resposta = speech

    extra = [pergunta, resposta]
    bot.set_trainer(ListTrainer)
    bot.train(extra)


def main(args):
    os.system('cls')
    print('\n\t\t.:: Assistente Virtual - Beta - by Daniel M. Alves ::.\n\n')

    try:

        while True:
            os.system("espeak - vpt - -stdout 'Fale algo...' | aplay")
            speech = recVoz(r)
            print('Você: ', speech)

            if speech == "pesquisar" or speech == "pesquisar no google" or speech == "pesquisar no Google":
                pesqGoogle()
            elif speech == "pesquisar no youtube" or speech == "pesquisar no YouTube" or speech == "Youtube":
                pesqYoutube()
            elif speech == "pesquisar no Wikipédia" or speech == "Wikipédia":
                wikipedia()
            elif speech == "traduzir" or speech == "translate" or speech == "Translator":
                traduzir()
            elif speech == "treinar" or speech == "treinar dialogo":
                treinoExtra(bot)
            elif speech == "estou com fome":
                url = "https://www.google.com.br/maps/search/Restaurantes/@-20.3118374,-40.3248965,16z/data=!4m7!2m6!3m5!1sRestaurantes!2s-20.3119,+-40.3269!4m2!1d-40.3269354!2d-20.3119305"
                os.system(
                    'cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe '+url)
                main()
            elif speech == "procurar" or speech == "search for" or speech == "Google maps" or speech == "mapa" or speech == "maps" or speech == "procurar em Vitória" or speech == "procurar nas proximidades":
                print('Sexta-feira: ...')
                speech = recVoz(r)
                print('Você: ', speech)
                busca = speech.replace(" ", '+')
                url = 'https://www.google.com.br/maps/search/' + \
                    busca+'/@-20.2869951,-40.3284409,13z'
                os.system(
                    'cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe "'+url+'" ')
                main()
            elif speech == "clima para hoje" or speech == "clima" or speech == "weather":
                time.sleep(2)
                url = "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/84/vitoria-es"
                page = rq.get(url=url, timeout=2)
                soup = bs(page.content, 'html.parser')
                content = soup.find(id="tempMin0")
                minima = content.get_text()
                content = soup.find(id="tempMax0")
                maxima = content.get_text()
                content = soup.find(id="content0")
                classe = content.find(class_="small-4 left rain-block")
                prob = classe.get_text()
                content = soup.find(id="content0")
                classe = content.find(class_="left font14 txt")
                descricao = classe.get_text()
                tempo = (u"Minima de "+minima + " e máxima de "+maxima)
                tts.Speak(tempo)
                print(tempo)
                chuva = (u"Probabilidade de "+prob)
                tts.Speak(chuva)
                desc = (u""+descricao)
                tts.Speak(desc)
                print(desc)
                main()
            elif speech == "clima para amanhã" or speech == "clima para amanhã em Vitória" or speech == "clima amanhã":
                time.sleep(2)
                url = "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/84/vitoria-es"
                page = rq.get(url=url, timeout=2)
                soup = bs(page.content, 'html.parser')
                content = soup.find(id="tempMin1")
                minima = content.get_text()
                content = soup.find(id="tempMax1")
                maxima = content.get_text()
                content = soup.find(id="content1")
                classe = content.find(class_="small-4 left rain-block")
                prob = classe.get_text()
                content = soup.find(id="content1")
                classe = content.find(class_="left font14 txt")
                descricao = classe.get_text()
                tempo = (u"Minima de "+minima + " e máxima de "+maxima)
                tts.Speak(tempo)
                print(tempo)
                chuva = (u"Probabilidade de "+prob)
                tts.Speak(chuva)
                desc = (u""+descricao)
                tts.Speak(desc)
                print(desc)
                main()
            elif speech == "curiosidades do dia" or speech == "curiosidades":
                url = 'https://pt.wikipedia.org/wiki/Wikipédia:Página_principal'
                page = rq.get(url=url)
                soup = bs(page.content, 'html.parser')
                conteudo = soup.find(id="mf-efemérides")
                texto = conteudo.get_text()
                print('Sexta-feira: ...')
                pesquisa = (u""+texto)
                tts.Speak(pesquisa)
                main()
            elif speech == "comparar preços" or speech == "pesquisar produto" or speech == "comparar preço" or speech == "pesquisar produtos":
                pesquisa = (u"Qual o produto desejado?")
                tts.Speak(pesquisa)
                speech = recVoz(r)
                print('Você: ', speech)
                busca = speech.replace(" ", '+')
                url = "https://www.google.com.br/search?tbm=shop&q="+busca
                print("Segue lista com comparação de preços de "+speech+"")
                pesquisa = (u"Segue lista com comparação de preços de "+speech)
                tts.Speak(pesquisa)
                os.system(
                    'cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe "'+url+'" ')
                main()
            elif speech == "tocar músicas" or speech == "reproduzir músicas" or speech == "tocar louvores":
                os.system(
                    'cd C:\\Program Files\\MPC-HC && .\\mpc-hc64.exe C:\\Users\\danie\\Music\\Gospel\\*.mp3')
                main()
            elif speech == "tocar música para relaxar" or speech == "tocar uma música calma" or speech == "tocar música relaxante":
                os.system(
                    'cd C:\\Program Files\\MPC-HC && .\\mpc-hc64.exe C:\\Users\\danie\\Music\\Sons de Meditação e Relaxamento\\Musica_Para_Relaxar.mp3')
                main()
            elif speech == "gerar senha":
                print("Senha: ", pass_generator())
                time.sleep(5)
                main()
            elif speech == "Abrir filmes" or speech == "abrir filmes" or speech == "abrir filme" or speech == "assistir filmes":
                stremio = (u"Abrindo programa de filmes")
                tts.Speak(stremio)
                stremio = 'C:\\Users\\danie\\AppData\\Local\\Programs\\LNV\\Stremio-4\\stremio.exe'
                os.startfile(stremio)
                main()
            elif speech == "me conte uma piada" or speech == "Me conte uma piada" or speech == "piada":
                piadas()
                main()
            elif speech == "fechar" or speech == "sair" or speech == "close":
                print("Encerrando sessão...")
                exit()
            else:
                response = bot.get_response(speech)
                print('Sexta-feira:', response)
                resposta = (u""+str(response))
                tts.Speak(resposta)
                main()
    except:
        print('Erro de excesão')
        os.system('pause')


if __name__ == "__main__":
    main()
