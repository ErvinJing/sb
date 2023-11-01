# -*-coding:utf-8-*-
# @Time    :2023/10/3014:30
# @Author  :JZW
# @Email   :1615573929@qq.com
# @File    :hanshu.py
# @Software:PyCharm



import csv


def hanshu_csv(file):
    mylist=[]
    with open(file,"r",encoding="utf-8") as f:
        data=csv.reader(f)
        for i in data:
            mylist.append(i)
        del mylist[0]
        return mylist
if __name__ == '__main__':
    datc = hanshu_csv(r"C:\Users\JZW\Desktop\datas.csv")
    print(datc)
