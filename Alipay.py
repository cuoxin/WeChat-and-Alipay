import csv
from fun import dealData

class Alipay(object):
    def __init__(self):
        self.csv_path = input("Alipay:")
    
    def getAllBill(self):
        """ 得到完整账单 """

        with open(self.csv_path, "r", encoding="gbk") as file: ## utf-8会出错
            txt = csv.reader(file)
            self.list_txt = list(txt)[5:-7]
    

    def dealBill(self):
        """ 处理账单，得到需要的数据 """
        
        ### 获取需要的列表
        self.bill_list = []
        for row in self.list_txt: ## 需要 2，7，8，9，10，11，15
            self.bill_list.append([row[2], row[10], row[7], row[9], row[8], row[15]])
        del self.list_txt

        self.bill_list = dealData(self.bill_list)

        ### 处理退款数据
        def searchList(L, val):
            """ 专项处理退款对应 """
            for row in L:
                if set(val) < set(row):
                    return True, row[2]
            else:
                return False, None
                
        row_dic = {}
        name_price_row = []  ## 保存名字和价格和序列
        for i, row in enumerate(self.bill_list):
            if "退款" in row[4]:
                name = row[4].split("-")
                name = name[-1]
                name_price_row.append([name, row[3], i])
                row_dic[i] = None

            search_val = [row[4], row[3]]
            result_bool, result_i = searchList(name_price_row, search_val)     
            if result_bool:
                row_i = result_i ## 原本退款条目所在的行数
                row_dic[row_i] = i
                name_price_row.remove([row[4], row[3], result_i]) ## 删除键值对
        
        for val in row_dic:
            if row_dic[val] != None:
                self.bill_list[val] = None
                self.bill_list[row_dic[val]] = None ### 防止下标出错，用None先代替

        try:
            while 1:
                self.bill_list.remove(None)
        except ValueError as e:
            pass
