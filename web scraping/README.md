# Web Scraping

A primeira coisa que precisamos fazer para realizar o web scrap é baixar a página. Podemos baixar as páginas utilizando a biblioteca requests do Python. A biblioteca requests fará uma solicitação GET ao servidor, que fará o download dos conteúdos HTML da página solicitada para nós. Existem vários tipos de solicitação diferentes que podemos realizar utilizando a biblioteca requests – GET é apenas um deles.

Nós podemos utilizar a biblioteca BeautifulSoup para analisar esse documento e extrair o texto das tags. Primeiro, nós temos que importar a biblioteca e criar uma instância da classe BeautifulSoup para analisar o documento.
