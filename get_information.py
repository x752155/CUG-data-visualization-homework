from bs4 import BeautifulSoup
file = open("./ICCV.Html","rb")
html = file.read()
bs  = BeautifulSoup(html,"html.parser")
import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
author_excel = workbook.add_sheet('My Worksheet')
numx=-1
for item in bs.find_all('div', class_="bibref"):#从引用提取信息
    #print(item.text)
    numx+=1
    item = str(item.text)
    i = item.find('author')
    i2 = item.find('title')
    i3 = item.find('booktitle')
    author = item[i+10:i2-4]#作者信息划片
    author = author.split(" and ")    #首先使用and分离
    for ii in range(len(author)):
        author[ii] = author[ii].replace(", "," ")#将逗号用空格分离
        author[ii] = author[ii].replace(" ","_")#将空格用_连接
    for i in range(len(author)):
            author_excel.write(numx,i,author[i])
    print(author)
workbook.save("author_info.xls")

