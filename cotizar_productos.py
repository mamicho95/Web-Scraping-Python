import requests
from bs4 import BeautifulSoup as b

products = []

class Avena:
    def __init__(self, price='', marketname='', url=''):
        self.name        = 'Avena Instananea'
        self.brand       = 'Vivo'
        self.price       = price
        self.quantity    = '800 g'
        self.marketname  = marketname
        self.url         = url        
    def __str__(self) -> str:
        return f'Nombre: {self.name}\nMarca: {self.brand}\nPrecio: {self.price}\nCantidad: {self.quantity}\nLink: {self.url}' 

def getContentUrl(url):
    html    = requests.get(url)
    content = html.content
    soup    = b(content, features='lxml')
    return soup


url         = 'https://www.lider.cl/supermercado/product/Vivo-Avena-Instananea/834061'
content     = getContentUrl(url)
marketname  = 'Lider'
price       = content.find('p',{'itemprop':"lowPrice"}).text

products.append (Avena(
    price       = price,
    marketname  = marketname,
    url         = url
    ))

url         = 'https://www.unimarc.cl/product/avena-instantanea-vivo-800-gr'
content     = getContentUrl(url)
marketname  = 'Unimarc'
price       = content.find('div',{'class':"Text_text__cB7NM Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--semibold__MukSj Text_text--3xl__tLA7o Text_text--guardsman-red__wr1D8 Text_text__cursor--auto__cMaN1 Text_text--none__zez2n"}).text

products.append (Avena(
    price       = price,
    marketname  = marketname,
    url         = url
    ))

url         = 'https://www.jumbo.cl/avena-instantanea-vivo-900-g/p'
content     = getContentUrl(url)
marketname  = 'Jumbo'
price       = content.find('main').find('span',{'class':'product-sigle-price-wrapper'}).text
products.append (Avena(
    price       = price,
    marketname  = marketname,
    url         = url
    ))    

for p in products:
    print('========================================')
    print(p)
    