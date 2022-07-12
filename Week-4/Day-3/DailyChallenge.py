# CHALLENGE 1
# INSTRUCTIONS:

# 1- Ask a user for a word
# 2- Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

#   Make sure the letters are the keys.
#   Make sure the letters are strings.
#   Make sure the indexes are stored in a list and those lists are values.
#   
#   Examples:

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

user_word = str(input("Gimme a word !!"))
user_word_dictionary = {}

for idx in range (len(user_word)):

    if user_word[idx] not in user_word_dictionary:
        user_word_dictionary[user_word[idx]] = [idx]
        
    else:
        user_word_dictionary[user_word[idx]].append(idx)

print(user_word_dictionary)

# CHALLENGE 2
# INSTRUCTIONS:

# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Examples

# The key is the product, the value is the price

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
money = int(wallet.replace("$", ""))
can_afford = []


for item, price in items_purchase.items():

    dollarless = price.replace("$", "")
    if "," in dollarless:
        dollarless =int(dollarless.replace(",", ""))
    else:
        dollarless =int(dollarless)    
    
    if money > dollarless:
        can_afford.append(item)

if(len(can_afford) == 0):
    can_afford.append("Nothing")
print(can_afford)   

#➞ ["Bread", "Fertilizer", "Water"]

items_purchase2 = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet2 = "$100" 
money2 = int(wallet.replace("$", ""))
can_afford2 = []


for item, price in items_purchase2.items():

    dollarless2 = price.replace("$", "")
    if "," in dollarless2:
        dollarless2 =int(dollarless2.replace(",", ""))
    else:
        dollarless2 =int(dollarless2)    
    
    if money2 > dollarless2:
        can_afford2.append(item)

if(len(can_afford2) == 0):
    can_afford2.append("Nothing")
print(can_afford2)

# ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

items_purchase3 = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet3 = "$1" 
money3 = int(wallet.replace("$", ""))
can_afford3 = []


for item, price in items_purchase3.items():

    dollarless3 = price.replace("$", "")
    if "," in dollarless3:
        dollarless3 =int(dollarless3.replace(",", ""))
    else:
        dollarless3 =int(dollarless3)    
    
    if money3 > dollarless3:
        can_afford3.append(item)

if(len(can_afford3) == 0):
    can_afford3.append("Nothing")
print(can_afford3)

# ➞ "Nothing"