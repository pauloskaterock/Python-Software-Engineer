# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='caminho/para/chromedriver')

# driver.get("https://acme-test.uipath.com/login")

# campo_nome = driver.find_element_by_name("nome")
# campo_nome.send_keys("Seu Nome")

# campo_email = driver.find_element_by_name("email")
# campo_email.send_keys("seuemail@example.com")

# campo_email.send_keys(Keys.RETURN)

# # python  rpa engineer projects


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging

# configuração Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)


print("🤖 RPA - PREENCHIMENTO DE FORMULÁRIOS (CORRIGIDO)")
logging.info('=========================Aplicação iniciada com sucesso.')


# MÉTODO MODERNO  - Sem executable_path! Configuração Chrome Driver
try:
    print(" Configurando ChromeDriver...")
    logging.info('==============================Configurando Chrome Driver.')

    # 1. Usar Service + ChromeDriverManager (automático)
    service = Service(ChromeDriverManager().install())


    # 2. Opções do Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # Maximizar janela
    logging.info('==============================Maximizando Janela.')

    # 3. Inicializar driver CORRETAMENTE
    driver = webdriver.Chrome(service=service, options=options)
    print(" ChromeDriver configurado com sucesso!")


    logging.info('==============================Acessando Web Site.')
    # TESTE 1: Google (para ver se funciona)
    print("\n Testando conexão...")
    driver.get("https://rpachallenge.com/")
    time.sleep(2)
    logging.info('==============================Título: {driver.title}.')
    print(f" Web site carregado! Título: {driver.title}")

    # TESTE 2: Seu formulário (AJUSTE A URL!)
    print("\n Indo para formulário...")

    # URL do SEU formulário (substitua pela sua)
    # Exemplo com Google Forms público:
    form_url = "https://rpachallenge.com/"
    logging.info('===============================web site acessado com sucesso, iniciando preenchimento formulario')

    driver.get(form_url)
    time.sleep(3)  # Aguardar carregamento

    # TENTAR PREENCHER (ajuste os seletores)
    print(" Tentando preencher campos...")

    # Método 1: Por name
    try:
        # Tenta encontrar campo "nome" por name
        campo_nome = driver.find_element(By.NAME, "nome")
        campo_nome.send_keys("Paulo Santos")
        print(" Nome preenchido (por NAME)")
    except:
        print(" Campo 'nome' não encontrado por NAME")

    # Método 2: Por qualquer input de texto
    try:
        campos_texto = driver.find_elements(By.TAG_NAME, "input")
        for campo in campos_texto[:2]:  # Primeiros 2 inputs
            campo_type = campo.get_attribute("type")
            if campo_type in ["text", "email"]:
                campo.send_keys("teste@exemplo.com" if campo_type == "email" else "Teste RPA")
                print(f" Campo {campo_type} preenchido")
    except:
        print(" Não conseguiu preencher por TAG_NAME")

    # Método 3: Por XPath (mais flexível)
    try:
        # Procura qualquer input que aceite texto
        inputs = driver.find_elements(By.XPATH, "//input[@type='text' or @type='email']")
        for i, input_field in enumerate(inputs):
            if i == 0:
                input_field.send_keys("Paulo Santos")
            elif i == 1:
                input_field.send_keys("pauloengenharia5@yahoo.com")
            print(f" Campo {i+1} preenchido via XPath")
    except:
        print(" Não conseguiu preencher por XPath")

    # TENTAR ENVIAR
    print("\n Tentando enviar formulário...")
    try:
        # Pressiona ENTER no último campo
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ENTER)
        print(" Formulário enviado com ENTER")
    except:
        print(" Não conseguiu enviar com ENTER")

    # AGUARDAR E MOSTRAR RESULTADO
    time.sleep(3)
    print(f"\n Página atual: {driver.title}")

    # CAPTURAR SCREENSHOT
    # driver.save_screenshot("resultado_formulario.png")
    # print("📸 Screenshot salvo: resultado_formulario.png")

    # MANTER ABERTO PARA VISUALIZAÇÃO
    input("\n Pressione Enter para fechar o navegador...")

except Exception as e:
    print(f"\n❌ ERRO: {type(e).__name__}")
    print(f"   Mensagem: {e}")

    # DICAS ESPECÍFICAS PARA O ERRO
    if "executable_path" in str(e):
        print("\n SOLUÇÃO: Você está usando API antiga do Selenium!")
        print("   Use: service = Service(ChromeDriverManager().install())")
        print("   Use: driver = webdriver.Chrome(service=service)")

    elif "chromedriver" in str(e).lower():
        print("\n SOLUÇÃO: Problema com ChromeDriver!")
        print("   Execute: pip install --upgrade webdriver-manager")
        print("   Feche todas instâncias do Chrome")

    elif "session not created" in str(e).lower():
        print("\n SOLUÇÃO: Versão do Chrome incompatível!")
        print("   Atualize o Chrome ou reinstale webdriver-manager")

finally:
    # SEMPRE FECHAR O DRIVER
    try:
        driver.quit()
        print(" Navegador fechado")
    except:
        pass

print("\n Script finalizado!")
