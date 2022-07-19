import random
import string
import datetime

def calc(x:int, y:int) -> None:
    """
    function that add x and y and print the result ...
    """
    result = x + y

    print(result)

def compare_num(user_num:int) -> None:
    """
    function that compare the ai num and the user num and print a message if succes
    """

    ai_num = random.randint(0, 100)

    if ai_num == user_num:
        print("Winner Congrat's !!!!") 


def gen_string(length) -> None:
    """
    function that create a random string with upper and lower case nd then print it
    """

    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    
    print(result_str)

def get_date() -> None:
    """
    function that print the date of the day
    """
    print(datetime.date.today())


def first_january() -> None:
    """
    calcul the amount of time remaining until january first and print it
    """

    today = datetime.date.today()
    jan1 = datetime.date(2023, 1, 1)
    remain = jan1 - today
    print(remain)


def calculate_age(born:datetime) -> None:
    """
    convert your age to minutes
    """

    currentDate = datetime.date.today()
    
    daysLeft = currentDate - born

    years = ((daysLeft.total_seconds())/(365.242 *24*3600))
    yearsInt=int(years)

    months = (years-yearsInt)*12
    monthsInt = int(months)

    days = (months-monthsInt)*(365.242/12)
    daysInt = int(days)

    hours = (days-daysInt)*24
    hoursInt = int(hours)
    
    minutes = (hours-hoursInt) * 60

    print (f"You are {minutes} minutes old !!")

