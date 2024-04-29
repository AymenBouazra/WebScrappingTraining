from bs4 import BeautifulSoup
import requests
import pandas as pd
#for i in range (1,20):
products = []
for i in range(1,20):
    html = requests.get(f'https://www.tunisianet.com.tn/681-pc-portable-gamer?page={i}&order=product.price.asc').text
    soup = BeautifulSoup(html, 'lxml')
    product_articles = soup.find_all('article', class_='product-miniature')
    for article in product_articles:
        link_detail = article.find('a').attrs['href']
        title = article.find('h2', class_='product-title').text
        ref = article.find('span', class_='product-reference').text
        price = article.find('span', class_='price').text[0:-3]
        stock = article.find('div', id='stock_availability').text.strip()
        description = article.find('div', class_='listds').text.strip()
        products.append([title, link_detail, ref, description, price, stock])

print(products)
df = pd.DataFrame(products, columns=['title', 'link_detail', 'ref', 'description', 'price', 'stock'])
df.to_excel('tunisianet-pc-gamer.xlsx')