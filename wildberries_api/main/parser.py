import requests
import pandas
from fake_useragent import UserAgent

HEADERS = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
} # получаем рандомный user-agent



def parser_csr(input_article:str):
    for i in range(1,20):
        if i < 10:
            i = ("0" + str(i))
        a = f'https://basket-{i}.wb.ru/vol{input_article[:-5]}/part{input_article[:-3]}/{input_article}/info/ru/card.json'
        if not requests.get(a,headers=HEADERS).status_code == 404:
            response = requests.get(a,headers=HEADERS).json()
            article = response.get('nm_id')
            name_article = response.get('selling')
            brand_name = name_article.get('brand_name')
            name = response.get('imt_name')
            data = {
                'name':name,
                'article':article,
                'brand':brand_name
            }
            return data


def extract_data(file)->list:
    article_list=[]
    data = pandas.read_excel(file)
    for article in data.values:
        article_list.append(str(article[0]))
    return article_list


def parser_api(input_data)-> dict or list:
    if type(input_data) is str:
        return parser_csr(input_data)
    else:
        data = []
        article_list=extract_data(input_data)
        for article in article_list:
            data.append(parser_csr(article))
        return data


