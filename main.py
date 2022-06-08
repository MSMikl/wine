import os

from collections import defaultdict
from datetime import date
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    load_dotenv()
    wines_table_file = os.getenv('XLSX_PATH', 'wines.xlsx')
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    raw_readed_db = pandas.read_excel(wines_table_file, keep_default_na=False, na_values=None)
    wines = defaultdict(list)
    for line in raw_readed_db.values:
        wines[line[0]].append(
                        {
                'Название': line[1],
                'Сорт': line[2],
                'Цена': line[3],
                'Картинка': line[4]
            }
        )
    min_price = raw_readed_db['Цена'].min()

    template = env.get_template('template.html')

    raw_age = date.today().year - 1920
    if raw_age % 100 in range(10, 16):
        age = f'{raw_age} лет'
    elif raw_age % 10 in (2, 3, 4):
        age = f'{raw_age} года'
    elif raw_age% 10 == 1:
        age = f'{raw_age} год'
    else:
        age = f'{raw_age} лет'

    rendered_page = template.render(
        age=age,
        wines=wines,
        min_price=min_price
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()