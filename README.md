# 単一ページpdfをpngに変換するツール

## Description

2通りの状況下で、pdfファイルをpng画像に変換するツールです。
1. 単一ページpdfファイル一つをpng画像に変換する
2. ディレクトリ内の単一ページpdfファイル(複数可)をpng画像に変換する

`.pdf`部分が`.png`になったものがpdfファイルと同じディレクトリに出力されます．

複数ページpdfファイルを指定した場合、1ページ目のみがpng画像として出力されます。

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

2. 変換したいpdfファイルまたはフォルダを指定して`convert_pdf-to-png.py`を実行
   - pdfファイル(単一ページ、単一ファイル)のパスを指定する場合
     - `python3 convert_pdf-to-png.py <FULL filepath>`
     - **フルパス** で指定しないと動作しないため注意 
   - pdfファイル(単一ページ)のあるフォルダを指定する場合(フォルダ内に複数の単一ページpdfファイルがある場合も可)
     - `python3 convert_pdf-to-png.py <FULL directorypath>`
     - **フルパス** で指定しないと動作しないため注意 
    
例：以下のような構成の場合(カレントディレクトリは`/home/user/`を仮定)

```
/home/user/
    ├── convert_pdf-to-png.py
    └── target_dir
        ├── a.pdf
        ├── b.pdf
        └── c.pdf
```
    
### Example1

    pdfファイル(a.pdfのみ)を指定してconvert_pdf-to-png.pyを実行する
    
    ```
    $ python3 ./convert_pdf-to-png.py /home/user/target_dir/a.pdf
    ```

    実行後は以下のようになる．

    ```
    ./
    ├── convert_pdf-to-png.py
    └── target_dir
        ├── a.pdf
        ├── a.png  <- a.pngが生成された
        ├── b.pdf
        └── c.pdf
    ```

### Example2

    ディレクトリ(target_dir)を指定してconvert_pdf-to-png.pyを実行する
    
    ```
    $ python3 ./convert_pdf-to-png.py /home/user/target_dir
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