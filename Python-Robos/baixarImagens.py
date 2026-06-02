
# Baixar e Salvar Imagens com Requests e Pillow

import requests
from PIL import Image
from io import BytesIO

url = 'https://example.com/image.jpg'
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.save('imagem.jpg')
