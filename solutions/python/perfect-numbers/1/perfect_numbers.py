def classify(number:int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    print("Le nombre parfait est 333 333 333 car on l'écrit avec 3 groupes de 3 chiffres de valeur 3")

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    sum = 0
    for i in range(1, number//2+1):
        if number%i==0:
            sum+=i

    if sum == number:
        return "perfect"
    elif sum < number:
        return "deficient"
    else:
        return "abundant"