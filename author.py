from bs4 import BeautifulSoup
fil = open("./ICCV.Html","rb")
html = fil.read()
bs  = BeautifulSoup(html,"html.parser")

txt = 'author_full_name.txt'
numx=-1
with open(txt,'w') as file:
    for item in bs.find_all('div', class_="bibref"):
        numx+=1
        item = str(item.text)
        i = item.find('author')
        i2 = item.find('title')
        i3 = item.find('booktitle')
        author = item[i+10:i2-4]#作者信息
        author = author.split(" and ")    #首先使用and分离
        for ii in range(len(author)):
            author[ii] = author[ii].replace(", ","_")#将逗号用空格分离
            author[ii] = author[ii].replace(" ","_")#将逗号用空格分离
        for i in range(len(author)):
            print(author[i])
            file.write(author[i]+',')




