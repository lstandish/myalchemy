#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lloyd Standish'
SITENAME = "Lloyd's Blog"
SITEURL = ''
OUTPUT_PATH = 'output/'
PATH = 'content'

AUTHOR_SAVE_AS = ''
#The location to save the tag page
TAG_SAVE_AS = 'tag/{slug}.html'
#The URL to use for a tag.
TAG_URL = 'tag/{slug}.html'
#The URL to use for a category.
CATEGORY_URL = 'category/{slug}.html'
#The location to save a category.
CATEGORY_SAVE_AS = 'category/{slug}.html'


TIMEZONE = 'America/Costa_Rica'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#ARTICLE_URL = 'posts/{slug}.html'
#ARTICLE_SAVE_AS = ARTICLE_URL
#ARTICLE_LANG_URL = 'posts/{slug}-{lang}.html'
#ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

# temporary for development
LOAD_CONTENT_CACHE = False

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = []
#A list of filenames that should be retained and not deleted from the output directory.
# One use case would be the preservation of version control data.

# EXPLICIT FOR REFERENCE, THESE ARE DEFAULTS
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
# to hide pages add "status: hidden" metadata

# linking to non-article or non-page content (called "Static" content)
# need to declare directories containing such files in following setting
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = [ 'admin', 'images', 'pdfs' ]
# folder "images" is included by default

# if there is a need to mix static files and source files  in the same directory,
# such directory must be added to both PAGE_PATHS/ARTICLE_PATHS and STATIC_PATHS

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

# Theme settings --------------------------------------------------------------

THEME = 'themes/alchemy'
SITESUBTITLE = "Lloyd's Blog"
#SITEIMAGE = '/images/profile.jpg width=200 height=200'
DESCRIPTION = 'A functional, clean, responsive theme for Pelican. powered by' \
              'Bootstrap.'
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

ICONS = [
    ('github', 'https://github.com/nairobilug/pelican-alchemy'),
]

PYGMENTS_STYLE = 'monokai'
RFG_FAVICONS = True

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
