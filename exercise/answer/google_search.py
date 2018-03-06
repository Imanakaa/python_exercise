# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:08:51 2015

@author: ryuhei
"""

import os
import urllib
import natsort
import requests
from bs4 import BeautifulSoup

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

sentence_end = text.find('。')   # 最初の句点の位置
sentence = text[:sentence_end]  # 0文字目から最初の句点の一文字前までの文字列を切り出す
query = '"' + sentence + '"'    # ダブルクオーテーションで囲む（Googleで完全一致検索するため）

# クエリ文字列をGoogle検索し，検索結果画面から該当サイトのURLを抽出する
res = requests.get('http://google.com/search?q=' + query)
soup = BeautifulSoup(res.text, 'lxml')
link_elems = soup.select('.r a')
url = link_elems[0]['href']
params = urllib.parse.urlparse(url).query
url = urllib.parse.parse_qs(params)['q'][0]

print(url)
