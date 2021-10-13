import requests
import csv
from flask import Flask, render_template, request

app = Flask(__name__)
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0]['rates']
@app.route("/", methods= ['GET', 'POST']) 
def home():
    if request.method == "POST":
        bid = request.form['bid']
        count = request.form['count']
        return render_template("result.html", result= int(count or 0) * float(bid) )

    return render_template("index.html", rates=rates)

with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in rates:
        spamwriter.writerow([i['currency'], i['code'], i['bid'], i['ask']])
