# 解答例で用いたモジュール

## [natsort](https://pypi.python.org/pypi/natsort)
自然順ソート（natural sort, natsort）を行うためのモジュールです。
Anacondaのデフォルトには入ってませんが、condaで提供されており、

```bash
conda install natsort
```

とすればインストールできます。PyPiの[description](https://pypi.python.org/pypi/natsort)に使用例が載っています。具体的には以下のように使います:

```python
import natsort
a = ['a2', 'a9', 'a1', 'a4', 'a10']
print(natsort.natsorted(a))
# ['a1', 'a10', 'a2', 'a4', 'a9']
```

## [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Google検索を行うために使ったモジュールです。
これ自体は汎用のウェブスクレイピング用のツールです．
ウェブスクレイピングとは，ウェブ上のコンテンツ中の特定の箇所などをソフトウェアによって機械的に取得することをいいます．

Anacondaではデフォルトで同梱されているため，改めてインストールする必要はありません。

```bash
conda install beautifulsoup4
```

とすればインストールできます。具体的な利用方法は[公式サイトのドキュメント](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)を見てください．