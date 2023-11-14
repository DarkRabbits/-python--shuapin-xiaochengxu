import xlwings as xw
import random
from pynput.keyboard import Key,Controller
import time
keyboard=Controller()


def send_content(num):
    texts=('合法生效受监管有合同的，众安是上市公司市值超400亿全国超5亿用户，有问题问主播','众安全民普惠保，保费每月最低19元起，每年最高600万医疗保额','众安全民普惠保责任内每年600万保额、保一般医疗和重疾医疗、保医堡内和医堡外','带病也可买，结节，血脂高，高血糖买了也能报','责任内不限制疾病种类，重疾小病和意外，每年六百万保额','保费每月都一样，发送XX岁查询保费','认准我们众安官方直播间，保障范围广每月保费低，发送XX岁查询保费哦','0-60岁 每月19元，年交196元；61-105岁 每月69，年交796元')
    last_content=""
    for i in range(num):
        content=random.choice(texts)
        while content==last_content:
            content=random.choice(texts)
        print('发送内容：',content)
        keyboard.type(content)
        keyboard.press(Key.enter)
        last_content=content
        time.sleep(b)

def get_num():
    num=int(input('发送几次呢？'))
    
    return num



while True:
    num=get_num()
    b=int(input('发送间隔几秒呢?'))
    print('请将光标移动到文本框')
    time.sleep(3)
    for i in range(4):
        print(r"程序还有%d秒运行"%(4-i))
        time.sleep(0.5)
    send_content(num)
    print('发送完成')
    choice=input('是否继续运行，输入Y继续，其他任意键退出')
    if choice!='Y':
        break
