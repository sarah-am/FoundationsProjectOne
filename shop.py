####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["v####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Wallflour"
signature_flavors = ["pistachio", "lotus", "gingerbread"]
order_list = []

print("Welcome to " + cupcake_shop_name + "!\n")

def print_menu():
  print("Behold, our glorious menu:")
  for item in menu:
    print(" - " + item.title() + "(KD%.3f)" %menu[item])


#------------------ START -------------------#
def print_originals():
    print("\n"+"Our original flavor cupcakes are (KD%.3f each):" % original_price)
    for item in original_flavors:
        print(" - " + item.title())
    print("Our original flavor cupcakes (KD %s each):" % original_price)

    # your code goes here!

#------------------ FINISH -------------------#


#------------------ START -------------------#
def print_signatures():
    print("\n"+"Our signature flavor cupcakes are (KD%.3f each):" % signature_price)
    for item in signature_flavors:
        print(" - " + item.title())

def is_valid_order(item):
  if item.lower() in original_flavors or item.lower() in signature_flavors or item.lower() in menu:
    return True
  else:
    return False
    print("Our signature flavor cupcake (KD %s each):" % signature_price)

    # your code goes here!

#------------------ FINISH -------------------#

def get_order():
    # order_list = []
    print("\nWhat would you like to order?\n" + "(Enter the exact spelling of the item you want. Type 'Exit' to end your order.)")
    while True:
        order = str(input())
        if is_valid_order(order) == True:
            order_list.append(order)
        elif order == "Exit":
            return order_list
        else:
            print("Sorry, please try again.")
             

def get_total_price(order_list):
    total = 0
    for order in order_list:
        if order in signature_flavors:
            total += signature_price
        if order in original_flavors:
            total += original_price     
        if order in sorted(menu):
            total += menu[order] 
    return total

def accept_credit_card(get_total_price):
    if get_total_price(order_list) >= 5:
        print("Your order is eligible for credit card payment.")
#------------------ FINISH -------------------#


#------------------ START -------------------#
def print_order(order_list):
    print("\nYour order is: ")
    for item in order_list:
        print(" - " + item.title())
    print("\nThat'll be KD%.3f" % get_total_price(order_list))
    accept_credit_card(get_total_price)
    print("Thank you for shopping at " + cupcake_shop_name + "!")
    print()
    print("Your order is: ")

    # your code goes here!

#------------------ FINISH -------------------#
anilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = #complete me!
signature_flavors = #complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
