# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:25:17 2015

@author: sakurai
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
# ここまではgoogle_search.pyと同じ

# ウェブページのダウンロード
f = urllib.request.urlopen(url)
html = f.read()
f.close()
html = html.decode('utf-8')

# ディスプレイに対して●●●を行い、影
pre_str = "ディスプレイに対して"
suf_str = "を行い、影"
begin = html.find(pre_str) + len(pre_str)  # 最初の●の位置
end = html.find(suf_str)  # "を行い、影"の"を"の位置
answer = html[begin:end]
print(answer)
