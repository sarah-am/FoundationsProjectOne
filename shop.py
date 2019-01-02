####################### DO NOT MODIFY THIS CODE ########################
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

print("\nWelcome to " + cupcake_shop_name + "!\n")

def print_menu():
  print("Behold, our glorious menu:")
  for item in menu:
    print(" - " + item.title() + " (KD%.3f)" %menu[item])

def print_originals():
    print("\n"+"Our original flavor cupcakes are (KD%.3f each):" % original_price)
    for item in original_flavors:
        print(" - " + item.title())
 
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

def get_order():
    # order_list = []
    print("\nWhat would you like to order?\n" + "(Enter the exact spelling of the item you want. Type 'Exit' to end your order.)")
    while True:
        order = str(input(" > "))
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
        if order in menu:
            total += menu[order]
    return total

def accept_credit_card(get_total_price):
    if get_total_price(order_list) >= 5:
        print("Your order is eligible for credit card payment.")

def print_order(order_list):
    print("\nYour order is: ")
    for item in order_list:
        print(" - " + item.title())
    print("\nThat'll be KD%.3f" % get_total_price(order_list))
    accept_credit_card(get_total_price)
    print("Thank you for shopping at " + cupcake_shop_name + "!\n")
