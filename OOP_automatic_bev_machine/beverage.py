"""
Beverage classes
for fully automatic beverage machine program
"""


class Beverage:
    def __init__(self, lactose=False, **kwargs):
        self.name = kwargs.get('name')
        self.price = kwargs.get('price')
        self.caffeine = kwargs.get('caffeine')
        self.calories = kwargs.get('calories')
        self.lactose = bool(lactose)

    def __str__(self):
        return f'\nYour selection: \n' \
               f'{self.name}\n' \
               f'${self.price:.2f}\n' \
               f'Caffeine: {self.caffeine} mg\n' \
               f'Calories: {self.calories} cal\n' \
               f'Contains lactose: {self.lactose}\n'


class Latte(Beverage):
    def __init__(self, lactose=True, **kwargs):
        super().__init__(**kwargs)
        self.lactose = bool(lactose)


class Tea(Beverage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = kwargs.get('color')

    def __str__(self):
        return f'{self.color} {self.name}: ${self.price:.2f}\n' \
               f'Caffeine: {self.caffeine} mg\n' \
               f'Calories: {self.calories} cal\n' \
               f'Contains lactose: {self.lactose}\n'


# =============================================================================
# Condiment class
# =============================================================================
class Condiments:
    def __init__(self, **kwargs):
        self.milk = kwargs.get('milk')
        self.sugar = kwargs.get('sugar')
        self.units_milk = kwargs.get('units_milk')
        self.units_sugar = kwargs.get('units_sugar')

    def confirm_condiments(self):
        if self.milk:
            print(f'Milk: {self.units_milk} units')
        if self.sugar:
            print(f'Sugar: {self.units_sugar} units')
