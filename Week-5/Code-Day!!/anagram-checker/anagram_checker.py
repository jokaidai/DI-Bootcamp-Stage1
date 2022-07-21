class AnagramChecker():
    """
    class that hold all the function to check anagrams
    """

    with open("./properEngWords.txt", mode = 'r' ) as f:
        data = f.readlines()

    data = [str.rstrip('\n') for str in data]

    
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

    @classmethod
    def is_valid_word(cls:object, user_word:str) -> str: 
        """
        get input from user and check validate return the word if clean  
        """
        
        if user_word in cls.data:
            return user_word   
    
    
    def get_anagrams(self:object, user_word:str) -> list:
        """
        compare the word in param with the data list
        """
        
        anagrams = []
        for word in self.data:
            if AnagramChecker.is_anagram(user_word, word):
                anagrams.append(word)
        return anagrams