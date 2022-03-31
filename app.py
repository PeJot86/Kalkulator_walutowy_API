from flask import Flask, render_template, request
import requests
import csv

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/C?format=json')
data = response.json()

dates = {}
 
for i in data:
    dates = (i['rates'])

def export_to_csv():
    with open('Waluty.csv', mode='w', encoding='utf-8') as csv_file:
        fieldnames = ['currency', 'code', 'bid', 'ask']
        csvwriter = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csvwriter.writeheader()
        for n in dates:
            csvwriter.writerow(n)

#export_to_csv()

money = []

for i in dates:
    money.append (i['ask'])

exchange_rate ={
'USD' : money[0],
'AUD' : money[1],
'CAD' : money[2],
'EUR' : money[3],
'HUF' : money[4],
'CHF' : money[5],
'GBP' : money[6],
'JPY' : money[7],
'CZK' : money[8],
'DKK' : money[9],
'NOK' : money[10],
'SEK' : money[11],
'XDR' : money[12]
}
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def calculate_it():
    if request.method == "POST":
        data = request.form
        choice_currency = data.get('currency')
        choice_quantity = data.get("number")
        currency_value = exchange_rate[choice_currency]
        calc = float(currency_value) * float(choice_quantity)
        result = (round (calc, 2))
        return render_template("kalkulator_walut.html", result = result)
    return render_template("kalkulator_walut.html")