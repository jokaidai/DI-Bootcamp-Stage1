from random import choice

class Game():
    """
    class that hold all of the necessary function to play a game
    """

    items = ["R", "P", "S"]

    def get_user_item(self:object) -> None:
        """
        get choice from user, check validate the choice and assign it to self
        """

        while True:
            user_imput = input("Select (R)ock, (P)aper or (S)cissors: ")
            user_imput = user_imput.upper()
 
            try:
                int(user_imput)
                print("There is no way of cheating ... so please stop enterring numbers or weird characters in a foolish attemp to break my AI mind !!!!")
            except:
                if user_imput not in Game.items:
                    print("You can only select R for Rock, P for Paper or S for Scissors !!!! You serioussly don't now that game ??? Quit being funny let's play already !! ")
                else:
                    break

        self.user_item = user_imput
    

    def get_computer_item(self:object) -> None:
        """
        get a random choice of item  for the Ai and assign it to self 
        """
        
        self.ai_item = choice(Game.items)

    
    def get_game_result(self:object) -> str:
        """
        compare the user_item and the ai_item and determine who won the game ... send back a str with the result
        """

        if self.user_item == self.ai_item:
            return "draw"
        elif self.user_item == "R" and self.ai_item == "S" or self.user_item == "P" and self.ai_item == "R" or self.user_item == "S" and self.ai_item == "P" :
            return "win"
        else:
            return "loss"


    def play(self:object) -> str:
        """
        handle the game and send the result
        """

        self.get_user_item()
        self.get_computer_item()
        result = self.get_game_result()
        print(f"You chose: {self.user_item}. I chose {self.ai_item} Result: {result}")
        
        return result


