import  xlrd
import  matplotlib
import  numpy as np
import  csv
import  matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
#使用pandas读取excel文件
xls_file = xlrd.open_workbook('title_message.xls')
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
paper_length = []
actual_length =0
for hang in range(len(data)):
    actual_length =0
    one_paper_author = data[hang]
    paper = [i for i in one_paper_author if(len(str(i))!=0)]
    print(str(hang)+"  "+str(paper)+"  "+str(len(paper)))
    paper_length.append(len(paper))

    # if(hang ==931):
    #     print(one_paper_author)
    # for ii in range(len(one_paper_author)):
    #     if(one_paper_author[ii]==""):
    #         actual_length = ii
    #         paper_length.append(actual_length)
    #         break

print(paper_length)

plot_list = [0 for i in  range(20)]
label =[]
for i in range(19):
    label.append(i)
for i in  range(len(paper_length)):
    paper = paper_length[i]
    plot_list[paper-1]+=1
# # plt.pie(plot_list,labels=label,autopct='%1.1f%%')
plt.title("论文标题长度统计折线-柱状图", fontsize=15)
plt.xlabel("论文标题长度", fontsize=15)
plt.ylabel("对应的论文数量", fontsize=15)

x = range(1,21,1)
y = range(0,320,50)
print(plot_list)
for i in range(len(plot_list)):
    plt.bar(i+1,plot_list[i] ,color='steelblue', alpha=0.8)
    plt.text(i+1, plot_list[i]+5, str(plot_list[i]), ha='center', va='bottom', fontsize=15, rotation=0)
plt.plot(x,plot_list,'r-s')
plt.xticks(x)
plt.yticks(y)

plt.show()
