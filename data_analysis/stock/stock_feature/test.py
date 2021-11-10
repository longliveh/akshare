

import pickle

def loadData(filename) -> dict:
    with open(filename, "rb") as file:
        return pickle.load(file)

data = loadData("gdhs_0.pkl")
list = list(range(0, 4530, 500))
for i in range(list.__len__()):
    print(list[i],list[i+1])