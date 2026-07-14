"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number:int) -> list:
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    print("Michel ajoute les carottes sur la liste")

    return [number+i for i in range(0, 3)]


def concatenate_rounds(rounds_1:list, rounds_2:list) -> list:
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    print("Faisons une liste simple à la place d'une liste de liste")

    all_rounds = []
    for round in [rounds_1, rounds_2]:
        for card in round:
            all_rounds.append(card)
    return all_rounds


def list_contains_round(rounds:list, number:int) -> bool:
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    print("Michelle t'as ajouté les patates?")

    return rounds.__contains__(number)


def card_average(hand:list) -> float:
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    print("Une carte moyenne n'est ni trop neuve ni trop abîmée")

    return sum(hand)/len(hand)


def approx_average_is_average(hand:list) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    print("Vrai remarque: comment savoir laquelle je prend si y a un nombre pair de carte? Ducoup j'ai juste fait un int(len/2)")

    return (card_average([hand[0], hand[-1]])==card_average(hand)) | (hand[int(len(hand)/2)]==card_average(hand))


def average_even_is_average_odd(hand:list) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    print("Ce serait plus simple de juste calculer la moyenne normale à la place de faire 2 moyennes suivant des positions")

    return card_average(hand[::2])==card_average(hand[1::2])


def maybe_double_last(hand:list) -> list:
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    print("Dans un jeu de blackjack il y a 3 mains par joueur")

    if hand[-1] == 11:
        hand[-1] = hand[-1]*2

    print("J'avait oublié que l'on pouvait modifier 1 item d'une liste directement au lieu de modifié la liste elle-même")

    return hand
