import os

for path, dirs, files in os.walk('/home/luo3300612/PycharmProjects/scripts/code'):
    print(f"path:{path}")
    print("dirs")
    for dir in dirs:
        print(dir)
    print("files")
    for file in files:
        print(file)


if os.path.exists("ABC"): # 检查文件是否存在
    print("YES")