# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:23:01 2015

@author: ryuhei
"""

import sys
import os

dir_name = 'data'
if os.path.exists('data'):
    sys.exit(0)
os.mkdir(dir_name)

# Web上に1件しか存在しないテキストを入れる
text = '本研究では、物理的に立体形状を表現し、動的な形状表現によって立体のアニメーションも表現可能なディスプレイについて研究を行います。 立体ディスプレイの実現には、動的に立体形状を表現する機構を持つハードウェアを作成し、表現された形状に対しプロジェクタを用いてテクスチャをマッピングする必要があります。さらに、操作時に影のできない立体ディスプレイを実現しました。 これまでの立体ディスプレイに関する研究では、ディスプレイ上方に設置されたプロジェクタからディスプレイ表面に投影を行っていました。 しかし、この方法で投影した場合、直接インタラクションを行う際に手などが遮蔽物となりディスプレイ表面に影ができてしまいます。 そこで、本研究ではディスプレイに対してリアプロジェクションを行い、影のできない立体ディスプレイを実現しました。'

chars = [char.encode('utf8') for char in text.decode('utf8')]
for i, c in enumerate(chars):
    file_name = '%d.txt' % i
    file_path = os.path.join(dir_name, file_name)
    with open(file_path, 'w') as f:
        f.write(c)

text2 = "".join(chars)
print text2
print text == text2