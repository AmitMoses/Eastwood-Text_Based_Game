import Sentences as sc


class Player:
    def __init__(self):
        self.HP = 100
        self.bag = []
        self.keys = []

    def addItem(self, item):
        self.bag.append(item)

    def lookBag(self):
        print("Bag:" + str(self.bag))

    def lookKey(self):
        print("Keys:" + str(self.keys))

    def checkKeys(self, key):
        isKey = False
        if key in self.keys:
            isKey = True
        return isKey

    def checkBag(self, key):
        isKey = False
        if key in self.bag:
            isKey = True
        return isKey

    def makePotion(self, Ingredients):
        isIng = True
        for ing in Ingredients:
            if not self.checkBag(ing):
                sc.narrator('you lack of: ' + ing)
                isIng = False
        if not isIng:
            sc.narrator('You need to get all the require ingredients')
        else:
            for ing in Ingredients:
                self.bag.remove(ing)
            self.keys.append('potion')


def main():
    roni = Player()
    recipe = ['a', 'b', 'c']
    roni.lookBag()
    roni.lookKey()
    roni.makePotion(recipe)
    roni.addItem('a')
    roni.addItem('b')
    roni.addItem('c')
    roni.makePotion(recipe)
    roni.lookBag()
    roni.lookKey()




if __name__ == '__main__':
    main()
