import requests
import pandas as pd
from bs4 import BeautifulSoup



ano = 2017
serie = "a"
url = f"https://www.mg.superesportes.com.br/campeonatos/2017/brasileirao/serie-a/-{serie}/{ano}"

pagina = requests.get(url)
soup = BeautifulSoup(pagina.content, 'html.parser')
indicador = soup.select(' .hidden-sxs')[0].text
times = list(map(lambda time: time.select(' .hidden-sxs')[0].text, indicador))
