#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Natan Oliveira'
SITEURL = 'http://localhost:8000'
SITENAME = 'NatanOCR - Natan Oliveira Blog'
SITETITLE = AUTHOR
SITESUBTITLE = 'Analista de Sistemas'
SITELOGO = '//s.gravatar.com/avatar/8aaa554ca377fbcdb5f22bf0260821df?s=80'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'
ROBOTS = 'index, follow'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Blogroll
LINKS = (())

# Social widget
SOCIAL = (('linkedin', 'https://br.linkedin.com/in/natanocr/en'),
          ('github', 'https://github.com/natanocr'),
          ('twitter', 'https://twitter.com/natanocr'),
          ('rss', '//blog.alexandrevicenzi.com/feeds/all.atom.xml'))


MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DISQUS_SITENAME = "natanocr"
ADD_THIS_ID = 'ra-58ec12b388fb9915'
GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-8638263036572863',
    'page_level_ads': True,
    'ads': {
        'aside': '5340595560',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '9584371569',
        'article_top': '',
        'article_bottom': '7257980762',
    }
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = u'themes/Flex'