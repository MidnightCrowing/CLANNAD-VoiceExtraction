import glob
import os
import re
import shutil
import sys


class From:
    Count = "count"
    Text = "text"


def read_from_stdin():
    print("脚本:")
    return sys.stdin.read()


def copy_file_with_rename(file, save_path, person, content, index):
    base_name = content + ".ogg"
    target_dir = os.path.join(save_path, person)
    target_path = os.path.join(target_dir, base_name)

    # 如果目标目录不存在，创建它
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 检查目标文件是否存在，若存在则重命名
    # if os.path.exists(target_path):
    #     print(f"File '{target_path}' already exists.")
    #     i = 2
    #     while True:
    #         new_name = f"{content}({i}).ogg"
    #         new_target_path = os.path.join(target_dir, new_name)
    #         if not os.path.exists(new_target_path):
    #             target_path = new_target_path
    #             break
    #         i += 1

    # 复制文件到目标路径
    shutil.copy(file, target_path)
    print(f"File copied {os.path.basename(file)} to index: {index + 1}/{b} - '{target_path}'")


# text = read_from_stdin()

with open(r'..\scratch_2.txt', 'r',
          encoding='utf-8') as file:
    text = file.read()
find = re.findall('dwave .*?"z\\\\(.*?)\\.ogg"\n.*?\n?【(.*?)】　[「『（](.*?)[」』）]\\\\', text)
print('=' * 200)

code_find = re.findall('(?:^|\n)\\*(?:seen|SEEN)(.*?)_z', text)
if len(code_find) != 1:
    raise Exception(f"seen数量不符: {code_find}")
else:
    code = code_find[0]
files = glob.glob(f"\KOE\z{code}#*.ogg")
files.sort()
save_path = r"F:\temp"

first_index = None
a = len(find)
b = len(files)
index_from = From.Text
debug = False
add = 0
for i in range(len(find)):
    if index_from == From.Count:
        index = index1 = i
    else:
        index1 = int(find[i][0][2:])
        # if index1>2300000:
        #     index1-=1000000
        if first_index is None:
            first_index = index1
        index = index1 - first_index
        index += add
        # if index>66:
        #     index-=1
    person = find[i][1]
    content = find[i][2]

    if debug:
        try:
            print(f"{index - add} {index}/{b - 1} ({index + 1}/{b})", index1, files[index], person, content)
        except IndexError:
            raise IndexError(f"index: {index}, {index1}, {person}, {content}")
        # print(file, save_path, person, content, index)
    else:
        if content in ["………", "……？", "？", "……！", "～～～", "……", "？……", "？？？", "？？"]:
            continue

        file = files[index]

        os.makedirs(os.path.join(save_path, person), exist_ok=True)

        copy_file_with_rename(file, save_path, person, content, index)
