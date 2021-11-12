"""
近一年股东户数当前最低
"""
import os
import pickle
from akshare.stock_feature import stock_gdhs

from akshare.stock import stock_info


def deal() -> dict:
    all_stocks = stock_info.stock_info_a_code_name()
    l = list(range(0, 5001, 500))
    for i in range(l.__len__()):
        segment = all_stocks[l[i]:l[i + 1]]
        print(str(l[i]), str(l[i + 1]))
        data = {}
        if os.path.exists("gdhs_" + str(l[i+1]) + ".pkl"):
            continue
        for index, row in segment.iterrows():
            print(row)
            stock_code = row['code']
            stock_name = row['name']
            gdhs = stock_gdhs.stock_zh_a_gdhs_detail_em(stock_code)
            data[stock_code] = gdhs
        saveData(data,"gdhs_" + str(l[i+1]) + ".pkl")
    return data


def saveData(var, filename):
    with open(filename, "wb") as file:
        pickle.dump(var, file, True)


def loadData(filename) -> dict:
    with open(filename, "rb") as file:
        return pickle.load(file)


def analysis():
    l = list(range(500, 5001, 500))
    dict = {}
    for i in range(l.__len__()):
        dict = {**dict,**loadData("gdhs_" + str(l[i]) + ".pkl")}
    good = {}
    for key in dict:
        df = dict[key]
        if df is not None:
            segment = df[['股东户数统计截止日', '代码','名称', '股东户数-本次','户均持股市值', '股东户数-上次', '股东户数-增减', '股东户数-增减比例', '户均持股数量', '区间涨跌幅', '总市值', '总股本', '股本变动', '股本变动原因', '股东户数公告日期']]
            count = 0
            for index, row in segment.iterrows():
                gdhs_zj = row['股东户数-增减']
                gdhz_zjp = row['股东户数-增减比例']
                if gdhz_zjp > 0:
                    break
                if gdhz_zjp < -10:
                    count += 1
            if count >= 4 and (segment[0:1]["户均持股市值"][0] > 200000):
                good[key] = segment
    for key in good:
        t = good[key]
        print(key)


if __name__ == '__main__':
    # data = deal()
    # saveData(data)
    analysis()