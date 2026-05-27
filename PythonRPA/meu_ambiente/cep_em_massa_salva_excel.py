import http.client
import json
import pandas as  pd


def obter_endereco_por_cep(cep):
    conexao = http.client.HTTPSConnection("viacep.com.br")
    conexao.request("GET", f"/ws/{cep}/json/")
    resposta = conexao.getresponse()

    if resposta.status != 200:
        conexao.close()

        return None
    dados = resposta.read()

    endereco = json.loads(dados.decode("utf-8"))

    conexao.close()

    return endereco if  "erro" not in endereco else None

caminho_planilha = "CEP.xlsx"

planilha_ceps = pd.read_excel(caminho_planilha, sheets_name = 'CEP')
ceps = planilha_ceps['CEP'].dropna()

resultados = pd.DataFrame(columns=['CEP', 'Logradouro', 'Bairro', 'Cidade', 'UF'])

for cep in ceps:
    endereços = obter_endereco_por_cep(str(cep).replace('-', '')  )
    resultados = resultados.append(endereços, ignore_index=True)
