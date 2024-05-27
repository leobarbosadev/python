import locale
import os
import datetime


os.system('cls')

data = datetime.datetime.now()

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
mes = data.strftime('%A')
print(mes)
print('Sábado')