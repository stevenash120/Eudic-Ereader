import os
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

def get_wordnet_pos(word):
    """Map POS tag to first character used by WordNet"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN) # default to noun if mapping not found

# 设置需要处理的文件路径，具体到文件名!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
file_path = r"C:xxxxxx\input.txt"

# 读取文件内容
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 分割成段落列表
paragraphs = content.split("\n\n")

# 定义词形还原器
lemmatizer = WordNetLemmatizer()

# 处理每个段落
processed_paragraphs = []
for p in paragraphs:
    # 分割成行列表
    lines = p.split("\n")
    # 判断是否为需要处理的段落
    if len(lines) == 3 and lines[2].startswith("来源"):
        # 进行词性标注
        tokens = nltk.word_tokenize(lines[0])
        tagged_tokens = nltk.pos_tag(tokens)
        # 词形还原
        lemmatized_tokens = [lemmatizer.lemmatize(token, pos=get_wordnet_pos(pos_tag)) 
                             for token, pos_tag in tagged_tokens]
        # 替换原始单词
        lines[0] = lemmatized_tokens[0]
        # 合并第一和第二行
        lines[0] += "," + lines[1]
        # 保留第一行和合并后的第二行
        processed_paragraphs.append(lines[0] + "\n" + lines[2])

# 将处理后的段落写回文件
with open(file_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(processed_paragraphs))
