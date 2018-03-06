# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:08:51 2015

@author: ryuhei
"""

import urllib
import requests
from bs4 import BeautifulSoup

import reconstruct_text_adv  # モジュールとして読み込む


def search(text):
    sentence_end = text.find('。')   # 最初の句点の位置
    sentence = text[:sentence_end]  # 0文字目から最初の句点の一文字前までの文字列を切り出す
    query = '"' + sentence + '"'    # ダブルクォートで囲む（Googleで完全一致検索するため）

    # クエリ文字列をGoogle検索し，検索結果画面から該当サイトのURLを抽出する
    res = requests.get('http://google.com/search?q=' + query)
    soup = BeautifulSoup(res.text, 'lxml')
    link_elems = soup.select('.r a')
    url = link_elems[0]['href']
    params = urllib.parse.urlparse(url).query
    url = urllib.parse.parse_qs(params)['q'][0]
    return url


if __name__ == '__main__':
    text = reconstruct_text_adv.reconstruct()  # さっき作った関数を再利用する
    url = search(text)
    print(url)
