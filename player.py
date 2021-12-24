import Sentences as sc


class Player:
    def __init__(self):
        self.HP = 100
        self.bag = []
        self.potion = []
        self.PotionRecipes = {
            "A": ['a1', 'a2'],
            "B": ['b1', 'b2'],
            "C": ['c1', 'c2']
        }
        self.KeyItems = ['key_1', 'key_2', 'key_3']

    def addItem(self, item):
        sc.narrator('Congratulation! {} added to your item bag'.format(item))
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

    def checkBag(self, item):
        isItem = False
        if item in self.bag:
            isItem = True
        return isItem

    def makePotion(self, Recipe):
        if Recipe in self.PotionRecipes.keys():
            print("you know this recipe!")
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
                self.bag.remove(ing)
            self.potion.append(Recipe)


Roni = Player()

def main():
    roni = Player()
    recipe = "A"
    roni.lookBag()
    roni.lookPotion()
    roni.makePotion(recipe)
    roni.addItem('a1')
    roni.addItem('a2')
    roni.makePotion(recipe)
    roni.lookBag()
    roni.lookPotion()


if __name__ == '__main__':
    main()
