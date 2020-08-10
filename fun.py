
def dealData(L):
    """ 格式处理和数据处理 """

    fail = ["待收入", "待支出"] # 交易未成功的状态说明

    l = []
    for i, row in enumerate(L):
        ### 去除全部空格
        list_row_ed = []
        for val in row:
            val = val.strip()
            list_row_ed.append(val)

        if not (list_row_ed[1] in ["收入", "支出"]):
            continue

        if list_row_ed[-1] in fail:
            continue

        ### 时间
        time_str = list_row_ed[0].split(" ")
        time_str = time_str[0]
        time_str = time_str.split("-")[-1]
        time_int = int(time_str)
        list_row_ed[0] = time_int

        ### 保存
        l.append(list_row_ed)
    
    return l