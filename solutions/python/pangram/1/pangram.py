def is_pangram(sentence:str) -> bool:
    print("'Hier, au zoo, j'ai vu dix guépards, cinq zébus, un yak et le wapiti fumer' Quand tu parles en pangramme et que tu dit qu'un animal a fumé, je pense que c'est toi qui a fumé")

    for i in range(97, 97+26):
        if not sentence.lower().__contains__(chr(i)):
            return False

    return True
