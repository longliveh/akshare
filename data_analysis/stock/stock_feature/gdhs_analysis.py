"""
近一年股东户数当前最低
"""
import os
import pickle
from akshare.stock_feature import stock_gdhs

from akshare.stock import stock_info


def deal() -> dict:
    all_stocks = stock_info.stock_info_a_code_name()
    l = list(range(0, 4530, 500))
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


def loadData() -> dict:
    with open("data.pkl", "rb") as file:
        return pickle.load(file, True)


if __name__ == '__main__':
    data = deal()
    saveData(data)
