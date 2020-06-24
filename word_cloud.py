import matplotlib.pyplot as plt

from wordcloud import WordCloud
# 1.读入txt文本数据
file = open(u'title.txt','r',encoding='utf-8').read()
word_cloud = WordCloud(
        background_color='white',
        width=800,
        height=600,
       max_font_size=80,  )
word_cloud.generate(file)
word_cloud.to_file(r"title.png")
# 以图片的形式显示词云
plt.imshow(word_cloud)
# 关闭图像坐标系
plt.axis("off")
plt.show()
