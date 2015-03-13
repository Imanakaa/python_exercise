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
print natsort.sorted(a)
# ['a1', 'a10', 'a2', 'a4', 'a9']
```

## [google](https://pypi.python.org/pypi/google)

Google検索を行うためのモジュールです。
これはcondaでは配布されていないため、pipでインストールします。

```bash
pip install google
```

とすればインストールできます。PyPiのdescriptionに[使用方法へのリンク](https://breakingcode.wordpress.com/2010/06/29/google-search-python/)があり、具体的には以下のように使います:

```python
# Get the first 20 hits for "Mariposa botnet" in Google Spain
from google import search
for url in search('Mariposa botnet', tld='es', lang='es', stop=20):
    print(url)
```
