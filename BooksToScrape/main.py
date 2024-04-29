from bs4 import BeautifulSoup
import requests
import pandas as pd
books = []
for i in range(1,51):
    html = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html').text
    soup = BeautifulSoup(html, 'lxml')

    ol = soup.find('ol')
    books_articles = ol.find_all('article', class_='product_pod')
    for article in books_articles:
        title = article.find('img').attrs['alt']
        star = article.find('p', class_='star-rating').attrs['class'][-1]
        price = article.find('p', class_='price_color').text
        price = float(price[2:])
        books.append([title, price, star])

df = pd.DataFrame(books, columns=['Title', 'Price', 'Star rating'])
print(df)
df.to_excel('books.xlsx')