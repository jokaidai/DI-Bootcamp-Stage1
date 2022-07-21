import game

results ={'win': 0, 'loss': 0, 'draw': 0}


def get_user_menu_choice()-> str:
    """
    print a welcome message with a menu to let the player choose the action he want to do
    """

    while True:

        choice = input("Menu:\n(g) Play a new game\n(x)Show scores and exit\n: ")

        try:
            int(choice)
            print("... I am not sure why you enter a number here... ")
    
        except:
        
            if choice == 'g' or choice == 'x':
                break
            else:
                print("Enter g or x  it's pretty simple !!!")
             
    return choice
     

def print_result(results:dict) -> None:
    """
    print the result from the global variable result{}
    """

    print(f"Game Results:\nYou won {results['win']} times\nYou lost {results['loss']} times\nYou drew {results['draw']} times\n")
    print("Thank you for playing !!!")


def main() -> None:
    """
    the main funtion that handle the all program
    """
    print("\nWelcome to Rock, Paper, Scissors !!!\n")

    game_start = game.Game()
    menu_choice = get_user_menu_choice()

    while menu_choice != 'x':
        
        result = game_start.play()
        results[result] += 1
        menu_choice = get_user_menu_choice()
        
    print_result(results)

main()