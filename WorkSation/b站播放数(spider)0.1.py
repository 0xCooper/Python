'''
Descripttion: blibli视频播放量爬取
version: 
Author: myc
Date: 2021-02-22 22:24:42
'''
import requests
from bs4 import BeautifulSoup

url1="https://www.bilibili.com/video/BV1F7411e7MJ/?spm_id_from=333.788.videocard.0"
url="https://www.bilibili.com/video/BV1Ap4y1W7MP/"
fake_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; '\
'WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}
response = requests.get(url, headers=fake_headers)
soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
videoview = soup.select('#viewbox_report > div > span.view')
#videoview =videoview.get_text()
#print(videoview)


#提取标签里的详细播放数
videoview=str(videoview)
str1="总播放数"
str2="\">"
index=videoview.find(str1)
index1=videoview.find(str2)
print(videoview[index+len(str1):index1])
