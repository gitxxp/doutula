import requests
from bs4 import BeautifulSoup
import urllib
import os #跨平台兼容
n = 0#计数
p = 1
#新建文件夹
folder = os.getcwd()+'/img' # xxx = os.getcwd() #获取当前绝对路径
test=os.path.exists(folder)
if not test:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.mkdir(folder)            #--------------------创建img文件夹
 
        print('初始化...')
        
else:
        # 如果目录存在则不创建，并提示目录已存在
        print('初始化完成...')
       
#定义下载器模块
def download(url):
    name = img['alt']+url[-4:]#图片重名命
   
    download_file = os.path.join('img',name)#跨平台兼容 融合文件夹路径+图片名
    try:
            urllib.request.urlretrieve(url,filename=download_file)
    except:
           print('下载失败')
           pass        
    
#http头
head = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
             }

#开始获取网页
while p <= int(input('输入要爬取的页数')):
        a = requests.get('http://www.doutula.com/photo/list/?page='+str(p),headers=head)
        print('当前第'+str(p)+'页')
        p += 1
        content = a.content#获取整个网页内容
        soup = BeautifulSoup(content,'lxml')#定义工具
        list = soup.find_all('img',attrs={'img-responsive lazy image_dta'})#图片选择
        #准备输出
        for img in list:
                url = img['data-original']#从img中筛选出图片下载真实地址
                print('成功下载第'+str(n)+'张')
                n = n+1
                print('----'*10)
                download('https'+url[4:])#传入下载器 ps：不知为什么无法支持http，只能手动把http改成https，报错<URLError: type: socks5>

