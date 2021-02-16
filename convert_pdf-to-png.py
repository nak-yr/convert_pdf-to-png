"""
指定したディレクトリ内のpdf or 指定した単一ページPDFファイル一つをpngに一括変換
usage：
    $ python3 convert_pdf-to-png.py <FULL filepath>
    $ python3 convert_pdf-to-png.py <FULL directorypath>
"""

from pdf2image import convert_from_path
import sys
import os

# コマンドライン引数で指定されたパス
path = sys.argv[1]

# 変換予定のpdfファイルのフルパス格納用リスト
pdfs_path = []
# 変換後のpngファイルのフルパス指定用リスト
pngs_path = []

# コマンドライン引数がフォルダパスかファイルパスかを判定し、処理を分岐する
if os.path.isdir(path):
    # フォルダパスだった場合、フォルダ内全てのPDFファイルを変換対象とする
    # カレントディレクトリ内で拡張子がpdfのものだけをpdfs_pathに抽出
    for fileName in os.listdir(path):
        if ".pdf" in fileName:
            # 拡張子が.pdfのすべてのファイルのフルパスを生成して格納
            temp_path = path + '/' + fileName
            pdfs_path.append(temp_path)
        if len(pdfs_path)==0:
            print("ERROR : There is no PDF file!")
            sys.exit(1)
elif os.path.isfile(path):
    # ファイルパスだった場合、指定されたPDFファイルを変換対象とする
    # 一つでも拡張子が「.pdf」でないファイル名を指定すると、異常終了する
    if not (".pdf" in path):
        print("ERROR: You may have a wrong filename!")
        sys.exit(1)
    pdfs_path.append(path)
else:
    # ファイルでもディレクトリでもない場合、存在しない旨を表示し異常終了する
    print("ERROR : Please input correct file or directory name.")
    sys.exit(1)

# 変換するpdfファイルのフルパスのリストpdfs_pathを作成
for i in range(len(pdfs_path)):
    pngs_path.append(pdfs_path[i].replace('.pdf', '.png'))

# pdfs_pathリストに記されたpdfファイルをpngに変換
for i in range(len(pdfs_path)):
    images = convert_from_path(pdfs_path[i])
    images[0].save(pngs_path[i], 'png')