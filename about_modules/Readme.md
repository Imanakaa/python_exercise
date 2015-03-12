Pythonの初歩2: モジュールの活用
==========================

[TOC]

## モジュール（module）について

モジュールとは、`C++`でいうところのライブラリとだいたい同じ概念です。効率的な開発には、本体に標準で付属するモジュール群や、サードパーティー製のモジュールの活用が不可欠です。
今回の勉強会ではPythonの環境構築にAnacondaを用いたので、Python本体（+標準モジュール群）だけでなく、よく使われるサードパーティー製モジュール群も一緒にインストールされており、すぐ使える状態が整っています。

* 標準ライブラリ
    * [標準ライブラリレファレンス](http://docs.python.jp/2.7/library/index.html)
        * Pythonをインストールすると本体に標準で付属される、最初から利用可能なモジュール（`C++`でいうところの`<iostream>`など）の一覧です。
    * [標準ライブラリミニツアー1](http://docs.python.jp/2/tutorial/stdlib.html), [ミニツアー2](http://docs.python.jp/2/tutorial/stdlib2.html)
        * 膨大な標準モジュール群のうち、基本的なものが紹介されています。[公式チュートリアル](http://docs.python.jp/2/tutorial/index.html)の一項目です。
* サードパーティー製とそのインストール方法
    * （`C++`でいうところの`OpenCV`など）

## 標準モジュール

* os, os.path
* re
正規表現のモジュールです。

* urllib2
インターネットからURLをもとにデータを取得するためのモジュールです。
ファイルを読み書きするための`open関数`に似た作りになっていて、openした後にreadして読み込むところは同じです。下記の例では、yahoo.co.jpのトップページをダウンロードして表示しています。

```python
import urllib2
f = urllib2.urlopen('http://www.yahoo.co.jp')
html = f.read()
print html
```

* smtplib
メールサーバを介してメールを送信するためのモジュールです。
なお、これを実行するためには、McAfeeの **アクセス保護を無効にする** 必要があります。また、このサンプルは研究室LAN内からしか実行できません。しかし、SMTPサーバとしてgmailなどを使えば、どこからでも送信可能にできます（その場合、若干の拡張が必要になります）。

```python
import smtplib
# 研究室のメールサーバに接続
server = smtplib.SMTP('aissrv.ais.ics.ritsumei.ac.jp')
# 送信者アドレス、宛先アドレス、本文を指定する
server.sendmail('sakurai@ais.ics.ritsumei.ac.jp',
				'rsakurai@fc.ritsumei.ac.jp',
				'This is a test mail')
```

* SimpleHTTPServer
カレントディレクトリを簡易HTTPサーバにしてしまうモジュールです。

```python
import SimpleHTTPServer
SimpleHTTPServer.test()
```

上記スクリプトを実行した後、ブラウザから http://localhost:8000/ を開くと、カレントディレクトリのファイル一覧が表示されます。ファイルのリンクをクリックするとファイルが表示され、ダウンロードすることもできます。普通にインターネットに公開されているため、 http://133.19.61.144:8000/ にアクセスすると、創成用14番機のファイルがダウンロードできます。 **危険なので使用には注意が必要です。**

## サードパーティ製モジュール
開発内容に応じて必要なモジュールをインストールすることになると思います。

### インストール方法
サードパーティ製モジュールは様々な方式で配布されており、インストール方法にも色々あるため、正直言ってややこしいです。PythonのインストールにAnacondaを使った場合は、以下の3つの方法で外部のモジュールをインストールすることになります。

1. `conda install module_name` を使う方法
2. `pip install module_name` を使う方法
3. ソースコードをダウンロードし、`python setup.py install` とする方法

これらは、番号が若いほうの方法ほど推奨されます。そのため、インストールしたいモジュールを見つけた場合は、上から順番に試してください。

1の`conda`は、Anacondaのパッケージ管理機能を使う方法です。可能ならこの方法を使うことが理想的です。

* 利点: パッケージ間の依存関係やバージョンに関わる整合性が、Anacondaの開発スタッフによって検証されているので、不具合が起きにくい。また、アンインストールが簡単。
* 欠点: Anacondaで管理可能なモジュールはメジャーなものだけなので、マイナーなモジュールはこの方法でインストールできないことが多い。

具体的には、[condaの対応モジュール一覧](http://docs.continuum.io/anaconda/pkg-docs.html) にあるものはconda経由でインストールできます（モジュール名の右肩にLinuxとか付いているものは除く）。

2の`pip`は現状最も一般的なインストール方法です。condaが無理だった場合にこの方法を使います。

* 利点: 多くのモジュールがpipでインストールできる。また、アンインストールが簡単。
* 欠点: Anacondaほど整合性のチェックが徹底的ではない。

pipは[PyPi](https://pypi.python.org/pypi)というモジュール共有システムを介してインストールする方法です。pipも同様にパッケージ管理機能を有しており、依存関係の解決は行われます。しかし、検証はモジュール作者に委ねられているため、不具合はありえます。

3の`setup.py`は、パッケージ管理を介さず、ソースコードから直接インストールする方式です。この方法でインストールした場合は、 **自動アンインストールできません** 。

* 利点: インストール方法が提供されていること自体が利点。
* 欠点: パッケージ管理機能の対象とならない。また、アンインストールは手動で行う必要がある。

これは、モジュールの作者が提供する直接的なインストール方法です。GitHubなどにおいてソースコードの状態で配布してくれている場合に、このインストール方法が提供されていることがあります。

### [natsort](https://pypi.python.org/pypi/natsort)
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

### [google](https://pypi.python.org/pypi/google)

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
