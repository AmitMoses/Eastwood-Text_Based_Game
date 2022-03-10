import TestCheck as tc
import player as pl
import Items as IT
import Sentences as sc

class Shop:
    def __init__(self, item_dic):
        self.items = item_dic

    def printItems(self):
        print(self.items)

    def showGoods(self):
        index = 1
        for key, value in self.items.items():
            print(f'{index}. {value}')
            index = index + 1

    def buy(self, playerObj):
        ItemsList = list(self.items.values())
        IDList = list(self.items.keys())

        print(IDList)
        isShop = True
        while isShop:
            answer = tc.input_commend(ItemsList, "What would you like to purchase?[Enter number]",
                                      show_options=False, text_check=False, getback=False)
            selected_item_index = answer - 1
            print(ItemsList[selected_item_index])
            playerObj.addItem(IDList[selected_item_index])
            continue_shop = tc.input_commend(["y", "n"], "Anything else??[y/n]",
                                      show_options=False, getback=False)
            if continue_shop == 'n':
                isShop = False

        return playerObj

def getSubDic(sub_list):
    sub_dic = {k:IT.itemdict[k] for k in sub_list if k in IT.itemdict}
    return sub_dic


def main():
    print(IT.itemdict.items())
    Market = Shop(item_dic=IT.itemdict)
    Market.printItems()
    Market.showGoods()
    # pl.Roni = Market.buy(pl.Roni)
    # pl.Roni.lookBag()

    items_black_market = ["A3", "S1", "S2", "L7", "L8"]
    items_apothacety_store = \
        ["G1", "G2", "G3", "G4", "G5", "A1", "A2", "A3", "L1", "L2", "L3", "L4", "L5", "L6", "A4", "A5"]
    black_market_dic = getSubDic(items_black_market)
    apothacety_store_dic = getSubDic(items_apothacety_store)
    print(black_market_dic)


if __name__ == '__main__':
    main()
