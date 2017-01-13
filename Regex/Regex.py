#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re as regex

re_ob = regex.compile("sd")

text = "asdasd qwdasd wsdassdd asdsdajfkopzdmfrun"

for url, name in re_ob.findall(text):
    print ('%s (%s)' % (name , url))

m = regex.match('fuoo', 'afuood')
if m is not None:
    print("regex match")
    print(m.group())

s = regex.search('fuoo', 'afuood')
if s is not None:
    print("regex search")
    print(s.group())