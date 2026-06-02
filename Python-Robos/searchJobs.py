from selenium import webdriver
from selenium.webdriver.commom.by import by
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_.chrome.import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.commom.keys import keys
import time

# variaveis de configuração

print ("Starting Robo SearchJobs")
URL_GOOGLE = "https://www.google.com"

# Termo de pesquisa
TERMO_PESQUISA = "RPA Developer Remote Internacional Jobs"

DELAY_NAVIGATE = 5 # tempo de espera para o google carregar
DELAY_ACTION = 3 # delay entre as açoes do Robo

def iniciar_pesquisa(url: str, termo: str):
  """
    Inicia o navegador, navega até o Google, insere e executa a pesquisa.

    Args:
        url (str): URL de destino (Google).
        termo (str): String a ser pesquisada.
    """
  print("---Robo SearchJobs Iniciando a Pesquisa")

  # Iniciando o Driver
  print("Iniciando o Navegador Chrome")
  service = ChromeService(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service)


  try:
  # navega para o google
    print(f"Navegando para: {url}")
    driver.get(url)
    time.sleep(DELAY_NAVIGATE)

  # encontrar e preencher a pesquisa
  # Usamos By.NAME para localizar a caixa de pesquisa ('q' é o nome padrão do Google)
    print(f"Localizando caixa de pesquisa e digitando: '{termo}'")
    caixa_pesquisa = driver.find_element(By.NAME, "q")

    # insere e texto e simula a pesquisa
    caixa_pesquisa.send_keys(termo + Keys.ENTER)
    time.sleep(DELAY_NAVIGATE) # aguardo os resultados carregarem
    print("Pesquisa executada. Verifique os resultados")

  except Except as e:
    print(f"Ocorreu um erro durante a execução do robo SearchJobs {e}")

  finally:
    # garante que o navegador feche apos a visualização
    print("\nManter navegador aberto por  15 segundos")
    time.sleep(15)
    driver.quit()
  print("---Robo SearchJobs concluindo a pesquisa")
if __name__ == "__main__":
  iniciar_pesquisa(URL_GOOGLE, TERMO_PESQUISA)
