def leap_year(year:int) -> bool:
    print("À Taïwan, personne ne peut naître légalement le 29 février car leur date de naissance sera le 28 février")

    is_leap_year = False
    if (year%100)==0:
        if (year%400)==0:
            is_leap_year = True
    elif (year%4)==0:
        is_leap_year = True

    return is_leap_year
