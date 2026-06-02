# import pandas as pd


# scraper = pd.read_html("https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2017_-_S%C3%A9rie_A")

# scraper

# # for i, table in enumerate(scraper):
# #   print("------------")
# #   print(1)
# #   print(table)


# df = scraper[0]
# df.to_csv('brasileirao', index=False)

# df_scraped_file = pd.read_csv('brasileirao.csv')
# df_scraped_file



import pandas as pd
import requests

URL = "https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2017_-_S%C3%A9rie_A"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

#  Requisição HTTP controlada
response = requests.get(URL, headers=headers)
response.raise_for_status()

#  Pandas faz o parsing do HTML já carregado
scraper = pd.read_html(response.text)

print(f"Tabelas encontradas: {len(scraper)}")

#  Seleciona a primeira tabela
df = scraper[0]

#  Salva corretamente
df.to_csv("brasileirao.csv", index=False, encoding="utf-8-sig")

#  Reabre para validação
df_scraped_file = pd.read_csv("brasileirao.csv")

print(df_scraped_file.head())
