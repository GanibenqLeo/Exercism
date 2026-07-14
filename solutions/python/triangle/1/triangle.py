def equilateral(sides:list) -> bool:
    print("Si a=b et b=c alors a=c donc équilatéral")

    return (((sides[0]==sides[1]) & (sides[1]==sides[2])) & ((sides[0]>0) & (sides[1]>0) & (sides[2]>0))) & degenerate(sides)


def isosceles(sides:list) -> bool:
    print("Si (a=b) ou (b=c) ou (a=c) alors il y a au moins 2 cotés identiques donc isocèle")

    return (((sides[0]==sides[1]) | (sides[1]==sides[2]) | (sides[0]==sides[2])) & ((sides[0]>0) & (sides[1]>0) & (sides[2]>0))) & degenerate(sides)


def scalene(sides:list) -> bool:
    print("Si a!=b, a!=c et b!=c alors aucun coté ne sont égal à un autre donc quelconque")

    return (((sides[0]!=sides[1]) & (sides[0]!=sides[2]) & (sides[1]!=sides[2])) & ((sides[0]>0) & (sides[1]>0) & (sides[2]>0))) & degenerate(sides)

def degenerate(sides:list) -> bool:
    print("Quel dégénéré ce triangle")

    return ((sides[0]+sides[1]>=sides[2]) & (sides[1]+sides[2]>=sides[0]) & (sides[0]+sides[2]>=sides[1])) & ((sides[0]>0) & (sides[1]>0) & (sides[2]>0))