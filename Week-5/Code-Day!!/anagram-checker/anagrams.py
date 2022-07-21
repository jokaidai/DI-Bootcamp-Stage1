import anagram_checker

def check_validate(user_word) -> bool:
    """
    check valide the data inside the user input 
    """

    if " " in user_word:
            print ("One word at the time please...")
            return False

    if  not user_word.isalpha():

        print("Error Error what you chose is not a word ... can not compute .... try again.  ")
        return False
    else:

        if anagram_checker.AnagramChecker.is_valid_word(user_word):
            return True
        else:   
            print("Error Error what you chose is not a proper word .... can not compute ... try again")
            return False


def show_menu() -> str:
    """
    get imput from user or exit 
    """
    
    while True:

        user_word = input("\nWelcome I am the anagrams checker do you want to use me ? (type no to quit ...): ")
        user_word = user_word.lstrip()
        user_word = user_word.rstrip()
        
        if user_word == 'no':
            break

        user_word = user_word.upper()
        if check_validate(user_word):
            return user_word

    return user_word


def main() -> None:
    """
    main function that handle the all program
    """

    user_word = show_menu()
    checker = anagram_checker.AnagramChecker()

    if user_word == 'no':
        print("See you next time :)")
    else:
        anagram_list = checker.get_anagrams(user_word)

        if anagram_list == []:
            anagram_list.append("No anagrams found :(")
            anagram_list = ''.join(anagram_list)

        print(f"Your Word: {user_word}\nAnagrams: {anagram_list}")

main()
