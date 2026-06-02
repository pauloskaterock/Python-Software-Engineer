# Importa as bibliotecas necessárias para realizar conexões HTTP e
# trabalhar com dados em JSON e tabelas
import http.client  # Biblioteca para realizar requisições HTTP
import json         # Biblioteca para manipular dados em formato JSON
import pandas as pd # Biblioteca para manipulação de dados tabulares

def obter_endereco_por_cep(cep):

    """
    Esta função consulta uma API para obter informações de endereço com
                    base em um Código de Endereçamento Postal (CEP).

    Parâmetros:
    cep (str): O CEP para o qual o endereço deve ser consultado.

    Retorna:
    dict: Retorna um dicionário contendo as informações do endereço, ou
                    None se o CEP não for encontrado ou ocorrer um erro.
    """

    # Estabelece uma conexão HTTPS com o site 'viacep.com.br', que
                    # fornece uma API para consulta de CEPs.
    # 'http.client.HTTPSConnection' é uma classe do módulo http.client do Python
    # que permite criar uma conexão cliente com servidores HTTPS.
    # A string "viacep.com.br" especifica o domínio do servidor ao
                    # qual a conexão é estabelecida.
    conexao = http.client.HTTPSConnection("viacep.com.br")

    # Envia uma requisição GET para a API do ViaCEP, solicitando dados do
                    # endereço associado ao CEP fornecido.
    # O método 'request' da conexão é utilizado para enviar a requisição. 'GET' é
                    # o método HTTP utilizado para solicitar dados de um recurso especificado.
    # 'f"/ws/{cep}/json/"' é a URL específica para a API, onde {cep} será substituído
                    # pelo valor real do CEP passado à função. A resposta esperada é em formato JSON.
    conexao.request("GET", f"/ws/{cep}/json/")

    # Aguarda a resposta do servidor à requisição enviada e armazena essa
                    # resposta na variável 'resposta'.
    # O método 'getresponse' é chamado após 'request' para obter a resposta do
                    # servidor. Esse método retorna uma instância de HTTPResponse.
    resposta = conexao.getresponse()

    # Verifica o status da resposta. Se o status for diferente de 200 (sucesso), retorna None.
    # O status HTTP 200 indica sucesso na requisição HTTP. Qualquer status
                    # diferente (como 404 para "não encontrado" ou 500 para "erro interno do servidor")
    # indica que algo deu errado com a solicitação, que pode ser desde
                    # um CEP inexistente até problemas no servidor.
    # 'resposta.status' acessa o código de status da resposta HTTP recebida.
    if resposta.status != 200:

        # Fecha a conexão antes de retornar. 'close()' é um método para
                    # liberar explicitamente a conexão.
        conexao.close()

        # Retorna 'None' para indicar que a requisição não foi
                    # bem-sucedida e não há dados para processar.
        return None

    # Lê os dados da resposta, que são recebidos em formato de bytes.
    # O método 'read' de um objeto HTTPResponse lê o corpo da resposta e retorna os dados.
    # A resposta é geralmente retornada em bytes, o que significa que
                    # precisará ser decodificada para string antes de ser convertida de JSON.
    dados = resposta.read()


    # Converte os dados de bytes para uma string JSON e depois
                    # carrega essa string como um dicionário Python.
    # A decodificação é feita em UTF-8, que é um padrão para caracteres latinos.
    endereco = json.loads(dados.decode("utf-8"))

    # Fecha a conexão HTTPS com o servidor ViaCEP, liberando os recursos de rede.
    conexao.close()

    # Verifica se a chave 'erro' está no dicionário de endereço, indicando que o CEP não foi encontrado.
    # Se 'erro' não estiver presente, retorna o dicionário com os dados do endereço.
    # Se 'erro' estiver presente, retorna None, indicando que o endereço para o CEP fornecido não existe.
    return endereco if "erro" not in endereco else None



# Define o caminho do arquivo Excel que contém os dados. Este arquivo deve
# estar acessível no mesmo diretório do script ou o caminho deve ser
# ajustado adequadamente.
caminho_planilha = "CEP.xlsx"

# Utiliza a função read_excel do pandas para carregar especificamente a aba 'CEP' do arquivo Excel.
# O argumento 'sheet_name' especifica qual aba da planilha deve ser lida. Neste caso, a aba com o nome 'CEP'.
# A função retorna um objeto DataFrame, que é uma estrutura de dados bidimensional, semelhante a uma tabela,
# onde cada coluna representa uma variável e cada linha representa uma observação.
planilha_ceps = pd.read_excel(caminho_planilha, sheet_name='CEP')

# A partir do DataFrame carregado, seleciona-se apenas a coluna 'CEP'.
# O método dropna() é aplicado à série de dados (uma dimensão do DataFrame)
            # para remover qualquer linha que contenha um valor nulo (NaN).
# Valores nulos em dados de CEP podem ocorrer devido a erros de
            # entrada de dados ou células vazias na planilha.
# Remover essas entradas é crucial para evitar erros durante a consulta dos endereços.
ceps = planilha_ceps['CEP'].dropna()

# Cria um novo DataFrame vazio chamado 'resultados'. Este DataFrame é
            # inicializado com colunas específicas.
