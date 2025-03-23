#Online shopping cart

#building the class that represents an item in the shopping cart
class ItemToPurchase:
    def __init__(self, name = 'none', price = 0, quantity = 0, description = 'none'):
        self.item_name = name
        self.item_price = price
        self. item_quantity = quantity
        self. item_description = description

    def print_item_cost(self):
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}'

    def print_item_description(self):
        return f'{self.item_name}: {self.item_description}'

#building the class that represents a shopping cart
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print('Item is not in the cart, nothing removed.')

    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                found = True
                if item.item_description != 'none':
                    cart_item.item_description = item.item_description
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                break
        if not found:
            print('Item is not in the cart, nothing modified.')
            
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    
    def get_cost_of_cart(self):
        return sum(item.item_quantity * item.item_price for item in self.cart_items)
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f'Number of Items: {self.get_num_items_in_cart()}')
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(item.print_item_cost())
            print(f'Total: ${self.get_cost_of_cart()}')
    
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print('Item Descriptions')
        for item in self.cart_items:
            print(item.print_item_description())

#function that displays the menu and user choices
def print_menu(cart):
    while True:
        print('\nMENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print("i - Output items' descriptions")
        print('o - Output shopping cart')
        print('q - Quit')
        choice = input('Choose an option: ')
        
        if choice == 'q':
            break
        elif choice == 'a':
            name = input('Enter item name: ')
            description = input('Enter item description: ')
            price = int(input('Enter item price: '))
            quantity = int(input('Enter item quantity: '))
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
        elif choice == 'r':
            name = input('Enter name of item to remove: ')
            cart.remove_item(name)
        elif choice == 'c':
            name = input('Enter name of item to modify: ')
            description = input('Enter new description (or leave blank to keep current): ') or 'none'
            price = input('Enter new price (or leave blank to keep current): ')
            quantity = input('Enter new quantity (or leave blank to keep current): ')
            
            price = int(price) if price else 0
            quantity = int(quantity) if quantity else 0
            
            item = ItemToPurchase(name, price, quantity, description)
            cart.modify_item(item)
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            print('\nOUTPUT SHOPPING CART')
            cart.print_total()
        else:
            print('Invalid option, please try again.')


#main function to initialize the shopping cart program
def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


#entry point for the program
if __name__ == '__main__':
    main()
