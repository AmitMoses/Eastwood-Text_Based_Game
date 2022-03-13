import Sentences as sc
import Items as IT


# "G1": "Pomegranate seeds",
#     "G2": "Comfry root",
#     "G3": "Clematis seed",
#     "G4": "Dried rhubarb leaf",
#     "G5": "Blood meal",


class Player:
    def __init__(self):
        self.HP = 100
        # self.bag = [IT.itemdict["URP"]]
        self.bag = ["Unknown-road-pass", "charm of love"]
        self.potion = []
        self.PotionRecipes = IT.PotionRecipes_dict
        self.KeyItems = ['key_1', 'key_2', 'key_3']


    def addItem(self, item_id):
        item = IT.itemdict[item_id]
        sc.narrator(f'Congratulation! {item} added to your item bag')
        self.bag.append(item)

    def lookBag(self):
        print("Bag:" + str(self.bag))

    def lookPotion(self):
        print("Keys:" + str(self.potion))

    def checkPotion(self, potion):
        isPotion = False
        if potion in self.potion:
            isPotion = True
        return isPotion

    def checkBag(self, item_id):
        item = IT.itemdict[item_id]
        isItem = False
        if item in self.bag:
            isItem = True
        return isItem

    def makePotion(self, Recipe):
        if Recipe in self.PotionRecipes.keys():
            sc.player("I know this recipe!")
        else:
            print("unknown recipe")
            return
        isIng = True
        Ingredients = self.PotionRecipes[Recipe]
        for ing in Ingredients:
            if not self.checkBag(ing):
                sc.narrator('you lack of: ' + ing)
                isIng = False
        if not isIng:
            sc.narrator('You need to get all the require ingredients')
        else:
            for ing in Ingredients:
                self.bag.remove(IT.itemdict[ing])
            self.bag.append(Recipe)
            sc.narrator(f"you just make a {Recipe} potion!")


Roni = Player()


def main():
    roni = Player()
    recipe = "A"
    roni.lookBag()
    roni.lookPotion()
    roni.makePotion(recipe)
    # roni.addItem('A1')
    roni.addItem('A2')
    roni.makePotion(recipe)
    # roni.lookBag()
    # roni.lookPotion()


if __name__ == '__main__':
    main()
