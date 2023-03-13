import requests
from fake_useragent import UserAgent

HEADERS = {"User-Agent":UserAgent().random} # получаем рандомный user-agent


input_articl = "104923631"

def parser_csr():
    for i in range(1,15):
        if i < 10:
            i = ("0" + str(i))
        a = (f'https://basket-{i}.wb.ru/vol{input_articl[:4]}/part{input_articl[:6]}/{input_articl}/info/ru/card.json')
        if not requests.get(a,headers=HEADERS).status_code == 404:
            response = requests.get(a,headers=HEADERS).json()
            articl = response.get('nm_id')
            name_articl = response.get('selling')
            brand_name = name_articl.get('brand_name')
            name = response.get('imt_name')
            print(articl)
            print(brand_name)
            print(name)
            break


if __name__ == "__main__":
    parser_csr()




