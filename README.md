# 単一ページpdfをpngに変換するツール

## Description

カレントディレクトリ内の単一ページpdfをpngに一括変換するpythonスクリプトです．

`.pdf`部分が`.png`になったものがカレントディレクトリに出力されます．

## Requirements

- python3.x
- package
  - pdf2image

## Usage

- `pdf2image`のインストール
    ```
    $ pip3 install pdf2image
    ```
1. `convert_pdf-to-png.py`を好きな場所に保存

2. 変換したいpdfファイルのあるディレクトリに移動

3. 移動したディレクトリ内で以下を実行
    ```
    $ python3 path/to/convert_pdf-to-png.py
    ```
    
    例：以下のような構成の場合
    
    ```
    ./
    ├── convert_pdf-to-png.py
    └── target_dir
        ├── a.pdf
        ├── b.pdf
        └── c.pdf
    ```
    
    この場合，`target_dir`に移動して，その中からconvert_pdf-to-png.pyを実行する．
    
    ```
    $ cd target_dir
    $ python3 ../convert_pdf-to-png.py
    ```

    実行後は以下のようになる．

    ```
    ./
    ├── convert_pdf-to-png.py
    └── target_dir
        ├── a.pdf
        ├── a.png
        ├── b.pdf
        ├── b.png
        ├── c.pdf
        └── c.png
    ```

## Notes

- 複数ページのpdfは最初の1ページ目しか出力されません
  - 出来れば改善します...

## Biblio

- Python, enumerateの使い方: リストの要素とインデックスを取得 - note.nkmk.me

    https://note.nkmk.me/python-enumerate-start/

- Pythonで文字列を比較（完全一致、部分一致、大小関係など）- note.nkmk.me

    https://note.nkmk.me/python-str-compare/

- python pdf2imageでPDF→png - @ume1126 Qiita

    https://qiita.com/ume1126/items/5d9ae08689de737176d2

## LICENSE

**MIT LICENSE**