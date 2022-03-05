def pizza_order():
    print('Welcome to Python Pizza Deliveries! 🍕🍕🍕')

    # Get keyboard input
    size = input('What size pizza do you want? S, M, or L ')
    add_pepperoni = input('Do you want pepperoni? Y or N ')
    extra_cheese = input('Do you want extra cheese? Y or N ')

    # Declare price variables
    size_price = 0
    pepper_price = 0
    cheese_price = 0

    # Condition
    if size == 'S':
        size_price = 15
    elif size == 'M':
        size_price = 20
    elif size == 'L':
        size_price = 25
    
    if add_pepperoni == 'Y' and size == 'S':
        pepper_price = 2
    
    if add_pepperoni == 'Y' and (size == 'M' or size == 'L'):
        pepper_price = 3
    
    if extra_cheese == 'Y':
        cheese_price = 1

    print(f"Your final bill is: ${size_price + pepper_price + cheese_price}")

pizza_order()

