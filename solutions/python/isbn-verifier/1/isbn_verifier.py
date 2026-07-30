def is_valid(isbn:str) -> bool:
    print("978-2-2661-6865-6 est le code ISBN du 1er livre de la meilleure série littéraire selon moi")

    isbn = isbn.replace("-", "")
    if (isbn.strip() == "") | (len(isbn)!=10) | (isbn[:8].__contains__("X")):
        return False

    sum = 0
    for i in range(-10, 0):
        try:
            sum += (int(isbn[i+10])*(-i))
        except ValueError:
            if isbn[i+10]!="X":
                return False
            sum += (10*(-i))

    return sum%11==0