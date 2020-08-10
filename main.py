import csv
from Alipay import Alipay
from WeChat import WeChat


def AlipayRun(Ali):
    Ali.getAllBill()
    Ali.dealBill()


def WeChatRun(Wec):
    Wec.getAllBill()
    Wec.dealBill()


def main():
    Ali = Alipay()
    Wec = WeChat()

    AlipayRun(Ali)
    WeChatRun(Wec) 
    """ TODO:
        1. 双线程
        2. 排序
        3. 写入文件
    """


if __name__ == "__main__":
    main()