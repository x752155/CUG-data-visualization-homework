import pandas as pd
import  xlrd
import  numpy as np
import  csv
import  matplotlib.pyplot as plt
#使用pandas读取excel文件
xls_file = xlrd.open_workbook('title_message1.xls')
name_list = []
name_count=[]
correlation =[0 for i in range(len(name_list))]
print(correlation)
correlation = correlation*(len(name_list))
print(correlation)
sheet =xls_file.sheet_by_index(0)             # 读sheet，这里取第一个
rows  = sheet.nrows                      # 获得行数
data  = [[] for i in range(rows)]        # 去掉表头，从第二行读数据
for i in range(1, rows+1):
    data[i-1] = sheet.row_values(i-1)[0:16] #
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
correlation = [([0]*(len(name_list))) for i in range(len(name_list))]
actual_length =0
for hang in range(len(data)):
    actual_length =0
    one_paper_author = data[hang]
    for ii in range(len(one_paper_author)):
        if(one_paper_author[ii]==""):
            actual_length = ii
            break
    for num in range(actual_length-1):
        for num2 in  range(num+1,actual_length):
            name1 = one_paper_author[num]
            name2 =one_paper_author[num2]
            index1 = name_list.index(name1)
            index2 = name_list.index(name2)
            correlation[index1][index2]+=1
            correlation[index2][index1]+=1
np_co = np.array(correlation)
print(np_co.shape)
x_size,y_size = np_co.shape

plt.matshow(np_co)
plt.show()
f = open('title_weights2.csv','w',encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["Source","Target","Weight"])
for i in range(x_size):
    for j in  range(i,y_size):
        if(np_co[i][j] != 0):
            csv_writer.writerow([name_list[i],name_list[j],np_co[i][j]])
f.close()
fff = open('title_counts2.csv','w',encoding='utf-8')
csv_writer = csv.writer(fff)
csv_writer.writerow(["ID","Label","Weight"])
for i in range(len(name_list)):
    csv_writer.writerow([name_list[i],name_list[i],name_count[i]])
fff.close()





