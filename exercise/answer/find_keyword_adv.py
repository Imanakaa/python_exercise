# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:25:17 2015

@author: sakurai
"""

import google_search_adv
import urllib2
import re

if __name__ == '__main__':
    url = google_search_adv.search()
    # ウェブページのダウンロード
    f = urllib2.urlopen(url)
    html = f.read()
    
    # 正規表現を使う
    pattern = "ディスプレイに対して(.*)を行い、影"
    match = re.search(pattern, html)
    answer = match.group(1)
    print answer