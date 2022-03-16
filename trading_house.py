import TestCheck as tc
import player as pl
import Items as IT
import Sentences as sc


class Shop:
    def __init__(self, item_dic, oos=[]):
        self.items = item_dic
        self.out_of_stock = oos
        # self.out_of_stock = {IT.itemdict[k] for k in oos}

    def printItems(self):
        print(self.items)

    def showGoods(self):

        index = 1
        for key, value in self.items.items():
            print(f'{index}. {value}')
            index = index + 1
        print(f'{index}. Nothing')

    def buy(self, playerObj):
        ItemsList = list(self.items.values())
        ItemsList.append(0)
        IDList = list(self.items.keys())

        # print(IDList)
        isShop = True
        while isShop:
            answer = tc.input_commend(ItemsList, "What would you like to purchase?[Enter number]",
                                      show_options=False, text_check=False, getback=False)
            selected_item_index = answer - 1
            if answer == len(ItemsList):
                isShop = False
                break
            # print("Check OOS")
            # print(selected_item_index)
            # print(ItemsList[selected_item_index])
            # print(self.out_of_stock)

            item_id = list(self.items.keys())[list(self.items.values()).index(ItemsList[selected_item_index])]
            # print(item_id)
            if item_id in self.out_of_stock:

                # Dried rhubarb leaf | Bay leaves | Rose Petals | Catnip
                if ItemsList[selected_item_index] == IT.itemdict["G4"] or \
                        ItemsList[selected_item_index] == IT.itemdict["A4"] or\
                        ItemsList[selected_item_index] == IT.itemdict["L5"] or\
                        ItemsList[selected_item_index] == IT.itemdict["L6"]:
                    sc.NPC("Apothecary", f"{ItemsList[selected_item_index]}... Let me check.")
                    sc.NPC("Apothecary", "Sorry, I dont see it on the shelf..")
                    sc.player("Do you know where I can get it?")
                    sc.NPC("Apothecary", "Maybe some sprout in the garden.")

                 # Blood meal
                elif ItemsList[selected_item_index] == IT.itemdict["G5"]:
                    sc.NPC("Apothecary", f"{ItemsList[selected_item_index]}... ")
                    sc.NPC("Apothecary", "You’re treading dangerous grounds, young witch.")
                    sc.NPC("Apothecary", "What you are looking for is in a house in the better part of town, "
                                         "but you’ll have to find a way not to get eaten alive there -")
                    sc.NPC("Apothecary", "it’s rumoured to be crawling with blood sucking vampires.")
                    sc.NPC("Apothecary", "They say their queen likes her roses, but nothing would grow without "
                                         "blood-meal next to her den.")
                    sc.NPC("Apothecary", "The ol’ gardener is always keeping anyone from touching his blood-meal, "
                                         "might be the blood sucker charmed him.")
                    sc.NPC("Apothecary", " Might be she just threatened him. Either way all of it is in that house.")
                    sc.player("I see.. you know where exactly?")
                    sc.NPC("Apothecary", "No. But all the rumors cross the bartender ears.")
                    sc.player("Thanks for the tip. I should look into it.")






                # Clover blossom
                elif ItemsList[selected_item_index] == IT.itemdict["A3"]:
                    sc.NPC("Apothecary", "This ingredient shouldn't be on sell. I burnt what was left.")
                    sc.player("Why, its not dangerous?")
                    sc.NPC("Apothecary", "Direct order from the church. The priest demanded it himself.")
                    sc.player(f"Very strange... What the priest have against {ItemsList[selected_item_index]}?")
                    sc.NPC("Apothecary", "Dont no. But all the rumors cross the bartender ears..")
                    sc.player("Thanks for the tip. I should look into it.")

                # Laurel leaves
                elif ItemsList[selected_item_index] == IT.itemdict["A5"]:
                    sc.NPC("Apothecary",
                           f"{ItemsList[selected_item_index]} is a very rare plant. I dont sell anymore.")
                    sc.player("Do you know where can I find some??")
                    sc.NPC("Apothecary",
                           "If you wish for danger, you can find in on The Naked Tree, in The Dark Forest")
                    sc.player("The Dark Forest?")
                    sc.NPC("Apothecary",
                           "Take the Unknown road and you will find it.")
                    sc.NPC("Apothecary",
                           "I should warn you, most of the people that get in, never find the way out")
                    playerObj.addItem('URP')
                    sc.player("Thanks for the tip. But Im not most people.")

            else:
                playerObj.addItem(IDList[selected_item_index])
            continue_shop = tc.input_commend(["y", "n"], "Anything else?[y/n]",
                                             show_options=False, getback=False)
            if continue_shop == 'n':
                isShop = False

        return playerObj

    def enter(self, playerObj):
        self.showGoods()
        playerObj = self.buy(playerObj)
        return playerObj


def get_sub_dic(sub_list):
    sub_dic = {k: IT.itemdict[k] for k in sub_list if k in IT.itemdict}
    return sub_dic


# Apothecary store
items_apothecary_store = \
    ["G1", "G2", "G3", "G4", "G5", "A1", "A2", "A3", "L1", "L2", "L3", "L4", "L5", "L6", "A4", "A5"]
items_apothecary_store_oos = ["G4", "G5", "A3", "L5", "L6", "A5", "A4"]
apothecary_store_dic = get_sub_dic(items_apothecary_store)
ApothecaryStore = Shop(item_dic=apothecary_store_dic, oos=items_apothecary_store_oos)

# Apothecary garden
items_apothecary_garden = ["G4", "A4", "L5", "L6"]
apothecary_garden_dic = get_sub_dic(items_apothecary_garden)
ApothecaryGarden = Shop(item_dic=apothecary_garden_dic)

# Black Market
items_black_market = ["A3", "S1", "S2", "L7", "L8"]
black_market_dic = get_sub_dic(items_black_market)
BlackMarket = Shop(item_dic=black_market_dic)

def main():
    # Apothecary store
    items_apothecary_store = \
        ["G1", "G2", "G3", "G4", "G5", "A1", "A2", "A3", "L1", "L2", "L3", "L4", "L5", "L6", "A4", "A5"]
    items_apothecary_store_oos = ["G4", "G5", "A3", "L5", "L6", "A5", "A4"]
    apothecary_store_dic = get_sub_dic(items_apothecary_store)

    # Apothecary garden
    items_apothecary_garden = "G4", "A4", "A5", "L5", "L6"
    apothecary_garden_dic = get_sub_dic(items_apothecary_garden)

    # Black Market
    items_black_market = ["A3", "S1", "S2", "L7", "L8"]
    black_market_dic = get_sub_dic(items_black_market)

    print(IT.itemdict.items())
    print(IT.itemdict["A1"])

    print(list(IT.itemdict.keys())[list(IT.itemdict.values()).index("Laurel leaves")])
    # print(get_key_by_value("Laurel leaves"))
    # Market = Shop(item_dic=apothecary_store_dic, oos=items_apothecary_store_oos)
    Market = Shop(item_dic=apothecary_store_dic, oos=items_apothecary_store_oos)
    Market.printItems()
    Market.showGoods()
    pl.Roni = Market.buy(pl.Roni)
    # pl.Roni.lookBag()



if __name__ == '__main__':
    main()
