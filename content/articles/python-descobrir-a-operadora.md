Title: Python descobrir a operadora
Date: 2017-05-22 21:00
Modified: 2017-05-22 21:00
Category: Python
Tags: tutorial, python, operadora
Slug: python-descobrir-a-operadora
Cover: images/python-descobrir-a-operadora.png

Esta é uma forma simples e rápida para descobrir qual a operadora de um determinado número. Necessitamos apenas da requisição de uma url com [Requests](http://docs.python-requests.org) e posteriormente da análise do código html retornado com a ajuda do  [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).

###TODO
* Requisitar com um post a url que fornece a informação que procuramos.
* Nessa requisição passamos como parametro o numero de celular e o paramentro **verify=False**, este úiltimo serve para contornar erros do ssl do servidor casa haja.
* Passamos os dados retornados para o **BeautifulSoup** para que este nos auxilie a a parsear o html.
* Na análise do html vamos procurar pelo tag exata que retorna a operadora e retornamos a informação encntrada.

####MÃOS A OBRA
```python
import requests
from bs4 import BeautifulSoup

def get_operadora(fone):
    req = requests.post('https://www.qual-operadora.net/#fb-root',
                        data={'numero':fone}, verify=False)
    soup = BeautifulSoup(req.text, 'html.parser')
    list = soup.findAll("span", { "class" : "verde" })
    return (list[1].text.strip(':'))
```

Espero que gostem.

