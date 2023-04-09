class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
        
class Admin:
    def __init__(self):
        self.menu = {}
        self.current_id = 1
        
    def add_food_item(self, food_item):
        food_item.food_id = self.current_id
        self.menu[self.current_id] = food_item
        self.current_id += 1
    
    def edit_food_item(self, food_id, name=None, quantity=None, price=None, discount=None, stock=None):
        food_item = self.menu.get(food_id)
        if not food_item:
            print("Food item not found.")
            return
        if name:
            food_item.name = name
        if quantity:
            food_item.quantity = quantity
        if price:
            food_item.price = price
        if discount:
            food_item.discount = discount
        if stock:
            food_item.stock = stock
    
    def view_menu(self):
        for food_id, food_item in self.menu.items():
            print(f"ID: {food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}")
    
    def remove_food_item(self, food_id):
        if food_id in self.menu:
            del self.menu[food_id]
        else:
            print("Food item not found.")


menu = Admin()

menu.add_food_item(FoodItem("Tandoori Chicken", "4 pieces", 240, 0, 50))
menu.add_food_item(FoodItem("Vegan Burger", "1 piece", 320, 10, 20))
menu.add_food_item(FoodItem("Truffle Cake", "500gm", 900, 5, 10))

menu.view_menu()

menu.edit_food_item(1, price=260, stock=60)

menu.view_menu()

menu.remove_food_item(2)

menu.view_menu()
