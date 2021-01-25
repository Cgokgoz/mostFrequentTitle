import json
import csv
import re
from collections import Counter
import matplotlib.pyplot as plt

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def readData2(dataJson, dataCsv):
    with open(dataJson) as f:
        data = json.load(f)
    with open('log.txt', 'w') as log:
        for value in data.values():
            log.write('{}\n'.format(value))
        with open(dataCsv, 'rt') as file:
            data2 = csv.reader(file, delimiter=',')
            for row in data2:
                log.write('{}\n'.format(row[1]))


def take_json_adress():
    datajson = (input("please enter json data address: "))
    return datajson


def take_csv_adress():
    data_csv = (input("please enter csv data address : "))
    return data_csv


def openfile():
    f = open('log.txt', 'r')
    linelist = f.readlines()

    # Re-open file here
    f2 = open('log.txt', 'w')
    for line in linelist:
        f2.write('{}\n'.format(normalize(line)))
    f2.close()


def normalize(name):
    name = name.lower()
    name = re.sub(r"[.,/#!$%^*;:{}=_`~()@]", ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def take_input():
    # n = int(input('please enter a number between 1 to 10 :'))
    while True:
        try:
            n = int(input('please enter a number between 1 to 10 :'))
            while not( 1>= n >= 10):
                print("Oops!  That was no valid number.  Try again...")
                n = int(input('please enter a number between 1 to 10 :'))
                break
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    return n


def frequent_data(n):
    with open('log.txt') as f:
        cnts = Counter(l.strip() for l in f)

    x = cnts.most_common(int(n))
    print("top-" + str(n) + " most frequent titles:")
    print(x)
    return x


def display_barchart(x):
    y_line = []
    x_line = []
    for t in x:
        y_line.append(t[0])
        x_line.append(t[1])

    y_pos = np.arange((len(y_line)))
    plt.bar(y_pos, x_line, align='edge', alpha=0.5)
    plt.xticks(y_pos, y_line)
    plt.ylabel('Count')
    plt.title('Most Frequent Title')
    plt.show()


if __name__ == '__main__':
    readData2(take_json_adress(), take_csv_adress())
    openfile()
    display_barchart(frequent_data(take_input()))

