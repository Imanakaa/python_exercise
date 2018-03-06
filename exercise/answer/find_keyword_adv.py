# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:25:17 2015

@author: sakurai
"""

import requests
import re

import google_search_adv
import reconstruct_text_adv

if __name__ == '__main__':
    text = reconstruct_text_adv.reconstruct()  # さっき作った関数を再利用する
    url = google_search_adv.search(text)
    print(url)

    # ウェブページのダウンロード
    html = requests.get(url).text

    # 正規表現を使う
    pattern = "ディスプレイに対して(.*)を行い、影"
    match = re.search(pattern, html)
    answer = match.group(1)
    print(answer)
