#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:29:44 2018

@author: jayhan
"""
import bs4

#html_doc = """
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title"><b>The Dormouse's story</b></p>
#
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#
#<p class="story">...</p>
#"""

html_doc = open("html_structure_select.html").read()
soup = bs4.BeautifulSoup(html_doc,"lxml")
print(soup.prettify())

a_tags = soup.select("a")
print()
print("a_tags:\n",a_tags)

a_tag = soup.select("a[id=link1]")
print()
print("a_tag with id=link1:\n",a_tag)
    
