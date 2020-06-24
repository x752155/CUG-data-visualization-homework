import  requests
def main():
    #   爬取网页
    baseurl = "http://openaccess.thecvf.com/ICCV2019.py"
    html = requests.get(baseurl)
    print(html.encoding)
    f = open("ICCV.Html", "w",encoding="ISO-8859-1")
    for i in html.text:
        #将数据写入文件
        f.write(i)
#关闭文件
    f.close()
if __name__ =='__main__':
    main()