# As colunas são: 'CEP', 'Logradouro', 'Bairro', 'Localidade', 'UF'.
# Este DataFrame será usado para armazenar os resultados da
            # consulta ao serviço de API que retorna os endereços.
# Cada coluna é destinada a armazenar uma parte específica do endereço:
# - 'CEP' para o código postal,
# - 'Logradouro' para o nome da rua ou avenida,
# - 'Bairro' para o setor ou região,
# - 'Localidade' para a cidade ou localidade,
# - 'UF' para a unidade federativa ou estado.
resultados = pd.DataFrame(columns=['CEP', 'Logradouro', 'Bairro', 'Localidade', 'UF'])


# Este bloco de código itera sobre cada CEP extraído da planilha Excel.
# O loop for percorre a série 'ceps' que contém todos os CEPs
        # válidos (não nulos) lidos da planilha.
for cep in ceps:

    # A função 'obter_endereco_por_cep' é chamada com o CEP atual como argumento.
    # Antes de passar o CEP para a função, quaisquer hífens são
                # removidos usando 'str(cep).replace('-', '')'.
    # Isso é necessário porque alguns formatos de CEP podem incluir
                # hífens que não são aceitos por algumas APIs de consulta de endereço.
    # A função retorna um dicionário com os dados do endereço, se
                # encontrado, ou None, se ocorrer um erro ou o CEP não existir.
    endereco = obter_endereco_por_cep(str(cep).replace('-', ''))

    # Este if verifica se um objeto 'endereco' válido foi retornado pela função.
    # Um objeto válido significa que o dicionário contém dados do
                # endereço e não possui a chave 'erro'.
    if endereco:

        # Um novo DataFrame é criado com os dados do endereço. Este
                    # DataFrame é temporário e contém apenas uma linha.
        # Os dados do endereço são organizados em colunas correspondentes às
                    # partes do endereço: CEP, Logradouro, Bairro, Localidade e UF.
        # Os valores são extraídos do dicionário 'endereco' usando o
                    # método '.get()', que também permite especificar um valor padrão ('')
        # para o caso de a chave não estar presente no dicionário, evitando assim erros.
        nova_linha = pd.DataFrame([{
            'CEP': cep,
            'Logradouro': endereco.get('logradouro', ''),
            'Bairro': endereco.get('bairro', ''),
            'Localidade': endereco.get('localidade', ''),
            'UF': endereco.get('uf', '')
        }])

        # O DataFrame 'resultados', que foi inicializado fora do loop, é
                    # então atualizado para incluir a nova linha.
        # A função 'pd.concat' é usada para concatenar a 'nova_linha' ao DataFrame 'resultados'.
        # O parâmetro 'ignore_index=True' é crucial aqui: ele instrui o
                    # pandas a reindexar o DataFrame resultante,
        # o que significa que os índices serão renumerados de forma contínua,
                    # evitando duplicações ou lacunas nos índices.
        resultados = pd.concat([resultados, nova_linha], ignore_index=True)


# Este bloco de código é responsável por salvar os dados coletados e
                # processados no DataFrame 'resultados' de volta no arquivo Excel.
# A operação de salvamento é realizada utilizando o contexto de
                # gerenciamento de recursos do Python (o bloco 'with'), que
                # garante o fechamento adequado do arquivo após a conclusão das operações.

# O objeto 'pd.ExcelWriter' é utilizado para escrever em arquivos Excel.
                # Ele é configurado com vários parâmetros:
# 'caminho_planilha' é o caminho para o arquivo Excel que será escrito.
                # Este é o mesmo arquivo de onde os CEPs foram originalmente lidos.
# 'engine='openpyxl'' especifica que a biblioteca openpyxl deve ser usada como o
                # motor para escrever em arquivos Excel. Openpyxl permite trabalhar com arquivos .xlsx.
# 'mode='a'' configura o ExcelWriter para abrir o arquivo no modo de anexação ('a' de append).
                # Isso é crucial para garantir que as abas existentes no arquivo Excel não
                # sejam excluídas quando novos dados forem adicionados.
# 'if_sheet_exists='replace'' instrui o ExcelWriter a substituir a aba se ela já
                # existir. Isso é útil quando queremos atualizar os dados na aba 'Dados' com
                # novas informações sem criar múltiplas abas com o mesmo nome.
with pd.ExcelWriter(caminho_planilha, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:

    # O método 'to_excel' do DataFrame 'resultados' é chamado para escrever seus
                # dados na aba chamada 'Dados' do arquivo Excel.
    # 'sheet_name='Dados'' especifica o nome da aba onde os dados devem ser salvos.
    # 'index=False' é usado para indicar que os índices do DataFrame (que são
                # automaticamente criados pelo pandas) não devem ser salvos no arquivo
                # Excel. Isso ajuda a manter o arquivo de saída limpo e focado apenas
                # nos dados sem colunas adicionais de índice.
    resultados.to_excel(writer, sheet_name='Dados', index=False)


# Imprime uma mensagem indicando que os endereços foram salvos na
                # aba 'Dados' do arquivo especificado.
print("Endereços salvos na aba 'Dados' da planilha 'CEP.xlsx'.")
