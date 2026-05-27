# Importa o módulo http.client, que fornece classes e métodos
        # para realizar requisições HTTP e HTTPS.
import http.client

# Importa o módulo json, essencial para trabalhar com dados no
        # formato JSON, que é um formato padrão para a troca de dados na internet.
import json

# Importa o módulo pandas, uma biblioteca robusta para manipulação e
        # análise de dados em Python, particularmente útil para
        # trabalhar com estruturas de dados tabulares como DataFrames.
import pandas as pd

def obter_endereco_por_cep(cep):

    """
    Esta função consulta uma API web para obter informações de
                endereço associadas a um CEP especificado.

    Parâmetros:
    cep (str): O Código Postal para o qual o endereço será buscado.

    Retorna:
    dict: Um dicionário contendo os detalhes do endereço se o CEP
                for válido, ou retorna None se houver algum erro.
    """

    # Estabelece uma conexão HTTPS com o servidor 'viacep.com.br', que
                # oferece uma API gratuita para consulta de CEPs no Brasil.
    conexao = http.client.HTTPSConnection("viacep.com.br")

    # Formata e envia uma requisição GET ao servidor. A URL formada
                # inclui o CEP e especifica que a resposta deve ser em JSON.
    conexao.request("GET", f"/ws/{cep}/json/")

    # Espera pela resposta do servidor e a captura no objeto 'resposta'.
    resposta = conexao.getresponse()

    # Lê os dados da resposta, que são enviados em formato de bytes, que é
                # uma sequência de bytes que precisa ser decodificada para ser lida.
    dados = resposta.read()

    # Converte os bytes para uma string usando UTF-8, que é um padrão de
                # codificação de caracteres, e então converte essa string
                # de JSON para um dicionário Python.
    endereco = json.loads(dados.decode("utf-8"))

    # Fecha a conexão com o servidor, liberando os recursos de rede associados.
    conexao.close()

    # Retorna o dicionário contendo as informações de endereço ou None
                # se ocorrer algum erro ou o CEP não existir.
    return endereco


def salvar_endereco_excel(endereco, nome_arquivo="endereco.xlsx"):

    """
    Salva os dados de endereço obtidos da API em um arquivo Excel, cada
                parte do endereço em uma coluna separada.

    Parâmetros:
    endereco (dict): Dicionário contendo os dados do endereço.
    nome_arquivo (str): Nome do arquivo Excel para salvar os dados.
                Se não especificado, 'endereco.xlsx' será usado.
    """

    # Verifica se o dicionário contém a chave 'erro'. A presença dessa
                # chave indica que o CEP não foi encontrado.
    if "erro" not in endereco:

        # Cria um DataFrame do pandas a partir de uma lista que contém o
                # dicionário de endereço, estruturando os dados em formato tabular.
        df = pd.DataFrame([endereco])

        # Salva o DataFrame em um arquivo Excel. 'index=False' significa que o
                # índice do DataFrame não será salvo, mantendo o arquivo
                # limpo apenas com os dados.
        df.to_excel(nome_arquivo, index=False)

        # Imprime uma mensagem de sucesso, indicando onde os dados foram salvos.
        print(f"Dados salvos com sucesso no arquivo {nome_arquivo}")

    else:

        # Se a chave 'erro' estiver presente, imprime uma mensagem de erro.
        print("Não foi possível salvar os dados: CEP não encontrado.")

# Demonstração de como as funções podem ser usadas:
cep_exemplo = "03195-970"  # Um CEP de exemplo para demonstração.

# Usa a função para consultar o endereço.
endereco_resultado = obter_endereco_por_cep(cep_exemplo)

# Salva os dados de endereço em um arquivo Excel.
salvar_endereco_excel(endereco_resultado)
