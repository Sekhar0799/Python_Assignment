class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

class Admin:
    def __init__(self):
        self.users = []

    def register_user(self, full_name, phone_number, email, address, password):
        user = User(full_name, phone_number, email, address, password)
        self.users.append(user)

    def login_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None  

    def show_menu(self):
        print("Menu:")
        print("1. Tandoori Chicken (4 pieces) [INR 240]")
        print("2. Vegan Burger (1 Piece) [INR 320]")
        print("3. Truffle Cake (500gm) [INR 900]")

    def place_order(self, user, item_numbers):
        items = []
        for number in item_numbers:
            if number == 1:
                items.append("Tandoori Chicken (4 pieces) [INR 240]")
            elif number == 2:
                items.append("Vegan Burger (1 Piece) [INR 320]")
            elif number == 3:
                items.append("Truffle Cake (500gm) [INR 900]")
        order = {"user": user.full_name, "items": items}
        user.orders.append(order)

    def view_order_history(self, user):
        print("Order History:")
        for index, order in enumerate(user.orders):
            print(f"{index + 1}. {order['user']}: {', '.join(order['items'])}")

    def update_profile(self, user, full_name, phone_number, email, address, password):
        user.full_name = full_name
        user.phone_number = phone_number
        user.email = email
        user.address = address
        user.password = password

restaurant = Admin()

restaurant.register_user("Sekhar Reddy", "1234567890", "chandrasekhar@com", "123 Main St, Anytown, INDIA", "password123")

user = restaurant.login_user("chandrasekhar@com", "password123")

restaurant.show_menu()

restaurant.place_order(user, [2, 3])

restaurant.view_order_history(user)

restaurant.update_profile(user, "Sekhar Reddy", "0987654321", "chandrasekhar@com", "456 Second St, Othertown, INDIA", "newpassword456")

# output 
1. Tandoori Chicken (4 pieces) [INR 240]
2. Vegan Burger (1 Piece) [INR 320]
3. Truffle Cake (500gm) [INR 900]
Order History:
1. Sekhar Reddy: Vegan Burger (1 Piece) [INR 320], Truffle Cake (500gm) [INR 900]
