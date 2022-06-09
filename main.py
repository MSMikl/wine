import os

from collections import defaultdict
from datetime import date
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    established_at = 1920
    load_dotenv()
    wines_table_file = os.getenv('XLSX_PATH', 'wines.xlsx')
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    wines_from_excel = (
        pandas
        .read_excel(wines_table_file, keep_default_na=False, na_values=None)
        .to_dict('records')
    )
    wines = defaultdict(list)
    for line in wines_from_excel:
        wines[line['Категория']].append(line)

    template = env.get_template('template.html')

    age_in_years = date.today().year - established_at
    if age_in_years % 100 in range(10, 16):
        age = f'{age_in_years} лет'
    elif age_in_years % 10 in (2, 3, 4):
        age = f'{age_in_years} года'
    elif age_in_years% 10 == 1:
        age = f'{age_in_years} год'
    else:
        age = f'{age_in_years} лет'

    rendered_page = template.render(
        age=age,
        wines=wines
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()