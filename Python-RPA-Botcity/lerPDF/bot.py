
# Import for the Desktop Bot
# from botcity.document_processing import *
# import pathlib
# import panda as pd



dados = []



def lerPDF():
    reader = PDFReader()
    parser = reader.read_file('./docs/Contoso_INVOICE_TailSpin.pdf')
   
    
    # Import the packages
    from botcity.document_processing import PDFReader
    
    # Read the file and instantiate the reader
    parser = PDFReader().read_file('docs\docs\Contoso_INVOICE_TailSpin.pdf')
   
    _date = parser.get_first_entry("Date:")
    date = parser.read(_date, 1.380952, -2.1, 3.047619, 3.5)
    print('Date: ' + date)
    
    _bill_to = parser.get_first_entry("Bill to:")
    bill_to = parser.read(_bill_to, 1.148148, -2.3, 6.259259, 4.4)
    print('Bill to: ' + bill_to)

    _contact = parser.get_first_entry("Contact:")
    contact = parser.read(_contact, 1.171053, -1.6, 4.973684, 3.8)
    print('Contact: ' + contact)

    _balance_due = parser.get_first_entry("Balance due:")
    balance_due = parser.read(_balance_due, 1.133333, -1.833333, 1.766667, 3.583333)
    print('Balance due: ' + balance_due)

    arquivos = pathlib.Path('./docs/Contoso_INVOICE_TailSpin.pdf').glob('*.pdf')

    for arquivo in arquivos:
       # print(arquivo)
        lerPDF(arquivo)


dados.append([date, bill_to, contact, balance_due])
# lerPDF()
    
    
    
df = pd.DataFrame(dados, columns=['Date' , 'Bill to', 'Contact', 'Balance due'])
df.to_csv('dados_pdf.csv', sep=',', index=False)



