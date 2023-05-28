import requests

url="https://raw.githubusercontent.com/mwitiderrick/stockprice/master/NSE-TATAGLOBAL.csv"
file_name="stock.csv"
response=requests.get(url)
response.raise_for_status()
with open(file_name,'wb') as file:
    file.write(response.content)


print('Dataset downloaded successfully.')
