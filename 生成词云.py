import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np  # 计算
from PIL import Image  # 读取某一个图片

# 对歌词经行切割
# str = "好好学习，天天向上"

str = open("pachong\\name.txt", "r", encoding="UTF-8").read().replace("\n", "").replace("：", "").replace(":", "").replace(" ", "")

# 切割的原理中文词库
# 精确模式  把文本精确的切开，不存在冗余单词
list1 = jieba.lcut(str)
# 拼接
lists = " ".join(list1)
# for s in list: #lcut 等同于
#     print(s)

# 全模式： 把文本中所有可能的词语都扫描出来，可能有冗余
# list2 = jieba.lcut(str, cut_all=True)
# 搜索引擎模式：在精切模式上，对长词再次切分
# list = jieba.lcut_for_search(str)
print(list1)
print(lists)
# print(list)


# 统计一首歌出现的次数
# 把结果放到字典里面去{键值对类型}
# results = {}
# for s in list1:
#     results[s] = results.get(s, 0) + 1 # 第一个s 键 第二个值(第一次没有默认为0)有的话类推加
#
# print(results)

# 排序  lambda X代表一个数组: 代表数组里面的下标X[1]
# resultList = list(results.items())#.items()拿到所有的键值对
# resultList.sort(key=lambda x: x[1], reverse=True)
# print(resultList)

# 指定云词图的模板   np.array(转换指定读取的数据类型)
image = np.array(Image.open("F:\Download\CF.jpg"))

# 使用WordCloud进行云词图的展示  mask(图片的数组类型)
wc = WordCloud(font_path="msyh.ttc", height=800, width=800, mask=image, )
# 根据那个生成云词图
wc.generate(lists)

plt.imshow(wc)  # 设置要显示的对象
plt.axis("off")  # 关闭坐标刻度
plt.show()  # 显示

# 保存
wc.to_file("结果.png")
