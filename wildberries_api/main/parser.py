import requests
from fake_useragent import UserAgent

HEADERS = {"User-Agent":UserAgent().random} # получаем рандомный user-agent


def parser_csr(input_article:str):
    for i in range(1,20):
        if i < 10:
            i = ("0" + str(i))
        a = f'https://basket-{i}.wb.ru/vol{input_article[:4]}/part{input_article[:6]}/{input_article}/info/ru/card.json'
        if not requests.get(a,headers=HEADERS).status_code == 404:
            response = requests.get(a,headers=HEADERS).json()
            article = response.get('nm_id')
            name_article = response.get('selling')
            brand_name = name_article.get('brand_name')
            name = response.get('imt_name')
            print(article)
            print(brand_name)
            print(name)
            break







