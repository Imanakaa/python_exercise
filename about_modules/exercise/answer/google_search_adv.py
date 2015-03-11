# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:08:51 2015

@author: ryuhei
"""

import google
import reconstruct_text_adv # モジュールとして読み込む

text = reconstruct_text_adv.reconstruct() # さっき作った関数を再利用する
sentence_end = text.find('。')
sentence = text[:sentence_end]
query = '"' + sentence + '"'
results = google.search(query)

url = results.next() # イテレータから1個読み出す
print url