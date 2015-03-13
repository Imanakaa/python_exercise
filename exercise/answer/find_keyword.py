# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:25:17 2015

@author: sakurai
"""

import os
import natsort
import google
import urllib2

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
# ここまではgoogle_search.pyと同じ

# ウェブページのダウンロード
f = urllib2.urlopen(url)
html = f.read()
f.close()

# ディスプレイに対して●●●を行い、影
pre_str = "ディスプレイに対して"
suf_str = "を行い、影"
begin = html.find(pre_str) + len(pre_str) # 最初の●の位置
end   = html.find(suf_str) # "を行い、影"の"を"の位置
answer = html[begin:end]
print answer