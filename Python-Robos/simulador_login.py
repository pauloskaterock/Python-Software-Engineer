from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- VARIÁVEIS DE CONFIGURAÇÃO ---
URL_LOGIN = "https://demoqa.com/login"
USERNAME_FICTICIO = "Automacao_Python"
PASSWORD_FICTICIA = "Senha12345!"
DELAY_NAVIGATE = 2  # Tempo de espera para a página carregar

def simular_login(url: str, user: str, password: str):
    """
    Executa a automação de login usando Selenium.

    Args:
        url (str): URL da página de login.
        user (str): Username a ser digitado.
        password (str): Senha a ser digitada.
    """
    print("--- INÍCIO DA AUTOMAÇÃO WEB ---")

    # 1. INICIALIZAÇÃO DO DRIVER
    # Usamos o ChromeDriverManager para garantir que o WebDriver correto seja
    # baixado e configurado automaticamente, simplificando a implementação.
    print("Iniciando navegador Chrome...")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # 2. NAVEGAR PARA O SITE
        print(f"Navegando para: {url}")
        driver.get(url)
        driver.maximize_window() # Prática para garantir que todos os elementos estejam visíveis
        time.sleep(DELAY_NAVIGATE)

        # 3. ENCONTRAR E PREENCHER O CAMPO USERNAME
        # Usamos By.ID, pois é um seletor rápido e único.
        print(f"Preenchendo Username: {user}")
        campo_usuario = driver.find_element(By.ID, "userName")
        campo_usuario.send_keys(user)
        time.sleep(DELAY_ACTION)

        # 4. ENCONTRAR E PREENCHER O CAMPO PASSWORD
        print("Preenchendo Password...")
        campo_senha = driver.find_element(By.ID, "password")
        campo_senha.send_keys(password)
        time.sleep(DELAY_ACTION)

        # 5. CLICAR NO BOTÃO DE LOGIN
        print("Clicando no botão Login...")
        botao_login = driver.find_element(By.ID, "login")
        botao_login.click()

        # 6. VERIFICAÇÃO SIMPLES (MELHOR PRÁTICA)
        # O robô espera um momento para ver o resultado do login (sucesso ou falha).
        time.sleep(DELAY_NAVIGATE * 2)

        print("URL Atual após o Login:", driver.current_url)
        print("--- AUTOMAÇÃO CONCLUÍDA: Login Simulado ---")

    except Exception as e:
        print(f"Ocorreu um erro durante a automação: {e}")

    finally:
        # 7. FECHAR O NAVEGADOR
        # É crucial fechar o driver para liberar recursos.
        print("Fechando o navegador...")
        driver.quit()


if __name__ == "__main__":
    # Define um pequeno atraso de ação para fins didáticos
    DELAY_ACTION = 0.5
    simular_login(URL_LOGIN, USERNAME_FICTICIO, PASSWORD_FICTICIA)
