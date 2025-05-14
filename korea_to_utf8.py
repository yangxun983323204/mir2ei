import os

srcDir = "./"
for root, _, files in os.walk(srcDir):
    for file in files:
        if file.endswith(".cpp") or file.endswith(".h"):
            filePath = os.path.join(root, file)
            try:
                with open(filePath, 'r', encoding='EUC-KR') as f:
                    content = f.read()
                with open(filePath, 'w', encoding='utf-8') as f:
                    f.write(content)
            except UnicodeDecodeError as e:
                print(f"{filePath}解码失败：{e}，可尝试用'CP949'编码或忽略错误字符")