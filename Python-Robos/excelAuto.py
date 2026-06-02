from openpyxl import workbook
from win32com.client import Dispatch


# Cria um novo objeto Workbook (livro de trabalho do Excel)
# Isso cria um arquivo Excel em memória
workbook = workbook()


sheet = workbook.active

# Preenche células específicas da planilha:
# A1 = primeira coluna (A), primeira linha (1)
sheet["A1"] = "hello"
sheet["B1"] = "Youtube"

workbook.save(filename="Hello_youtube.xlxs")

# Cria uma instância da aplicação Excel
# Dispatch("Excel.Application") conecta com o Excel instalado no Windows
# Similar a abrir o Excel manualmente, mas programaticamente
xl = Dispatch("Excel.Application")


xl.Visible = True # Torna o Excel visível na tela


# Abre o arquivo Excel que acabamos de criar
# Precisa do caminho completo ou arquivo no diretório atual
wb = xl.Workbooks.Open("Hello_youtube.xlsx")



wb.Close()
xl.Quit()
