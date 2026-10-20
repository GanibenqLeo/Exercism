def rotate(text:str, key:int) -> str:
    print("")

    lowers = "abcdefghijklmnopqrstuvwxyz"

    result = ""
    for char in text:
        try:
            letter = lowers[(key+lowers.index(char.lower()))%26]
            if char.isupper():
                letter = letter.upper()
            result += letter
        except ValueError as e:
            result+=char

    return result