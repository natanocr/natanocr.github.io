Title: Criando comandos customizados para o django
Date: 2017-09-16 01:00
Modified: 2017-09-16 01:15
Category: Python, Django, crawler
:author: Natan Oliveira - @natanocr
Tags: tutorial, python, Django, crawler
Slug: criando-comandos-customizados-para-o-django
Cover: images/criando-comandos-customizados-para-o-django.png

Recentemente estava desenvolvendo um projeto pessoal que era simples mas acabei batendo cabeça por algumas horas a fio, para em fim encontrar essa solução tão simples. Meu objetivo era integrar um crawler simples de poucas linhas, ao meu site Django, porém sem sucesso. Estava preso em um bug onde o meu crawler não conseguia reconhecer o caminho para o models da app django, desta forma não conseguia salvar as informações raspadas.
	
Enfim minha solução foi criar um comando personalizado para minha app, nesse comando consigo rápido e fácilmente acessar o crawler por meio do manager.py do próprio Django

###TODO
* Criar o diretório **management** dentro da nossa app, com o arquivo **__init__.py** em seu interior.
* Criar o diretório **commands** dentro de  **management**, com o arquivo **__init__.py** em seu interior.
* Criar o arquivo **crawler.py** dentro de **commands**.
* Iniciar nosso crawler com o comando **python manager.py crawler**

####MÃOS A OBRA

Esta será a estrutura do nosso comando customizado::

    app
    └── management
        └── __init__.py
        |
        └── commands
            │   
            └── __init__.py
            └── crawler.py

O básico para que o comando possa ser acessado e funcionar corretamente é este.

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "help of crawler"

    def handle(self, *args, **kwargs):
        self.stdout.write('Crawler iniciado')
	#aqui vai os comandos para iniciar seu crawler

```

O crawler pode ser facilmente acessado pelo comando a seguir.
```
> python manager.py crawler
```

O help para este comando personalisado pode ser acessado deste modo.
```
> python manager.py crawler help
```
Espero que gostem.
