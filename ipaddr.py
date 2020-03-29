import requests
from lxml import etree
import  optparse
import random
import sys
'''
date 20200326
Author cmdback
主要是使用站长工具查询IP地址的功能进行批量进行查询IP地址的小工具
'''
user_agent_list = [
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
"(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
"(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
"(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
"(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
"(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
"(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
"(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
"(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
"(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
"(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
"(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
"(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
"(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
"(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
"(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
"(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
"(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
"(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
#设置UA头部信息进行伪装
headers = {
'User-Agent': random.choice(user_agent_list)
}
#将查询的IP集合存在在txt文档中
def open_ips():
    #将需要查询的IP地址归属地的IP存放在一个txt文件中
    with open('ip.txt','r') as f:
        ips = f.readlines()
        for ip in ips:
            if ip:
                main(ip.strip())
            else:
                break
# 主函数
def main(ip):
    try:
        url = "http://ip.tool.chinaz.com/{}".format(ip)
        res = requests.get(url)
        # 站长工具进行查询的话就就执行以下代码
        html = etree.HTML(res.text,etree.HTMLParser())
        ip_info = html.xpath('//div/p[2]/span/text()')
        ipaddrs = ip_info[2] + "归属地是：" + ip_info[5]
        print("正在查询{}".format(ipaddrs))
        with open('outfile.txt','a+',encoding="utf-8") as f:
            f.writelines(ipaddrs+'\n')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    usage = "python  -f file"
    parse = optparse.OptionParser(usage)
    parse.add_option('-f','--file',dest="file",help="Enter a ipaddr file")
    parse.add_option('-o', '--outfile', dest="outfile", help="Enter a ipaddr outfile")
    (options,arges) = parse.parse_args()
    if options.file == None :
        print(parse.usage)
        sys.exit(0)
    else:
        file = options.file
    open_ips()