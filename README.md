# CUG-data-visualization-homework
CUG data visualization homework
地大数据可视化课设
包含如下：
1. 使用爬虫爬取ICCV2019信息
2. 分词，清洗，保存
3. 生成词云
4. 生成Gephi所需的两个CSV文件与关系矩阵
详见CSDN博客  https://editor.csdn.net/md/?articleId=106903928  



ICCV.Html ---->  爬取到的ICCV2019信息，网站见博客  
analyse_correlation.py   ----->  生成作者的两个CSV与关系二维矩阵  
analyse_title_correlation.py  ----->这个是标题的，同上  
author.py   ----->  保存作者信息进TXT  
author_publication_count.py  ----->  统计论文的作者数量，画折线柱状图  
get_information.py  ---->获得作者名字分词，保存进EXCEL  
spider.py  ---->  爬虫  
title_information.py  ----> 获得标题分词，保存进EXCEL  
title_length_countpy  ---->  统计标题长度，绘制折线柱状图  
word_cloud.py   ---->  生成词云  
author_counts2.csv   author_weights2.csv   ----->  Gephi绘图所需的两个CSV文件  
命名很差，无视我

