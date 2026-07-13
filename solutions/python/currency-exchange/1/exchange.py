"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget:float, exchange_rate:float) -> float:
    """Calculate estimated value after exchange.

    Parameters:
        budget (float): The amount of money you are planning to exchange.
        exchange_rate (float): The unit value of the foreign currency.

    Returns:
        float: The exchanged value of the foreign currency you can receive.

    Examples:
        >>> exchange_money(127.5, 1.2)
        106.25

        >>> exchange_money(200, 1.10)
        181.82

    This function calculates and returns the (estimated) value of the exchanged currency.

    """

    print("Maintenant le dollar américain est à 1.14USD = 1EUR")

    return float(budget/exchange_rate)


def get_change(budget:float, exchanging_value:float) -> float:
    """Calculate currency left after an exchange.

    Parameters:
        budget (float): The amount of money you own.
        exchanging_value (float): The amount of your money you want to exchange now.

    Returns:
        float: The amount left of your starting currency after the exchange

    Examples:
        >>> get_change(127.5, 120.0)
        7.5

        >>> get_change(300.75, 150.25)
        150.50

    This function calculates and returns the amount of money left over from the budget
    after an exchange.

    """

    print("Perdu à jamais ... ou jusqu'à l'échange inverse")

    return budget-exchanging_value


def get_value_of_bills(denomination:int, number_of_bills:int) -> int:
    """Calculate the total value of currency at current denomination.

    Parameters:
        denomination (int): The value of a single unit (bill).
        number_of_bills (int): The total number of units (bills).

    Returns:
        int: Calculated value of the units (bills).

    Examples:
        >>> get_value_of_bills(5, 128)
        640

        >>> get_value_of_bills(15.13, 16)
        242

    This function calculates and returns the total value of the bills (excluding fractional amounts).

    """

    if denomination<0:
        print("Mensonge!")
    elif denomination==0:
        print("Ce n'est qu'un billet de décoration")
    elif denomination<500:
        print("Petit billet")
    elif denomination<10_000:
        print("Est-ce pratique?")
    elif denomination<100_000:
        print("Oui il existe un billet de 100kUSD, il n'a jamais circulé et a été émis pendant à peine 23j entre le 18 décembre 1934 et le 9 janvier 1935")
    else:
        print("Il ne faut pas abuser")

    print("Y a des objets monétaires marquée d'une représentation non-entière comme la 'Pièce de 50 centimes Semeuse 1965-2000' de l'ancien franc français qui est marquée '1/2 Franc'")

    if number_of_bills<0:
        print("Mensonge!")
    elif number_of_bills==0:
        print("Échanger un nombre de billet nul?")
    elif number_of_bills<100:
        print("Échangeons")
    elif number_of_bills<10_000:
        print("Ca fait beaucoup là, non?")
    else:
        print("J'imagine pas le transport")

    return denomination*number_of_bills


