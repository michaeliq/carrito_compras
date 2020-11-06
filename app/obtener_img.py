from bs4 import BeautifulSoup
import requests
import re

def remplazarLetra(oracion):
    operacion = re.finditer(r"\s",oracion)
    operacion = [x.start() for x in operacion]
    oracion_n = oracion.replace(" ","+",len(operacion))
    return oracion_n

def fijar_img(referencia):
    elem_a_buscar = remplazarLetra(referencia)

    url = f'https://www.google.com/search?q={elem_a_buscar}&client=firefox-b-d&bih=650&biw=1366&hl=es&sxsrf=ALeKk01uUbfogCIOZ4MliNCe9KeV1kPXDA:1604610381808&tbm=isch&source=iu&ictx=1&fir=wYLEvc_TXFOXvM%252CeTsS9e7PFZCRkM%252C_&vet=1&usg=AI4_-kTBPne8P8sjYokQ36nnlBqwN8Rj-A&sa=X&ved=2ahUKEwioy72-p-zsAhVKlFkKHUFNCd8Q_h16BAgZEAk'

    req = requests.get(url)

    soup = BeautifulSoup(req.text,'html.parser')

    img_obj = soup.find_all('img')[1]['src']

    return img_obj







