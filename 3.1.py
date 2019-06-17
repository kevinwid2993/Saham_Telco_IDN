import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

xl = pd.read_csv('dataSaham/EXCL.JK.csv', parse_dates = ['Date'])
smart = pd.read_csv('dataSaham/FREN.JK.csv', parse_dates = ['Date'])
indosat = pd.read_csv('dataSaham/ISAT.JK.csv', parse_dates = ['Date'])
telkom = pd.read_csv('dataSaham/TLKM.JK.csv', parse_dates = ['Date'])

plt.figure('Harga Historis Saham Provider Telco Indonesia', figsize=(10,5))

plt.plot(xl['Date'],xl['Close'], color = 'green')
plt.plot(smart['Date'],smart['Close'], color = 'cyan')
plt.plot(indosat['Date'],indosat['Close'], color = 'blue')
plt.plot(telkom['Date'],telkom['Close'], color= 'red')

plt.title('Harga Historis Saham Telco Indonesia')

plt.xlabel('Tanggal')
plt.ylabel('Rupiah(IDR)')

plt.yticks(rotation=45)
plt.xticks(rotation=45)
plt.legend(['PT XL AXIATA','PT SMARTFREN TELECOM','PT INDOSAT','PT TELEKOMUNIKASI INDONESIA'], loc = 1)

plt.show()