# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:43:34 2015

@author: ryuhei
"""

import os
import glob
import natsort

def reconstruct():
    dir_name = 'data'

    file_paths = glob.glob(os.path.join(dir_name, "*.txt")) # globを使う
    file_paths = natsort.natsorted(file_paths)

    text = ""
    for path in file_paths:
        # with構文を使って自動的にcloseされるようにする（openを使うときは普通こうする）
        with open(path, 'r') as f:
            text += f.read()
    return text

if __name__ == '__main__':
    text = reconstruct()
    print(text)
