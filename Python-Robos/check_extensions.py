
import os
import re

# Define o caminho padrão onde o VS Code Server armazena as extensões quando
# Estou usando o ambiente WSL (Linux Subsystem for Windows).
# A variável EXTENSIONS_PATH armazena este caminho como uma string.
# O símbolo '~' (til) representa o diretório home do usuário no Linux.
# A função os.path.expanduser() é usada para converter '~' no caminho completo
# do diretório home (ex: '/home/seu_usuario/').
EXTENSIONS_PATH = os.path.expanduser('~/.vscode-server/extensions/')

# Define a função principal que executará a lógica da automação.
# Ela recebe o 'caminho' do diretório de extensões como argumento.
def listar_extensoes_vscode(caminho):
    """
    Função: listar_extensoes_vscode
    Objetivo: Lista e formata os nomes das extensões instaladas no VS Code.
    """
    # Imprime uma mensagem inicial para o usuário saber que o script começou.
    print("Iniciando a verificação de extensões do VS Code...")

    # --- Verificação de Segurança (Fluxo de Controle) ---
    # Verifica se o diretório especificado pelo 'caminho' realmente existe no sistema.
    if not os.path.exists(caminho):
        # Se o caminho não for encontrado, imprime uma mensagem de erro formatada.
        # Utilizamos f-string (f"...") para incluir a variável 'caminho' facilmente.
        print(f"\nERRO: O diretório de extensões não foi encontrado em: {caminho}")
        print("Certifique-se de que o VS Code está instalado e em uso no WSL.")
        # Interrompe a execução da função e retorna.
        return

    # Inicializa uma lista vazia onde armazenaremos os nomes das extensões encontradas.
    extensoes = []

    # --- Início do Processo de Leitura do Diretório (Loop) ---
    # O loop 'for' percorre e lista todos os arquivos e diretórios dentro do 'caminho'.
    for item in os.listdir(caminho):

        # Constrói o caminho completo para o item atual.
        # É uma boa prática usar os.path.join() para garantir a barra correta (/)
        # independentemente do sistema operacional.
        item_path = os.path.join(caminho, item)

        # Verifica se o item atual é um diretório (pasta).
        # Cada extensão instalada é armazenada em sua própria pasta.
        if os.path.isdir(item_path):

            # --- Limpeza do Nome (Expressão Regular) ---
            # O nome da pasta inclui a versão, ex: 'ms-python.python-2023.22.1'.
            # Esta expressão regular busca:
            # r'(.+)' -> Qualquer coisa (nome da extensão) que vem antes do último traço.
            # '-\d+\.\d+\.\d+$' -> O padrão de traço seguido por Números.Pontos.Números no final da string.
            match = re.match(r'(.+)-\d+\.\d+\.\d+$', item)

            # Verifica se a expressão regular encontrou uma correspondência.
            if match:
                # match.group(1) extrai o texto capturado pelo primeiro grupo '(.+)',
                # que é o nome limpo da extensão (ex: 'ms-python.python').
                nome_limpo = match.group(1)
                # Adiciona o nome limpo à nossa lista de extensões.
                extensoes.append(nome_limpo)

    # --- Exibição e Formatação do Resultado ---
    # Imprime um cabeçalho mostrando o número total de extensões encontradas.
    print(f"\n--- {len(extensoes)} Extensões Encontradas ---")

    # set(extensoes): Cria um conjunto (set) a partir da lista, o que remove automaticamente duplicatas
    # (úteis se houver mais de uma versão da mesma extensão listada).
    # sorted(...): Ordena os nomes em ordem alfabética para facilitar a leitura.
    for nome in sorted(set(extensoes)):
        # Imprime cada nome de extensão formatado com um ícone.
        print(f"✅ {nome}")

# --- Ponto de Entrada do Programa ---
# Chama a função principal com o caminho de extensões definido.
# Isso inicia a execução do script.

print("EXTENSIONS_PATH")
listar_extensoes_vscode(EXTENSIONS_PATH)
