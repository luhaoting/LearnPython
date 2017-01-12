from urllib.request import urlopen
import re

p = re.compile('((\w+)\s+\w+)')

text = urlopen('http://www.mop.com/').read()

text = text.decode("utf-8")

print(p.findall(text))
'''
for url, name in p.findall(text):
    print ('%s (%s)' % (name , url))
'''