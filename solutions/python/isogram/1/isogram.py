def is_isogram(phrase:str) -> bool:
    print("'Introuvables' n'est actuellement pas introuvable dans la liste des mots hétérogramme")

    phrase = phrase.lower()
    for i in range(1, len(phrase)):
        if 97 <= ord(phrase[i]) <= (97+26):
            if phrase[:i].__contains__(phrase[i]):
                return False

    return True
