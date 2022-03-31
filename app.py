from flask import Flask, render_template, request
import requests
import csv

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/C?format=json')
data = response.json()

rates = data[0]["rates"]

exchange_rate = {}

for rate in rates:
    exchange_rate[rate["code"]] = rate["ask"]

def export_to_csv():
    with open('Waluty.csv', mode='w', encoding='utf-8') as csv_file:
        fieldnames = ['currency', 'code', 'bid', 'ask']
        csvwriter = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csvwriter.writeheader()
        for n in rates:
            csvwriter.writerow(n)

export_to_csv()

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