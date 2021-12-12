import requests
from bs4 import BeautifulSoup
"""
class lesson(self,cname,ename,dep,teacher,cr,wk,time,rq,du):
    def __init__(self):
        self.cname=cname
        self.ename=ename
        
"""
response=requests.post("https://cis.ncu.edu.tw/Course/main/query/byKeywords?year=109&fall_spring=2&selectDept=1092%3A1-4003-0&keyword&week&day&crs_lang_no=0&query=%E6%9F%A5%E8%26A9%A2")
soup=BeautifulSoup(response.text,"lxml")
print(soup)
rawDataOdd=soup.find_all("tr")
for i in rawDataOdd:
    print(i)
    print("----------------------------------------------------")