# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:08:51 2015

@author: ryuhei
"""

import os
import natsort
import google

dir_name = 'data'

# ここから...
file_paths = []
for file_name in os.listdir(dir_name):
    file_path = os.path.join(dir_name, file_name)
    file_paths.append(file_path)

file_paths = natsort.natsorted(file_paths)

text = ""
for path in file_paths:
    with open(path, 'r') as f:
        char = f.read()
        text += char
# ここまではreconstruct_text.pyと同じ

sentence_end = text.find('。')  # 最初の句点の位置
sentence = text[:sentence_end] #　0文字目から最初の句点の一文字前までの文字列を切り出す
query = '"' + sentence + '"'   # ダブルクオーテーションで囲む（Googleで完全一致検索するため）
results = google.search(query) # 検索結果は一般には複数あることに注意

urls = [] # resultsから結果を取り出し、urlsに入れる
for result in results:
    urls.append(result)

print "検索結果:", len(urls), "件"
url = urls[0]
print url