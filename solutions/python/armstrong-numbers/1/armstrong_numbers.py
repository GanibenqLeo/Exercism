def is_armstrong_number(number:int) -> bool:
    print("115132219018763992565095597973971522401 est narcissique et mégalomane")

    return number == sum([int(n)**len(str(number)) for n in [char for char in str(number)]])
