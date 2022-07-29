import menu_class


def load_manager(item_name:str, item_price:int) -> object:
    """
    get a clean name and price and use them to create a new instance (obj) of type MenuItem 
    """

    new_item = menu_class.MenuItem(item_name, item_price)
    return new_item


def is_valid(type:str, user_input:str) -> bool :
    """
    function to check if a value is the given type
    """

    if type == 'int':
        try:
            int(user_input)
            return True
        except:
            return False 
    
    if type == 'str':
        try:
            int(user_input)
            return False
        except:
            return True


def add_item_to_menu() -> None: 
    """
    get an input from the user check it create an instance and add it to the menu (call to check_validate() ,load_manager and MenuItem.save())
    """

    while True:
        dish = input("Enter a dish please: ")
        if  is_valid('str', dish) == False:
            print("Sorry this dish doesnt exist ...")
        else:
            while True:
                price = input("What price do you want to set ? ")
                if is_valid('int', price):
                    item = load_manager(dish, price)
                    item.save()
                    print("Item was added succesfully !")
                    break
                else:
                    print("Sorry i need a real number to set the price")
            break


def remove_item_from_menu() -> None:
    """
    get an input from the user with what he want to remove from the menu(item_list)
    """

    while True:
        user_input = input("Wich dish do you want to remove from the menu ? ")

        if is_valid('str', user_input):
            unwanted = menu_class.MenuItem.get_by_name(user_input)
            if unwanted == None: 
                print("This dish is not inside the menu")
                break
            else:
                menu_class.MenuItem.delete(unwanted)
                print("The specified dish was succefully deleted from the menu")
                break
        else:
            print("This is not a dish ...")

def show_user_menu() -> None:
    """
    print the option menu until x is selected and call the appropriate functions if something else is selected
    """
    
    while True:

        user_input = input("""      
                MENU
            (a) Add an item
            (d) Delete an item
            (v) View the menu
            (x) Exit
            : 
            """)

        if user_input == 'a':
            add_item_to_menu()

        if user_input == 'd':
            remove_item_from_menu() 

        if user_input == 'v':
           show_restaurant_menu()
        
        if user_input == 'x':
            show_restaurant_menu()
            break
    
		    
def show_restaurant_menu() -> None:
    """
    display the current menu
    """ 
    menu = menu_class.MenuItem.all()
    print("     Restaurant's Menu")
    for item in menu:
        print(f"{item[1]}       price: {item[2]}")

show_user_menu()