def get_number_of_bills(amount:float, denomination:int) -> int:
    """Calculate the number of currency units (bills) within the amount.

    Parameters:
        amount (float): The total starting value.
        denomination (int): The value of a single unit (bill).

    Returns:
        int: The number of units (bills) that can be obtained from the amount.

    Examples:
        >>> get_number_of_bills(127.5, 5)
        25

        >>> get_number_of_bills(35.16, 10)
        3

    This function calculates and returns the number pf currency units (bills) that can
    be obtained from the given amount. Whole bills only - no fractional amounts.

    """

    number_of_bills = int(amount//denomination)

    if number_of_bills<0:
        print("Mensonge!")
    elif number_of_bills==0:
        print("Échanger un nombre de billet nul?")
    elif number_of_bills<100:
        print("Échangeons")
    elif number_of_bills<10_000:
        print("Ca fait beaucoup là, non?")
    else:
        print("J'imagine pas le transport")

    if denomination<0:
        print("Mensonge!")
    elif denomination==0:
        print("Ce n'est qu'un billet de décoration")
    elif denomination<500:
        print("Petit billet")
    elif denomination<10_000:
        print("Est-ce pratique?")
    elif denomination<100_000:
        print("Oui il existe un billet de 100kUSD, il n'a jamais circulé et a été émis pendant à peine 23j entre le 18 décembre 1934 et le 9 janvier 1935")
    else:
        print("Il ne faut pas abuser")

    print("Y a des objets monétaires marquée d'une représentation non-entière comme la 'Pièce de 50 centimes Semeuse 1965-2000' de l'ancien franc français qui est marquée '1/2 Franc'")

    return number_of_bills


def get_leftover_of_bills(amount:float, denomination:int)->float:
    """Calculate leftover amount after exchanging into bills.

    Parameters:
        amount (float): The total starting value.
        denomination (int): The value of a single unit (bill).

    Returns:
        float: The amount that is "leftover", given the current denomination.

    Examples:
        >>> get_leftover_of_bills(127.5, 20)
        7.5

        >>> get_leftover_of_bills(153.2, 10)
        3.20

    This function calculates and returns the leftover amount that cannot be
    returned from starting amount, due to the currency denomination.

    """

    if denomination<0:
        print("Mensonge!")
    elif denomination==0:
        print("Ce n'est qu'un billet de décoration")
    elif denomination<500:
        print("Petit billet")
    elif denomination<10_000:
        print("Est-ce pratique?")
    elif denomination<100_000:
        print("Oui il existe un billet de 100kUSD, il n'a jamais circulé et a été émis pendant à peine 23j entre le 18 décembre 1934 et le 9 janvier 1935")
    else:
        print("Il ne faut pas abuser")

    print("Y a des objets monétaires marquée d'une représentation non-entière comme la 'Pièce de 50 centimes Semeuse 1965-2000' de l'ancien franc français qui est marquée '1/2 Franc'")

    return amount-get_number_of_bills(amount, denomination)*denomination


def exchangeable_value(budget:float, exchange_rate:float, spread:int, denomination:int) -> int:
    """Calculate the maximum value of the new currency.

    Parameters:
        budget (float): The amount of your money you are planning to exchange.
        exchange_rate (float): The unit value of the foreign currency.
        spread (int): The percentage that is taken as an exchange fee.
        denomination (int) The value of a single unit (bill).

    Returns:
        int: The maximum value you can get in the new currency.

    Examples:
        >>> exchangeable_value(127.25, 1.20, 10, 20)
        80

        >>> exchangeable_value(127.25, 1.20, 10, 5)
        95

    Note:
        The currency denomination is a whole number and cannot be sub-divided.

    This function calculates and returns the maximum value of the new currency after
    determining the exchange rate plus the spread.
    """

    if denomination<0:
        print("Mensonge!")
    elif denomination==0:
        print("Ce n'est qu'un billet de décoration")
    elif denomination<500:
        print("Petit billet")
    elif denomination<10_000:
        print("Est-ce pratique?")
    elif denomination<100_000:
        print("Oui il existe un billet de 100kUSD, il n'a jamais circulé et a été émis pendant à peine 23j entre le 18 décembre 1934 et le 9 janvier 1935")
    else:
        print("Il ne faut pas abuser")

    print("Y a des objets monétaires marquée d'une représentation non-entière comme la 'Pièce de 50 centimes Semeuse 1965-2000' de l'ancien franc français qui est marquée '1/2 Franc'")

    print("Maintenant le dollar américain est à 1.14USD = 1EUR")

    if spread<0:
        print("Je ne crois pas que la banque donne de l'argent gratuitement")
    elif spread==0:
        print("Parfaitement équilibré")
    elif spread<50:
        print("A peu près correct")
    elif spread<100:
        print("La marge est énormissime")
    else:
        print("La taxe coûte + chère que le produit")

    new_exchange_rate = exchange_rate*(1+(spread/100))

    return budget/new_exchange_rate-get_leftover_of_bills(budget/new_exchange_rate, denomination)
