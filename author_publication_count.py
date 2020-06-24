import  xlrd
import  matplotlib
import  numpy as np
import  csv
import  matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
#使用pandas读取excel文件
xls_file = xlrd.open_workbook('author_message.xls')
name_list = []
name_count=[]
correlation =[0 for i in range(len(name_list))]
correlation = correlation*(len(name_list))
sheet =xls_file.sheet_by_index(0)             # 读sheet，这里取第一个
rows  = sheet.nrows                      # 获得行数
data  = [[] for i in range(rows)]        # 去掉表头，从第二行读数据
for i in range(1, rows+1):
    data[i-1] = sheet.row_values(i-1)[0:20] #
    #for var in data:
        #print(var)
# print(len(data))
# print(len(data[0]))
# print(data[0])
for hang in range(len(data)):
    for lie in range(len(data[0])):
        name = data[hang][lie]
        if(name not in name_list and name != ""):
            name_list.append(name)
            name_count.append(0)
        if(name in name_list):

            index = name_list.index(name)
            name_count[index]+=1

#开始构建二维矩阵，统计交互
author_num = []
author_num.append(0)
actual_length =0
for hang in range(len(data)):
    actual_length =0
    one_paper_author = data[hang]
    if(hang ==931):
        print(one_paper_author)
    for ii in range(len(one_paper_author)):
        if(one_paper_author[ii]==""):
            actual_length = ii
            author_num.append(actual_length)
            break


plot_list = [0 for i in  range(17)]

for i in  range(len(author_num)):
    author_count = author_num[i]
    plot_list[author_count]+=1
plot_list[6]-=1
plot_list[16]+=1
plt.title("论文作者数量的统计折线图", fontsize=15)
plt.xlabel("每篇论文的作者数量", fontsize=15)
plt.ylabel("对应的论文数量", fontsize=15)

x = range(1,18,1)
y = range(0,320,50)
print(plot_list)
for i in range(len(plot_list)):
    plt.bar(i+1,plot_list[i] ,color='steelblue', alpha=0.8)
    plt.text(i+1, plot_list[i]+5, str(plot_list[i]), ha='center', va='bottom', fontsize=15, rotation=0)
plt.plot(x,plot_list,'r-s')
plt.xticks(x)
plt.yticks(y)

plt.show()
