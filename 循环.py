import re
# 待匹配的字符串
title = "你好，hello，世界"
# 创建正则表达式，用于只匹配中文
pattern = re.compile(r"[\u4e00-\u9fa5]+")
# 检索整个字符串，将匹配的中文放到列表中
result = pattern.findall(title)
print(result)
while True:
    print(title)



