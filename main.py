import re
import sys
import os

if os.path.exists("patterns.txt") == False:
    print("语言标准不存在！")
    exit()
else:
    # 读取正则表达式文件
    with open('patterns.txt', 'r') as pattern_file:
        patterns = pattern_file.readlines()

# 读取源文件
with open(str(sys.argv[1]), 'r') as source_file:
    source_content = source_file.read()

# 定义替换函数
def replace_patterns(text, patterns):
    for pattern in patterns:
        # 去除末尾换行符
        pattern = pattern.strip()
        # 如果模式非空，则替换
        if pattern:
            text = re.sub(pattern, '', text)
    return text

# 替换源文件中的内容
new_content = replace_patterns(source_content, patterns)

# 将结果保存到新文件
with open('build.py', 'w') as output_file:
    output_file.write(new_content)
print("完成！")