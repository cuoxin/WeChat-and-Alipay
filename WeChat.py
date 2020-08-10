import csv
from fun import dealData

class WeChat():
    def __init__(self):
        self.csv_path = input("WeChat:")

    def getAllBill(self):
        """ 得到完整账单 """

        with open(self.csv_path, "r") as file:
            txt = csv.reader(file)
            self.list_txt = list(txt)[17:]
    
    def dealBill(self):
        """ 处理账单，获取需要的数据 """
        
        ### 需要的列
        self.bill_list = []
        for row in self.list_txt:
            self.bill_list.append([row[0], row[4], row[2], row[5][1:], row[1], row[7]]) ## 针对金额特别操作了一下
        del self.list_txt

        self.bill_list = dealData(self.bill_list)