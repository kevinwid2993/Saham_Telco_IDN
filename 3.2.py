import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xl = pd.read_csv('dataSaham/EXCL.JK.csv', parse_dates = ['Date'])
smart = pd.read_csv('dataSaham/FREN.JK.csv', parse_dates = ['Date'])
indosat = pd.read_csv('dataSaham/ISAT.JK.csv', parse_dates = ['Date'])
telkom = pd.read_csv('dataSaham/TLKM.JK.csv', parse_dates = ['Date'])


plt.figure('Harga Historis Saham Provider Telco Indonesia (April 2019)', figsize = (8,5))
plt.plot(xl.set_index('Date')['2019-04'].index, xl.set_index('Date')['2019-04']['Close'], color = 'green')
plt.plot(smart.set_index('Date')['2019-04'].index, smart.set_index('Date')['2019-04']['Close'], color = 'cyan')
plt.plot(indosat.set_index('Date')['2019-04'].index, indosat.set_index('Date')['2019-04']['Close'], color = 'blue')
plt.plot(telkom.set_index('Date')['2019-04'].index, telkom.set_index('Date')['2019-04']['Close'], color = 'red')

plt.suptitle('Harga Historis Saham Provider Telco Indonesia (April 2019)')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation = 45)

plt.legend(['PT XL AXIATA','PT SMARTFREN TELECOM','PT INDOSAT','PT TELEKOMUNIKASI INDONESIA'], loc = 1)

plt.show()