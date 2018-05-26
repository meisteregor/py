import random

# List of constants:
PETROL92_COST_USD = 2.2
PETROL95_COST_USD = 2.4
DIESEL_COST_USD = 1.8
MAX_PETROL_RUN_REPAIR_KM = 100000
MAX_DIESEL_RUN_REPAIR_KM = 150000
EXHAUST_STEP_KM = 1000
PETROL_EXHAUST_VALUE_USD = 9.5
DIESEL_EXHAUST_VALUE_USD = 10.5
PERCENT_FUEL_SPAN_INCREASE = 1
POINT_SWAP_PETROL_KM = 50000
INIT_DIESEL_SPAN_LITER_PER = 6
INIT_PETROL_SPAN_LITER_PER = 8
RANDOM_GEN_START_POINT_KM = 55000
RANDOM_GEN_END_POINT_KM = 286000
HOW_MANY_CARS = 100
CAR_STARTING_BUDGET_USD = 10000


# Class Taxopark initialized just in case as it was mentioned in task
class Taxopark(object):
    pass


# Class Producer is logically responsible for release parameters
class Producer(Taxopark):
    vin = 1
    tachograph = 0

    def __init__(self, fuel_type="petrol", tank_full=60, money=CAR_STARTING_BUDGET_USD):
        self.vin = Producer.vin
        self.fuel_type = fuel_type
        self.tank_full = tank_full
        self.money = money
        self.tachograph = Producer.tachograph

        if self.vin % 3 == 0:
            self.fuel_type = "diesel"
        if self.vin % 5 == 0:
            self.tank_full = 75

        Producer.vin += 1

    def product_info(self):  # some in-between info about the cars
        dict_product_info = {'vin': self.vin, 'fuel_type': self.fuel_type, 'tank_full': self.tank_full,
                             'money': self.money, 'distance_reached': self.distance_reached,
                             'tachograph_miles': self.sensor_miles, 'tachograph_km': self.sensor_km}
        return dict_product_info


# Class is responsible for all the repairs & refillings.
class Workshop(Taxopark):
    times_repaired = 0
    times_tank_filled = 0
    times_engine_substitution = 0

    def __init__(self, petrol_repair_cost=500, diesel_repair_cost=700, engine_substitution_cost=3000):
        super(Workshop, self).__init__()
        self.engine_substitution_cost = engine_substitution_cost
        self.times_repaired = Workshop.times_repaired
        self.times_tank_filled = Workshop.times_tank_filled
        self.petrol_repair_cost = petrol_repair_cost
        self.diesel_repair_cost = diesel_repair_cost


# Class contains & refactor in-action dynamic parameters.
class Car(Workshop, Producer):
    fuel_span = 0
    money_for_fuel = 0

    def __init__(self):
        super(Car, self).__init__()
        self.fuel_span = Car.fuel_span
        self.money_for_fuel = Car.money_for_fuel

        if self.fuel_type == "diesel":
            self.fuel_span = INIT_DIESEL_SPAN_LITER_PER
        else:
            self.fuel_span = INIT_PETROL_SPAN_LITER_PER

    def fuel_info(self):
        dict_fuel_info = {'fuel_span': round(self.fuel_span, 1), 'times_tank_filled': self.times_tank_filled,
                          'times_repaired': self.times_repaired, 'money_for_fuel': self.money_for_fuel}
        return dict_fuel_info


# Class Tachograph as an object\detail of the Car
class Tachograph(Car):
    def __init__(self, temp=0):
        self._temp = temp
        super(Tachograph, self).__init__()

    @property
    def sensor_km(self):
        return self._temp

    @property
    def sensor_miles(self):
        return int(round(self._temp * 0.62))


