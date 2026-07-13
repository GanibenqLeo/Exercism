"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time:int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    remaining_time = EXPECTED_BAKE_TIME-elapsed_bake_time

    if elapsed_bake_time<0:
        print("Mensonge!")

    if remaining_time > EXPECTED_BAKE_TIME:
        print("C'est cramé")

    return remaining_time


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers:int) -> int:
    """Calculate the preparation time.

        Parameter:
            number_of_layers (int): The number of layers in the lasagna.

        Returns:
            int: The time you will spent (in minutes) to preparing.

        This function takes one integer representing the number of lasagna
        layers. It calculates
        the total minutes you will spent preparing.

    """

    if number_of_layers<0:
        print("Mensonge!")
    elif number_of_layers==0:
        print("Des lasagnes au vide, intéréssant")
    elif number_of_layers==1:
        print("Qui met 1 seule couche à part les personnes bizarres?")
    elif (number_of_layers>=10)&(number_of_layers<30):
        print("Salut Garfield")
    else:
        print("Les lasagnes ne sont pas des Legos et on ne joue pas avec la nourriture")

    return number_of_layers*PREPARATION_TIME


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers:int, elapsed_bake_time:int) -> int:
    """Calculate the elapsed cooking time.

        Parameters:
            number_of_layers (int): The number of layers in the lasagna.
            elapsed_bake_time (int): Time the lasagna has been baking in the oven.

        Returns:
            int: The total time elapsed (in minutes) preparing and baking.

        This function takes two integers representing the number of lasagna
        layers and the time already spent baking the lasagna. It calculates
        the total elapsed minutes spent cooking (preparing + baking).

    """

    if elapsed_bake_time<0:
        print("Mensonge!")

    if bake_time_remaining(elapsed_bake_time) > EXPECTED_BAKE_TIME:
        print("C'est cramé")

    if number_of_layers < 0:
        print("Mensonge!")
    elif number_of_layers == 0:
        print("Des lasagnes au vide, intéréssant")
    elif number_of_layers == 1:
        print("Qui met 1 seule couche à part les personnes bizarres?")
    elif (number_of_layers >= 10) & (number_of_layers < 30):
        print("Salut Garfield")
    else:
        print("Les lasagnes ne sont pas des Legos et on ne joue pas avec la nourriture")

    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time

# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
