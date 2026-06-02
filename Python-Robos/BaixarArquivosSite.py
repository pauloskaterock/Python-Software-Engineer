import requests

url = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'
response = requests.get(url)

with open('file.zip', 'wb') as file:
    file.write(response.content)
