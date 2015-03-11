# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:43:34 2015

@author: ryuhei
"""

import os
import natsort

def reconstruct():
    dir_name = 'data'

    # リスト内包記法を使う
    file_paths = [os.path.join(dir_name, name) for name in os.listdir(dir_name)]
    file_paths = natsort.natsorted(file_paths)

    text = ""
    for path in file_paths:
        # with構文を使って自動的にcloseされるようにする（openを使うときは普通こうする）
        with open(path, 'r') as f:
            text += f.read()
    return text

if __name__ == '__main__':
    text = reconstruct()
    print text