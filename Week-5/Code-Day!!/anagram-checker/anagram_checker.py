class AnagramChecker():
    """
    class that hold all the function to check anagrams
    """

    def __init__(self:object) -> None:

        with open("./properEngWords.txt", mode = 'r' ) as f:
            self.data = f.readlines()

        self.data = [str.rstrip('\n') for str in self.data]

    
    @classmethod
    def  is_anagram(cls:object, user_word:str, word:str) -> bool:
        """
        check if the 2 words in param are anagrams
        """
        
        if user_word == word:
            return False

        check_user = sorted(user_word)
        check_word = sorted(word)

        if check_user == check_word:
            return True
        
        return False


    def is_valid_word(self:object) -> str: # validate will be replace by the function in the other file and will just check if in list 
        """
        get input from user and check validate return the word if clean  
        """

        user_word = input("Chose a word please: ")
        user_word = user_word.upper()

        try:
            int(user_word)
            print("Error invalid word, try again")
        except:
            if user_word in self.data:
                return user_word
            else:
                print("Error not a proper world")
    

    def get_anagrams(self:object, user_word:str) -> list:
        """
        compare the word in param with the data list
        """
        
        anagrams = []
        for word in self.data:
            if AnagramChecker.is_anagram(user_word, word):
                anagrams.append(word)
        return anagrams