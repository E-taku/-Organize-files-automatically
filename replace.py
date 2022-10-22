import os
import shutil
import re

# コピー先のディレクトリを作成
if not (os.path.isdir('./../copy_ABC')):
    os.mkdir('./../copy_ABC')

# ディレクトリの取得
path='.'
dir_list = os.listdir(path)
files_dir = [f for f in dir_list if os.path.isdir(os.path.join(path, f))]


# 各ディレクトリ内のファイルを取得
for dir in files_dir:
    path = './' + dir
    files = os.listdir(path)

    files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]

    for file_name in files_file:
        pattern = '(.+?)\.(\w+)'
        # 正規表現で拡張子前のfile名部分を取得
        result = re.findall(pattern, file_name)

        filepath = f'./../copy_ABC/{result[0][0]}/{file_name}'
        dirpath = f'./../copy_ABC/{result[0][0]}'

        # ディレクトリの作成
        if not (os.path.isfile(dirpath)):
            try:
                os.mkdir(dirpath)
            except FileExistsError:
                pass

        # fileのコピー（移動）
        new_file = result[0][0] + '_' + dir + '.' + result[0][1]
        new_file = f'{dirpath}/{new_file}'
        copy_file = f'./{dir}/{file_name}'

        try:
            shutil.copy2(copy_file, new_file)
        except FileNotFoundError as e:
            print("No such file or directory: '{}'".format(copy_file))
