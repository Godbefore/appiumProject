import json
import requests

a=r'''{
"Host": "www.runoob.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding": "gzip, deflate",
"Referer": "https://www.baidu.com/link?url=Kc3Z2fGJELS2wL8XIhdA5djtJ7t3HyIFUNeEXSNr0ZjFswiUk094fch2g1G0H5M_lBjK-BBW4sXijaHU2kZ3iq&wd=&eqid=adaf69b00000e263000000065c7cf353",
"Connection": "keep-alive",
"Cookie": "Hm_lvt_3eec0b7da6548cf07db3bc477ea905ee=1547455039,1547545753,1547800520,1547801552; _ga=GA1.2.1905732031.1540606335",
"Upgrade-Insecure-Requests": "1",
"Cache-Control": "max-age=0"
}'''


r=requests.post("http://www.runoob.com/python/python-json.html",json=a)
print(r.content)