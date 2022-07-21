from random import choices

#  Exercise 1 – Random Sentence Generator
# Instructions:
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# 1 - Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# 2 - Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
#    - use the words list to get your random words.
#    - the amount of words should be the value of the length parameter.

# 3 - Take the random words and create a sentence (using a python method), the sentence should be lower case.

# 4 - Create a function called main which will:

#   1 - Print a message explaining what the program does.

#   2 - Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
#        - If the user inputs incorrect data, print an error message and end the program.
#        - If the user inputs correct data, run your code.

def get_words_from_file() -> list:
   """
   store the content of a txt file in the data var (list) and return it
   """

   with open("./ex1WordList.txt", mode = "r") as f:
      data = f.readlines()

   return data


def get_random_sentence(len:int) -> None:
   """
   get random words from a list and create a sentence, the length is define by the parameter 
   """

   data = get_words_from_file()
   clean_data = [str.rstrip('\n') for str in data]
   words_list = choices(clean_data, k = len)
   lower_list = [word.lower() for word in words_list]
   rand_str = " ".join(lower_list)

   print(rand_str)

def main() -> None:
   """
   main method handle the other funct, get the info from the user and check them .
   """

   
   while True:
      user_imput = input("How many words do you want in your sentence ?")

      try:
         user_imput = int(user_imput)
         if 2 <= user_imput <= 20:
            break
         else:
            print("Choose a number between 2 ~ 20 ...")

      except:
        print("Please enter a real number !!!")
   
   get_random_sentence(user_imput)

main()