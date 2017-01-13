#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path

rootdir = r"../"

for parent, dirnames, filenames in os.walk(rootdir):
    print("parent is :" + parent)
    for dirname in dirnames:
        print("dirname is :" + dirname)
    for filename in filenames:
        print("filename is :"+ filename)

ls = os.listdir(rootdir)
