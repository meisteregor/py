# -*- coding: utf-8 -*-
import random
import logging

logging.basicConfig(level=logging.INFO,
                    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-2s [%(asctime)s]  %(message)s')

# Constants:
CENTIMETER_FLOWER_LENGTH_FROM = 25
CENTIMETER_FLOWER_LENGTH_TO = 150
FRESHNESS_DAYS_MAX = 6
FRESHNESS_DAYS_MIN = 1
FRESHNESS_DAYS_FRONTIER = 4
FRESH_FLOWER_COST_BYN = 15
NON_FRESH_FLOWER_COST_BYN = 4
CENTIMETER_NORMAL_SIZE_FRONTIER = 100
COST_INCREASE_OVER_NORMAL_SIZE_BYN = 10
COST_INCREASE_FOR_UNIQUE_COLOR_BYN = 13
OXEYEDAISY_LIFECYCLE_DAYS = 10
DAHLIAS_LIFECYCLE_DAYS = 2
CHAMOMILE_LIFECYCLE_DAYS = 5


class Bouquet(object):
    def __init__(self, bouquet=None):
        if bouquet is None:
            bouquet = []
        self.bouquet = bouquet

    def add_items(self, *items):
        for _ in items:
            assert isinstance(_, Flower)
            self.bouquet.append(_)

    def remove_flower(self, item):
        assert isinstance(item, Flower)
        if item in self.bouquet:
            self.bouquet.remove(item)
            logging.info("Item has been successfully removed from the bouquet")
        else:
            logging.warning("You try to remove flower that is not exists in the bouquet")

    @property
    def bouquet_cost(self):
        return sum(_.cost for _ in self.bouquet)

    @property
    def bouquet_items_count(self):
        return len(self.bouquet)

    @property
    def average_bouquet_lifetime(self):
        return sum(_.lifecycle for _ in self.bouquet) / len(self.bouquet)

    def sorted_by_value(self, key='color'):
        list_to_sort = []
        if key == 'freshness' or key == 'color' or key == 'length' or key == 'cost':
            for _ in self.bouquet:
                list_to_sort.append(_.__dict__)
            # Getting full bouquet info sorted by any existing criteria
            return sorted(list_to_sort, key=lambda k: k[key])
        else:
            raise AttributeError('Unknown sorting criteria')

    def finding_flowers(self, attrib='color'):
        attrib_value_list = []
        name_list = []
        for flower in self.bouquet:
            if not hasattr(flower, attrib):
                logging.warning("There is no such a flower(s) with entered parameters in bouquet!")
            else:
                attrib_value_list.append(getattr(flower, attrib))
                name_list.append(flower.name)
        # Outputting the only 'searching_attribute, id' table if it exists.
        return zip(attrib_value_list, name_list)

    def deconstruct(self):
        for each in self.bouquet:
            each.status = 'dead'
        logging.warning('You have just put to death all the flowers in the bouquet')


# This class defines the flowers cost depending on different factors such as: freshness, color, length
class Flower(object):
    def __init__(self):
        self.status = 'alive'
        self.freshness = random.randint(FRESHNESS_DAYS_MIN, FRESHNESS_DAYS_MAX)  # Initializing flowers of rnd freshness
        self.color = random.randint(1, 3)  # Initializing new flowers of a random color
        if self.color == 1:
            self.color = 'red'
        elif self.color == 2:
            self.color = 'white'
        else:
            self.color = 'black'
        self.length = random.randint(CENTIMETER_FLOWER_LENGTH_FROM, CENTIMETER_FLOWER_LENGTH_TO)
        if self.freshness < FRESHNESS_DAYS_FRONTIER:  # Adding some variety in pricing
            self.cost = FRESH_FLOWER_COST_BYN
        else:
            self.cost = NON_FRESH_FLOWER_COST_BYN
        if self.length > CENTIMETER_NORMAL_SIZE_FRONTIER:
            self.cost += COST_INCREASE_OVER_NORMAL_SIZE_BYN
        if self.color == 'black':
            self.cost += COST_INCREASE_FOR_UNIQUE_COLOR_BYN
        super(Flower, self).__init__()


# Flowers with different average lifecycle and its own user friendly ID in form 'name'+'number'
class Oxeyedaisy(Flower):
    vin = 0

    def __init__(self, name='oxeyedaisy'):
        self.name = name
        self.lifecycle = OXEYEDAISY_LIFECYCLE_DAYS
        Oxeyedaisy.vin += 1
        self.name += str(Oxeyedaisy.vin)
        super(Oxeyedaisy, self).__init__()


class Dahlias(Flower):
    vin = 0

    def __init__(self, name='dahlias'):
        self.name = name
        self.lifecycle = DAHLIAS_LIFECYCLE_DAYS
        Dahlias.vin += 1
        self.name += str(Dahlias.vin)
        super(Dahlias, self).__init__()


class Chamomile(Flower):
    vin = 0

    def __init__(self, name='chamomile'):
        self.name = name
        self.lifecycle = CHAMOMILE_LIFECYCLE_DAYS
        Chamomile.vin += 1
        self.name += str(Chamomile.vin)
        super(Chamomile, self).__init__()


# Setting chapter
oxeyedaisy1 = Oxeyedaisy()
oxeyedaisy2 = Oxeyedaisy()
oxeyedaisy3 = Oxeyedaisy()
dahlias1 = Dahlias()
dahlias2 = Dahlias()
dahlias3 = Dahlias()
chamomile1 = Chamomile()
chamomile2 = Chamomile()
chamomile3 = Chamomile()
wedding_bouquet = Bouquet()
funeral_bouquet = Bouquet()
wedding_bouquet.add_items(oxeyedaisy1, oxeyedaisy2, dahlias1, dahlias2, chamomile1, chamomile2)
funeral_bouquet.add_items(oxeyedaisy3, dahlias3, chamomile3, oxeyedaisy1)

# Outputting chapter
print("Chamomile flower cost is {}BYN".format(chamomile2.cost))
print("Flower color is {}".format(chamomile2.color))
print("Bouquet cost is {}BYN".format(wedding_bouquet.bouquet_cost))  # Total cost
print("Total flowers count in bouquet is {}".format(
    wedding_bouquet.bouquet_items_count))  # Total flowers count in bouquet
print("Average lifetime of wedding bouquet is {} days".format(
    wedding_bouquet.average_bouquet_lifetime))  # Total average lifetime
print('sorted by default:{}'.format(wedding_bouquet.sorted_by_value()))  # Some sort options, 'color' by default
print('sorted by cost:{}'.format(funeral_bouquet.sorted_by_value('cost')))  # Some sort options, 'cost' as a key here

# Checking deconstruct block:
# The answer for the (*) task: we can just use the described deconstruct method that was to develop from the task.
# Than check status attribute of the flower we are looking for. If it's alive - it's not in the bouquet and vice versa
print("chamomlile2 status: {}".format(chamomile2.status))  # Is the flower alive after initializing? - Yes
wedding_bouquet.deconstruct()  # Let's crush the bouquet!!
print("chamomlile2 status: {}".format(chamomile2.status))  # Is it alive after deconstruct? - Sure, not
print("chamomlile3 status: {}".format(
    chamomile3.status))  # A flower which wasn't in the crushed bouquet. Is is alive? - Sure, yes

# Checking finding_flower() block:
print(
    "finding default parameter (color) and mapping it to an object: {}".format(funeral_bouquet.finding_flowers()))
print("finding custom parameter (cost) and mapping it to an object: {}".format(wedding_bouquet.finding_flowers('cost')))

# Checking remove_flower() block:
funeral_bouquet.remove_flower(oxeyedaisy3)  # Removing...
funeral_bouquet.remove_flower(oxeyedaisy3)  # We cannot remove the same flower from the bouquet twice
