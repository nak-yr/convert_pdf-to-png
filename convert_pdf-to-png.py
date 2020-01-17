# カレントディレクトリ内のpdf -> pngに一括変換
# 使用方法： 変換したいpdfのあるディレクトリにて「python3 <pdf2png.pyの相対パス>」を実行

from pdf2image import convert_from_path
import sys
import os

# カレントディレクトリのフルパスを取得
path_to_dir = os.getcwd()

# 拡張子がpdfのファイル名を格納するリスト
targets = []
# カレントディレクトリ内で拡張子がpdfのものだけをtargetsに抽出
for fileName in os.listdir(path_to_dir):
    if ".pdf" in fileName:
        # appendは，リストの末尾に要素を追加する
        targets.append(fileName)

# 変換予定のpdfファイルのフルパス格納用リスト
path_to_targets = []
# 変換後のpngファイルのフルパス指定用リスト
converted_pdfs_path = []

# 変換するpdfファイルのフルパスのリストpath_to_targetsを作成
for i in range(len(targets)):
    temp_path = path_to_dir + '/' + targets[i]
    path_to_targets.append(temp_path)
    converted_pdfs_path.append(temp_path.replace('.pdf', '.png'))

# path_to_targetsリストに記されたpdfファイルをpngに変換
for i in range(len(targets)):
    images = convert_from_path(path_to_targets[i])
    images[0].save(converted_pdfs_path[i], 'png')
