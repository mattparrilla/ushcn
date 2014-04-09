#!/usr/local/bin/python
import csv


def date_to_year():
    """Takes a CSV """
    f = csv.reader(open('app/data/stjohnsbury-mean-temp.csv', 'rU'))
    dates = [l for l in f]
    del dates[0:2]

    date_row = []
    all_dates = []

    header_row = ['year']
    for date in dates[:365]:
        if date[0] == '1':
            header_row.append(date[0])
        else:
            header_row.append(0)
    header_row[-1] = '1'
    all_dates.append(header_row)

    for date in dates:
        if date[0] == '29' and date[2] == '2':
            continue
        if date[0] == '1' and date[2] == '1':
            all_dates.append(date_row)
            if date[4][-1] == '0':
                date_row = [date[4]]
            else:
                date_row = ['']
        try:
            date_row.append(int(date[5]))
        except ValueError:
            date_row.append(date_row[-1])

    # Gets rid of incomplete years
    list_to_write = []
    for year in all_dates:
        if len(year) < 365:
            continue
        else:
            list_to_write.append(year)

    writer = csv.writer(open('app/data/stjohnsbury-mean-temp-by-year.csv', 'w'))
    writer.writerows(list_to_write)


date_to_year()