# Route class. Logically belongs to class-tree. It inherits all the classes in this script
# to have a method .run() which spreads upper classes and initialize some new instances if the car begins to move.
class Route(Tachograph):
    distance_to_reach = 0
    distance_reached = 0

    def __init__(self):
        super(Route, self).__init__()

        # self.distance_to_reach = Route.distance_to_reach
        self.distance_to_reach = random.randint(RANDOM_GEN_START_POINT_KM, RANDOM_GEN_END_POINT_KM)
        self.distance_reached = Route.distance_reached

    # This method has no final output, but it was necessary in the process of writing for scoping changes.
    def distance(self):
        dict_distance = {'distance_to_reach': self.distance_to_reach, 'distance_reached': self.distance_reached}
        return dict_distance

    def run(self):
        # In fact the main in-class function that describes driving process & triggers all re-assignments in script.
        while self.distance_to_reach != self.distance_reached:
            self.distance_reached += 1
            self._temp += 1
            if not self.distance_reached % EXHAUST_STEP_KM:
                if self.fuel_type == 'petrol':
                    self.money -= PETROL_EXHAUST_VALUE_USD
                    self.fuel_span *= (1 + PERCENT_FUEL_SPAN_INCREASE * 10 ** -2)
                else:
                    self.money -= DIESEL_EXHAUST_VALUE_USD
                    self.fuel_span *= (1 + PERCENT_FUEL_SPAN_INCREASE * 10 ** -2)
            if not self.distance_reached % int(round(self.tank_full * (self.fuel_span ** -1) * 100)):
                self.times_tank_filled += 1
                if (self.distance_reached <= POINT_SWAP_PETROL_KM) and (self.fuel_type == 'petrol'):
                    self.money -= (PETROL92_COST_USD * self.tank_full)
                    self.money_for_fuel += (PETROL92_COST_USD * self.tank_full)
                elif self.fuel_type == 'petrol':
                    self.money -= (PETROL95_COST_USD * self.tank_full)
                    self.money_for_fuel += (PETROL95_COST_USD * self.tank_full)
                else:
                    self.money -= (DIESEL_COST_USD * self.tank_full)
                    self.money_for_fuel += (DIESEL_COST_USD * self.tank_full)
            if not self.distance_reached % MAX_PETROL_RUN_REPAIR_KM and self.fuel_type == 'petrol':
                self.times_repaired += 1
                self.money -= self.petrol_repair_cost
            if not self.distance_reached % MAX_DIESEL_RUN_REPAIR_KM and self.fuel_type == 'diesel':
                self.times_repaired += 1
                self.money -= self.diesel_repair_cost


# Here would be cut output: from 0 to 6 to improve output readability.
def main():
    some_job = []
    iterator_ = xrange(HOW_MANY_CARS)
    # Generating list of instances to provide some work for them later
    for i in enumerate(iterator_, 1):
        some_job.append(Route())
    # Print some info before they start their voyage
    print('*' * 40 + ' BEFORE RUN INFO ' + '*' * 40)
    for _ in some_job[0:6]:
        print(_.product_info())
        print(_.fuel_info())
    # Ok, let's go!
    for _ in some_job[0:6]:
        _.run()
    # Some 'stars' to increase readability.
    print('*' * 40 + ' AFTER RUN INFO ' + '*' * 40)
    # The work is done. Full info
    for _ in some_job[0:6]:
        print(_.product_info())
        print(_.fuel_info())
        print
    print('*' * 40 + ' TASK OUTPUTS ' + '*' * 40)
    # Task output. 1st print: cars sorted by capitalization. 2nd print: Taxopark money balance.
    list_to_sort = [_.product_info() for _ in some_job[0:6]]
    list_sorted = sorted(list_to_sort, key=lambda k: k['money'], reverse=True)
    print("Main car info sorted by money: {}".format(list_sorted))
    print("Taxopark money balance: {} USD".format((sum(item['money'] for item in list_to_sort))))
    # To have full statistics of 100 cars just delete [0:6] or change it according to your context.


if __name__ == '__main__':
    main()
