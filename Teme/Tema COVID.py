import pandas as pd
import requests
from bs4 import BeautifulSoup

url_list = ['https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00/',
            'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00/',
            'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00/',
            'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00/',
            'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-2/'
            ]

column_names = ['01.03', '02.03', '03.03', '04.03', '05.03']

df = pd.DataFrame()

for idx, url in enumerate(url_list):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all('table')[0]

    dataset = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        dataset.append([x for x in cols if x])

    temp_df = pd.DataFrame(dataset)

    if idx == 0:
        df = temp_df.iloc[:, :3]
        df.columns = ['NR. CRT', 'Judet', '01.03']
    else:
        df[column_names[idx]] = temp_df.iloc[:, 2]

df = df.drop(0)
df.to_excel('Tema_Covid.xlsx', index=False)
