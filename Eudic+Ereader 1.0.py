import os

# 设置需要处理的文件路径，具体到文件名
file_path = r"FILEPATH"

# 读取文件内容
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 分割成段落列表
paragraphs = content.split("\n\n")

# 处理每个段落
processed_paragraphs = []
for p in paragraphs:
    # 分割成行列表
    lines = p.split("\n")
    # 判断是否为需要处理的段落
    if len(lines) == 3 and lines[2].startswith("来源"):
        # 合并第二和第三行
        lines[1] += " " + lines[2]
        # 保留第一行和合并后的第二行
        processed_paragraphs.append(lines[0] + "," + lines[1])

# 将处理后的段落写回文件
with open(file_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(processed_paragraphs))
