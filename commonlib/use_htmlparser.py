#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser


# htmlparser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_engtag(self, tag):
        print('<%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityef(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
        <head></head>
        <body>
        <!-- test html parser -->
            <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
            </body></html>''')
