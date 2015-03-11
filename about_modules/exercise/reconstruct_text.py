# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:43:34 2015

@author: ryuhei
"""

import os
import natsort

dir_name = 'data'

file_paths = [] # 空のリストを作成する
for file_name in os.listdir(dir_name):
    # os.path.joinを使ってフォルダ名とファイル名を結合している。 今回の場合は、
    # dir_name + "\\" + filename としても結果は同じだが、この方法を使うことが望ましい。
    # この方法なら、もしdir_nameの末尾にバックスラッシュがあったり、Linuxの場合（"\\"ではなく"/"）でもOK。
    file_path = os.path.join(dir_name, file_name)
    file_paths.append(file_path) # リストにファイルパスを追加する

#file_paths.sort() # この方法では思ったようにソートされない
file_paths = natsort.natsorted(file_paths) # 自然順ソート
print file_paths

# file_pathsのファイル達から順番に中身を読み出し、textに一文字ずつ追加する
text = ""
for path in file_paths:
    f = open(path, 'r')
    char = f.read()
    text += char
    f.close()

print text