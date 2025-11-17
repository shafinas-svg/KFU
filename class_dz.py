import datetime

# Продукт
class Product:
    def __init__(self, title, energy_value):
        self.title = title
        self.energy_value = energy_value

# блюдо
class Dish:
    def __init__(self, dish_name, cost, ingredients):
        self.dish_name = dish_name
        self.cost = cost
        self.ingredients = ingredients
        self.energy = self.compute_energy()
        self.__self_cost = cost/3

    def self_result(self):
        return self.__self_cost


    def compute_energy(self):
        result = 0
        for prod, amount in self.ingredients.items():
            result += (prod.energy_value * amount) / 100
        return result

# Клиент
class Client:
    def __init__(self, client_name):
        self.client_name = client_name

# Покупка
class Purchase:
    def __init__(self, buyer):
        self.dishes = []
        self.buyer = buyer
        self.timestamp = datetime.datetime.now()

    def include_dish(self, dish):
        self.dishes.append(dish)

    def del_dish(self,dish):
        if dish in self.dishes:
            self.dishes.remove(dish)


    def compute_sum(self):
        return sum(dish.cost for dish in self.dishes)

    def compute_total_mass(self):
        mass = 0
        for dish in self.dishes:
            mass += sum(dish.ingredients.values())
        return mass




pr1 = Product("Багет", 265)
pr2 = Product("Моцарелла", 280)
pr3 = Product("Огурцы", 15)

ingredients1 = {pr1: 120, pr2: 80, pr3: 60}
ingredients2 = {pr3: 150, pr2: 50}

dish1 = Dish("Итальянский сэндвич", 220, ingredients1)
dish2 = Dish("Овощной салат", 180, ingredients2)

client = Client("Мария")

purchase = Purchase(client)
purchase.include_dish(dish1)
purchase.include_dish(dish2)
print([i.dish_name for i in purchase.dishes])
purchase.del_dish(dish2)
print([i.dish_name for i in purchase.dishes])

# Сумма заказа
print(purchase.compute_sum()) 
# граммовка
print(purchase.compute_total_mass())

print(dish1.self_result())