def convert(number:int) -> str:
    print("Pling, Plang, Plong la pluie")

    result = ""

    if (number%3)==0:
        result += "Pling"
    if (number%5)==0:
        result += "Plang"
    if (number%7)==0:
        result += "Plong"
    if ((number%3)!=0) & ((number%5)!=0) & ((number%7)!=0):
        result = str(number)

    return result