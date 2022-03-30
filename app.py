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

export_to_csv()

money = []

for i in dates:
    money.append (i['ask'])

USD = money[0]
AUD = money[1]
CAD = money[2]
EUR = money[3]
HUF = money[4]
CHF = money[5]
GBP = money[6]
JPY = money[7]
CZK = money[8]
DKK = money[9]
NOK = money[10]
SEK = money[11]
XDR = money[12]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def calculate_it():
    if request.method == "POST":
        data = request.form
        choice_currency = data.get('currency')
        choice_quantity = data.get("number")
        if choice_currency == "USD":
            choice_currency = USD
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "AUD":
            choice_currency = AUD
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "CAD":
            choice_currency = CAD
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "EUR":
            choice_currency = EUR
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "HUF":
            choice_currency = HUF
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "CHF":
            choice_currency = CHF
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "GBP":
            choice_currency = GBP
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "JPY":
            choice_currency = JPY
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "CZK":
            choice_currency = CZK
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "DKK":
            choice_currency = DKK  
            result = float(choice_currency) * float(choice_quantity)
            result = (round (result, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "NOK":
            choice_currency = NOK
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "SEK":
            choice_currency = SEK
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)
        elif choice_currency == "XDR":
            choice_currency = XDR
            calc = float(choice_currency) * float(choice_quantity)
            result = (round (calc, 2))
            return render_template("kalkulator_walut.html", result = result)

    return render_template("kalkulator_walut.html")