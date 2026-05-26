3# Importa o módulo http.client que fornece a funcionalidade de
# cliente HTTP para Python, permitindo fazer requisições a servidores web.
import http.client

# Importa o módulo json que fornece métodos para trabalhar com
# dados no formato JSON, um formato comum para troca de dados na web.
import json

def obter_endereco_por_cep(cep):
    """
    Esta função consulta a API do ViaCEP para obter informações de endereço
            com base em um Código de Endereçamento Postal (CEP).

    Parâmetros:
    cep (str): O CEP para o qual o endereço deve ser consultado.

    Retorna:
    dict ou str: Retorna um dicionário contendo as informações do endereço, ou
            uma mensagem de erro se o CEP não for encontrado.
    """

    # Cria uma conexão HTTPS com o servidor 'viacep.com.br', que hospeda a API do ViaCEP.
    # A conexão HTTPS garante que os dados enviados e recebidos
    # sejam criptografados para segurança.
    conexao = http.client.HTTPSConnection("viacep.com.br")

    # Formata e envia uma requisição GET ao servidor ViaCEP.
    # A requisição inclui o CEP fornecido na URL.
    # '/ws/{cep}/json/' especifica o formato da API que inclui o
    # CEP e espera a resposta em formato JSON.
    # O método 'request' realiza a solicitação ao servidor
    # com o método HTTP 'GET'.
    conexao.request("GET", f"/ws/{cep}/json/")

    # Aguarda a resposta do servidor à solicitação feita
    # anteriormente e armazena essa resposta no objeto 'resposta'.
    # O método 'getresponse' retorna um objeto que
    # representa a resposta HTTP recebida do servidor.
    resposta = conexao.getresponse()

    # Lê o conteúdo completo da resposta HTTP, que é
    # enviado pelo servidor em formato de bytes.
    # O método 'read' lê os dados da resposta até que
    # todos os dados sejam recebidos.
    dados = resposta.read()

    # Decodifica os bytes recebidos para uma string em formato UTF-8. UTF-8
    # é um padrão comum para codificação de caracteres.
    # Converte a string JSON decodificada em um dicionário Python
    # usando o método 'loads' do módulo json.
    # Isso permite acessar os dados do JSON como um dicionário comum do Python.
    endereco = json.loads(dados.decode("utf-8"))

    # Encerra a conexão HTTPS com o servidor ViaCEP. Fechar a
    # conexão libera os recursos de rede usados pela conexão.
    conexao.close()

    # Verifica se a chave 'erro' está presente no dicionário de
    # endereço. A presença da chave 'erro' indica que o CEP fornecido não é válido.
    if "erro" not in endereco:

        # Se não houver erro, retorna o dicionário contendo as informações do endereço.
        return endereco

    else:

        # Se houver erro (CEP não encontrado), retorna uma mensagem de erro.
        return "CEP não encontrado."

# Demonstra o uso da função definida

# Especifica um CEP exemplo para consulta
cep_exemplo = "02411-050"

# Utiliza a função para obter o endereço relacionado ao CEP
endereco_resultado = obter_endereco_por_cep(cep_exemplo)

# Exibe o endereço ou a mensagem de erro resultante
print(endereco_resultado)

# https://www.ruacep.com.br/sp/sao-paulo/bairros/
