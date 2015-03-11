# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:43:34 2015

@author: ryuhei
"""

import os
import natsort

dir_name = 'data'

file_paths = []
for file_name in os.listdir(dir_name):
    file_path = os.path.join(dir_name, file_name)
    file_paths.append(file_path)

#file_paths.sort()
file_paths = natsort.natsorted(file_paths)
#print file_paths

text = ""
for path in file_paths:
    with open(path, 'r') as f:
        char = f.read()
        text += char
print text