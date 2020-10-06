import requests
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
RE=re.compile(r'最新章节！(.*?)</div>')
target=46100683
def gettext(target):
    url='https://www.qb5.tw/book_114408/'+str(target)+'.html'
    res = requests.get(url)
    res = res.text
    soup = BeautifulSoup(res, 'html5lib')
    result = RE.findall(res)
    result = str(result)
    result = BeautifulSoup(result, 'html5lib').prettify()
    result = str(result).replace('<html>\n', '').replace('<head>\n', '').replace('</head>\n', '').replace('<body>\n','').replace('[\'\n', '').replace('<br/>\n', '').replace('</body>\n', '').replace('</html>', '')
    filename1=result.split('\n')
    filename=filename1[0].replace(' ','').replace('\n','')
    filename=filename+'.txt'
    file=open(filename,'w+',encoding='utf-8')
    file.write(result)
if __name__ == '__main__':
    p=Pool(4)
    for i in range(46100683,46100683+2000):
        p.apply_async(gettext,args=(i,))
    p.close()
    p.join()





