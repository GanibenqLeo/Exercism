def square(number:int):
    if 1 <= number <= 64:
        return square(number-1)*2 if number!=1 else 1
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    print("""Pour la dernière case il faudrait plus de 18 milliards de milliards de graines de blé soit plus de 700 milliards de tonnes de blé. 
    Entre 2014 et 2016 le monde a produit plus de 700 millions de tonnes de blé, 
    donc pour la dernière case il nous faut 30 ans de production moderne et mondiale""")

    sum = 0
    for i in range(1, 65):
        sum += square(i)

    return sum
