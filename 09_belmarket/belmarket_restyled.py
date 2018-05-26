class Store(object):
    def __init__(self, shop=None):
        if shop is None:
            shop = []
        self.shop = shop

    def add_item(self, item):
        self.shop.append(item)

    def remove_item(self, item):
        if item in self.shop:
            self.shop.remove(item)
            print('item {} was successfully removed'.format(item))
        else:
            AttributeError("There is no such an item in store")

    def overall_price_discount(self):
        return sum(_._price for _ in self.shop)


class Grocery(Store):
    def add_item(self, *items):
        for _ in items:
            if isinstance(_, Food):
                super(Grocery, self).add_item(_)
                print('An item(s): {} was successfully added'.format(_))
            else:
                raise TypeError("Incorrect product assignment!")

    def remove_item(self, *items):
        for _ in items:
            super(Grocery, self).remove_item(_)


class Hardware(Store):
    def add_item(self, *items):
        for _ in items:
            if isinstance(_, Tools):
                super(Hardware, self).add_item(_)
            else:
                raise TypeError("Incorrect product assignment!")

    def remove_item(self, *items):
        for _ in items:
            super(Hardware, self).remove_item(_)


class Goods(object):
    def __init__(self, price=0, discount=None, freezing=False):
        self._price = price
        self.discount = discount
        self.freezing = freezing

    def set_discount(self, discount):
        self.discount = discount
        decrement = 1 - self.discount * 10 ** -2
        self._price = self._price * decrement
        return self._price

    @property
    def reset_discount(self):
        increment = 1 - self.discount * 10 ** -2
        return self._price * 1.0 / increment

    @property
    def freeze_price(self):
        self.freezing *= -1
        if not self.freezing:
            return self._price
        else:
            self._price = self.reset_discount
            return self._price


class Food(Goods):
    pass


class Tools(Goods):
    pass


class Banana(Food):
    pass


class Apple(Food):
    pass


class Ham(Food):
    pass


class Strawberry(Food):
    pass


class Nail(Tools):
    pass


class Axe(Tools):
    pass


class Saw(Tools):
    pass


class Hammer(Tools):
    pass


belmarket = Grocery()
bananas = Banana(6)  # create a banana with 6$ price
strawberry = Strawberry(22)  # create a strawberry with 22$ price
belmarket.add_item(bananas)
belmarket.add_item(strawberry)
print(belmarket.overall_price_discount())  # -> outputs 6+22 -> 28

# ham = Ham()
# belmarket.add_item(ham)
# belmarket.remove_item(ham)

belmarket.remove_item(strawberry)
belmarket.add_item(strawberry)
strawberry.set_discount(50)
# strawberry.freeze_price
print(belmarket.overall_price_discount())  # -> outputs 6+(22/100*50) -> 17
# hammer = Hammer(50)
# belmarket.add_item(hammer)  # -> TypeError("Incorrect product assignment!") should be raised
