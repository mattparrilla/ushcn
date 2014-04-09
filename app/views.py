from index import app
from flask import render_template
import csv


@app.route('/')
def index():
    f = csv.reader(open('app/data/stj-mean-temp-by-year.csv', 'rU'))
    years = [l for l in f]
    temperatures = [[10, 20, 30, 40, 50, 60, 70, 80, 90]]

    return render_template('mean-temp.html',
        temperatures=temperatures,
        years=years)
