import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://bnr.ro/Cursul-de-schimb-524.aspx')
link = BeautifulSoup(req.text, 'html.parser')

main = link.find_all('table', attrs={'class':'cursTable'})

dataset = []
header_list = []
header_list.insert(0, 'Numele Valutei')
header_list.insert(1, 'Prescurtarea Valutei')

for obj in main:
    for table_head in obj.find_all('thead'):
        for table_ths in table_head.find_all('th'):
            for header_data in table_ths.find_all('a'):
                header_list.append(header_data.get_text().replace("\xa0", "."))
    for table_body in obj.find_all('tbody'):
        for table_trs in table_body.find_all('tr'):
            body_list = []
            for idx, td in enumerate(table_trs.find_all('td')):
                if idx == 0:
                    body_list.append(td.get_text().strip())
                else:
                    if td.get_text().strip() != '':
                        body_list.append(td.get_text().replace(',','.'))
            if body_list:
                dataset.append(body_list)

df = pd.DataFrame(dataset, columns=header_list)
df.to_excel('Curs_BNR_Tema.xlsx', index=False)