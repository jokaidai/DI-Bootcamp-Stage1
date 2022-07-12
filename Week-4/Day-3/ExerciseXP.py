#EX1
# Instructions

# Convert the two following lists, into dictionaries.
# Hint: Use the zip method

# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict_from_list = dict(zip(keys, values))
print(dict_from_list)
#EX1

#EX2
#INSTRUCTIONS

# 1-A movie theater charges different ticket prices depending on a person’s age.
#   if a person is under the age of 3, the ticket is free.
#   if they are between 3 and 12, the ticket is $10.
#   if they are over the age of 12, the ticket is $15.

# 2-How much does each family member have to pay ?

# 3-Print out the family’s total cost for the movies.

# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

print("-----regular-----")

price = 0 
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

for name, age in family.items():

    if age < 3:
        print("its free for you sweety :)")
        print("next !")

    elif 3 <= age <= 12:
        print("10$ please :)")
        price += 10
        print("next !")

    else:
        print("15$ please :)")
        price += 15
        print("next !")

print(f"Your final check is {price}$ !!! Enjoy !!! :)")

print("-----bonus-----")

names = []
ages = []
price = 0
while True:
    want_to_buy = input ("do you want to buy ticket ?")
    if want_to_buy == "no":
        break
    names.append(input("name please ?"))
    ages.append(int(input("age please ?")))
    print("next")

generated_family = dict(zip(names, ages))

for name, age in generated_family.items():

    if age < 3:
        print("its free for you sweety :)")
        print("next !")

    elif 3 <= age <= 12:
        print("10$ please :)")
        price += 10
        print("next !")

    else:
        print("15$ please :)")
        price += 15
        print("next !")

print(f"Your final check is {price}$ !!! Enjoy !!! :)")
#EX2

#EX3
#INSTRUCTIONS

# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:
#     creation_date: 1975 
#     number_stores: 10 000
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ? answer : the num of store was updated from 7000 to 10000

brand = {
    "name": "Zara", 
    "creation_date": 1975, 
    "creator_name": "Amancio Ortega Gaona", 
    "type_of_clothes": ["men", "women", "children", "home"], 
    "international_competitors": ["Gap", "H&M", "Benetton"], 
    "number_stores": 7000,
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US":["pink", "green"]
    }
}
brand["number_stores"] = 2

print("We have clothe for", end = " ")
for client in brand["type_of_clothes"]:
    print(client, end = " ")
brand_name = brand["name"]
print(f"!!! just come check any {brand_name} near your home !!")

brand["country_creation"] = "spain"

key_present = "international_competitors"
if key_present in brand.keys():
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand))

print(brand.keys())

more_on_zara = {
    "creation_date": 1975, 
    "number_stores": 10000
}

brand.update(more_on_zara)

print(brand["number_stores"])
#EX3

#EX4
# INSTRUCTIONS:

#1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# 1-Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# 2-Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# 3-Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# 4-Only recreate the 1st result for:
#   -The characters, which names contain the letter “i”.
#   -The characters, which names start with the letter “m” or “p”.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

print("#1/")
disney_user_A = {name: idx for idx, name in enumerate(users)}
print(disney_user_A)

print("#2/")
disney_user_B = {idx: name for idx, name in enumerate(users)}
print(disney_user_B)

print("#3/")
disney_user_C = {name: idx for idx, name in enumerate(sorted(users))}
print(disney_user_C)

print("#4/")
disney_user_D = {name: idx for idx, name in enumerate(users) if "i" in name}
print(disney_user_D)

print("#5/")
disney_user_E = {name: idx for idx, name in enumerate(users) if name[0] == "M" or name[0] == "P"}
print(disney_user_E)
#EX4
