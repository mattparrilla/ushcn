#!/usr/local/bin/python
import csv


def date_to_year():
    """Takes a CSV from USHCN and converts it from 1 row/day to 1 row/year """
    f = csv.reader(open('app/data/stjohnsbury-mean-temp.csv', 'rU'))
    dates = [l for l in f]
    del dates[0:2]

    date_row = [''] * 367
    all_dates = []
    year_list = []

    # this block allows me to create tick marks for the first of the month
    header_row = ['year']
    for date in dates[:365]:
        if date[0] == '1':
            header_row.append(date[0])
        else:
            header_row.append(0)
    header_row[-1] = '1'
    all_dates.append(header_row)

    # below the original data is converted from 1 row/day to 1 row/year
    for date in dates:
        date_idx = int(date[1])
        if date[4] not in year_list:
            year_list.append(date[4])
            all_dates.append(date_row)
            date_row = [''] * 367
            # Add the year to the first column if year ends in zero
            if date[4][-1] == '0':
                date_row[0] = date[4]
        try:
            date_row[date_idx] = int(date[5])
        except ValueError:
            pass

    del all_dates[1]  # empty row created when I append date_row to all_dates

    writer = csv.writer(open('app/data/stj-mean-temp-by-year.csv', 'w'))
    writer.writerows(all_dates)


def mean_on_date():
    """Takes USHCN data and calculates the mean temperature for each date"""

    f = csv.reader(open('app/data/stjohnsbury-mean-temp.csv', 'rU'))
    dates = [l for l in f]
    del dates[0:2]

    temps = [[]] * 366

    for date in dates:
        date_idx = int(date[1]) - 1
        if date_idx == 0:
            try:
                temps[date_idx].append(int(date[5]))
            except ValueError:
                pass
    print temps[5]

mean_on_date()
