#Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений.
#Посчитать их количество.

import re

a = open('pazzl.html','r')
b = re.findall(r'<img.*?>', a.read(), re.M)
print(f'Коды: {b}')
print(f'Количество: {len(b)}')
a.close()
