#coding = utf-8
import urllib
import re
import time
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getPhotoPageHtml(html):
    reg = 'href="https://www.douban.com/photos/photo/.+?class="photolst_photo"'
    hrefre = re.compile(reg)
    hreflist = re.findall(hrefre, html)
    urllist = []
    for href in hreflist:
        url = href.split('"')[1]
        urllist.append(url)
    return urllist

def getImg(html):
    # reg = 'src="(.+?\.jpg)" alt='
    reg = 'src="(https://img3.doubanio.com/view/photo/l/public.+?.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    print imglist
    t = time.time()
    for imgurl in imglist:
        # urllib.urlretrieve(imgurl, '%s.jpg' % x)
        urllib.urlretrieve(imgurl, '\image\%s.jpg' % t)
    return imglist

def getImgFromUrl(url):
    html = getHtml(url)
    getImg(html)

# html = getHtml("http://pic.yxdown.com/list/0_0_1.html")
html = getHtml("https://www.douban.com/photos/album/1642028967/?start=36")
urllist = getPhotoPageHtml(html)
for url in urllist: 
    getImgFromUrl(url)
# print html
# print getImg(html)