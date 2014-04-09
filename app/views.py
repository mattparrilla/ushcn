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


@app.route('/diff-from-mean')
def diff_from_mean():
    f = csv.reader(open('app/data/stj-diff-from-mean.csv', 'rU'))
    years = [l for l in f]
    temperatures = [[0, 2, 3, 4, 5, 6, 7, 8, 9]]

    return render_template('mean-diff.html',
        temperatures=temperatures,
        years=years)
