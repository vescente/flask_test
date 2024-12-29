import requests
import json
from flask import Flask


# text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text

# curr = json.loads(text)


# for currency in curr['Valute']:
#     print(f"{currency}: {curr['Valute'][currency]['Name']} - {curr['Valute'][currency]['Value']}")

app = Flask(__name__)

@app.route('/')
def hello_world():
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    curr = json.loads(text)

    result = ''
    for currency in curr['Valute']:
        result += str(currency) + ': ' + str(curr['Valute'][currency]['Name']) + ' - ' + str(curr['Valute'][currency]['Value']) + '<br>'
    return result

if __name__ == '__main__':
    app.run()