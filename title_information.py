from bs4 import BeautifulSoup
import  collections
file = open("./ICCV.Html","rb")
html = file.read()
bs  = BeautifulSoup(html,"html.parser")
import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
title_excel = workbook.add_sheet('My Worksheet')
numx=-1
for item in bs.find_all('div', class_="bibref"):
    #print(item.text)
    numx+=1
    item = str(item.text)
    i = item.find('author')
    i2 = item.find('title')
    i3 = item.find('booktitle')
    title = item[i2+9:i3-4]#标题信息
    title = title.split(" ")
    for i in range(len(title)):
        title[i] =title[i].replace(":","")
        title[i] =title[i].replace(",","")
        title_excel.write(numx,i,title[i])
    print(title)
workbook.save("title_info.xls")

